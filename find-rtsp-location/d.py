import subprocess
import time
import json


with open('extracted_channels.json', 'r', encoding='utf-8') as file:
    channels = json.load(file)


rtsp_template = "rtsp://{ip}:1554/iptv/Tvod/iptv/001/001/{channel_id}.rsc?tvdr=20250407061300GMT-20250407064700GMT"


success_channels_file = 'rtsp.json'

# 检查 RTSP 流的函数
def check_rtsp(ip, channel_name, channel_id):
    rtsp_url = rtsp_template.format(ip=ip, channel_id=channel_id)
    print(f"正在检查 RTSP 地址: {rtsp_url} ({channel_name})")
    
    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'debug', rtsp_url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )

        if "Video:" in result.stderr or "Stream #0" in result.stderr:
            print(f"成功获取视频流: {rtsp_url}")

            success_data = {
                "ChannelName": channel_name,
                "RTSPURL": rtsp_url
            }

            with open(success_channels_file, 'a', encoding='utf-8') as output_file:
                json.dump(success_data, output_file, ensure_ascii=False)
                output_file.write("\n")
            return True 
        else:
            print(f"未能获取视频流: {rtsp_url}")
            return False
    except subprocess.TimeoutExpired:
        print(f"超时: {rtsp_url}")
        return False
    except Exception as e:
        print(f"发生错误 {e}，检查地址: {rtsp_url}")
        return False

# 遍历提取的频道并检查 RTSP 流
for channel in channels:
    channel_name = channel.get("ChannelName")
    channel_id = channel.get("ChannelID")
    

    for i in range(30, 51):  
        ip = f"112.245.125.{i}"
        if check_rtsp(ip, channel_name, channel_id):
            break  
        time.sleep(1)