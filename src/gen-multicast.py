import json


base_url = 'http://192.168.0.1:4022/rtp/'


def generate_m3u(json_data):
    m3u_content = '#EXTM3U\n'

    for channel in json_data:
        if 'ChannelURL' in channel and channel['ChannelURL'].startswith('igmp://'):
            cleaned_url = channel['ChannelURL'].replace('igmp://', '')
            full_url = f'{base_url}{cleaned_url}'

            group_title = '央视频道' if 'CCTV' in channel['ChannelName'] else '其他'
            group_title = '卫视频道' if '卫视' in channel['ChannelName'] else '其他'
            
            m3u_content += f'#EXTINF:-1 tvg-id="{channel["UserChannelID"]}" tvg-name="{channel["ChannelName"]}" group-title="{group_title}", {channel["ChannelName"]}\n'
            m3u_content += f'{full_url}\n'
        else:
            print(f"频道 {channel['ChannelID']} 没有 ChannelURL,跳过")

    return m3u_content


def create_m3u(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

        m3u_content = generate_m3u(json_data)

        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(m3u_content)
        print(f'M3U 文件已成功保存到 {output_filename}')

    except FileNotFoundError as e:
        print(f'文件未找到: {e}')
    except json.JSONDecodeError as e:
        print(f'解析 JSON 时发生错误: {e}')
    except Exception as e:
        print(f'发生错误: {e}')
        
        
create_m3u('iptv.json', 'multicast.m3u')