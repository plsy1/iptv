import json
import subprocess
import re

def get_redirected_rtsp(rtsp_url):
    command = [
        'ffprobe', 
        '-print_format', 'json', 
        '-i', rtsp_url
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stderr

        redirect_match = re.search(r'Redirecting to (rtsp://[^\s]+Uni\.sdp)', output)
        if redirect_match:
            return redirect_match.group(1)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running ffprobe: {e}")
        return None

    return None

def extract_live_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    rtsp_data = []
    for channel in data:
        if 'ChannelSDP' in channel:
            sdp_url = channel['ChannelSDP']
            match = re.search(r'rtsp://\S+', sdp_url)
            if match:
                rtsp_url = match.group(0)
                channel_name = channel.get('ChannelName', 'Unknown Channel')

                redirected_rtsp = get_redirected_rtsp(rtsp_url)
                if redirected_rtsp:
                    rtsp_url = redirected_rtsp
                    print(f'{channel_name}: {rtsp_url}')
                else:
                    print(f'获取单播地址失败：{channel_name}')
                rtsp_data.append((channel_name, rtsp_url))
    
    return rtsp_data

def write_live_to_m3u_file(file_path, rtsp_data):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        for channel_name, rtsp_url in rtsp_data:
            f.write(f"#EXTINF:-1, {channel_name}\n")
            f.write(f"{rtsp_url}\n")
            
            

def main():
    
    json_file_path = 'iptv.json'
    live_m3u_file_path = 'unicast-live.m3u'
    
    live_data = extract_live_from_json(json_file_path)
    
    if live_data:
        print(f"Found {len(live_data)} channels with RTSP URLs.")
        write_live_to_m3u_file(live_m3u_file_path, live_data)
        print(f"Live M3U file generated at {live_m3u_file_path}.")
    else:
        print("No RTSP URLs found in the provided JSON.")
        

if __name__ == "__main__":
    main()