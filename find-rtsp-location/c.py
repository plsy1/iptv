import json
import re

# 读取 IPTV JSON 文件
with open('iptv.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 用来存储提取的结果
output_data = []

# 遍历每一项
for channel in data:
    # 提取 ChannelName 和 TimeShiftURL
    channel_name = channel.get("ChannelName")
    time_shift_url = channel.get("ChannelSDP")

    # 使用正则表达式提取 chxxxxxxx 部分
    match = re.search(r'ch\d+', time_shift_url)
    if match:
        channel_id = match.group(0)
        output_data.append({
            "ChannelName": channel_name,
            "ChannelID": channel_id
        })

# 将结果保存为新的 JSON 文件
with open('extracted_channels.json', 'w', encoding='utf-8') as output_file:
    json.dump(output_data, output_file, ensure_ascii=False, indent=4)

print("数据已提取并保存到 'extracted_channels.json'")