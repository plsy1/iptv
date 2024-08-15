const fs = require('fs');

function generateM3U(jsonData) {
  const baseURL = 'http://192.168.0.1:4022/rtp/';
  let m3uContent = '#EXTM3U\n'; // M3U 文件的头部

  jsonData.forEach(channel => {
    if (channel.ChannelURL) {
      const cleanedURL = channel.ChannelURL.replace(/^igmp:\/\/|^rtsp:\/\//, '');
      const fullURL = `${baseURL}${cleanedURL}`;

      // 根据 ChannelName 判断 group-title
      const groupTitle = channel.ChannelName.includes('CCTV') ? '央视频道' : '其他';

      m3uContent += `#EXTINF:-1 tvg-id="${channel.UserChannelID}" tvg-name="${channel.ChannelName}" group-title="${groupTitle}", ${channel.ChannelName}\n`;
      m3uContent += `${fullURL}\n`;
    } else {
      console.warn(`频道 ${channel.ChannelID} 没有 ChannelURL`);
    }
  });

  return m3uContent;
}

async function createM3U(inputFilename, outputFilename) {
  fs.readFile(inputFilename, (err, data) => {
    if (err) {
      console.error('读取文件时发生错误:', err);
      return;
    }

    let jsonData;
    try {
      jsonData = JSON.parse(data);
    } catch (parseErr) {
      console.error('解析 JSON 时发生错误:', parseErr);
      return;
    }

    const m3uContent = generateM3U(jsonData);
    
    fs.writeFile(outputFilename, m3uContent, writeErr => {
      if (writeErr) {
        console.error('写入文件时发生错误:', writeErr);
      } else {
        console.log('M3U 文件已成功保存到', outputFilename);
      }
    });
  });
}

createM3U('iptv.json', 'playlist.m3u');