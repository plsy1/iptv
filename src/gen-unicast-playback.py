import re

def generate_playback_m3u(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    timeshift = '{utc:YmdHMS}GMT-{utcend:YmdHMS}GMT'
    pattern = r"(rtsp://\S+:\d+).*?(ch\d*)"
    channel_name = ''
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            if line.startswith('#EXTINF'):
                match = re.search(r'#EXTINF:-1, (.+)', line)
                if match:
                    channel_name = match.group(1)
            elif line.startswith('rtsp://'):
                match = re.search(pattern, line)
                if match:
                    url = match.group(1)
                    cid = match.group(2)
                    playbackURL = f'{url}/iptv/Tvod/iptv/001/001/{cid}.rsc?tvdr={timeshift}'
                    foo = f'#EXTINF:-1 catchup-source="{playbackURL}", {channel_name}\n'
                    outfile.write(foo)
                    outfile.write(line)
    
    print(f"Generated playback M3U file: {output_file}")

if __name__ == "__main__":
    input_m3u_file = 'unicast-live.m3u'
    output_m3u_file = 'unicast-playback.m3u'
    generate_playback_m3u(input_m3u_file, output_m3u_file)