const fs = require('fs');
const readline = require('readline');

function convertToJSON(data) {
  const cleanedData = data.replace(/^\(|\)$/g, '');
  const keyValuePairs = cleanedData.split(/,(?=(?:[^"]*"[^"]*")*[^"]*$)/);
  const jsonObject = {};

  keyValuePairs.forEach(pair => {
    const [key, value] = pair.split('=');
    if (key && value) {
      const cleanKey = key.trim().replace(/^"|"$/g, '');
      const cleanValue = value.trim().replace(/^"|"$/g, '').replace(/\\n/g, '\n');
      jsonObject[cleanKey] = cleanValue;
    }
  });
  return jsonObject;
}


async function processFile(inputFilename, outputFilename) {
  const fileStream = fs.createReadStream(inputFilename);
  const writeStream = fs.createWriteStream(outputFilename);
  
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  const jsonObjects = [];

  for await (const line of rl) {
    if (line.trim()) {
      const jsonObject = convertToJSON(line);
      jsonObjects.push(jsonObject); 
    }
  }

  writeStream.write(JSON.stringify(jsonObjects, null, 2), err => {
    if (err) {
      console.error('写入文件时发生错误:', err);
    } else {
      console.log('数据已成功保存到', outputFilename);
    }
  });
}

processFile('iptv.txt', 'iptv.json');