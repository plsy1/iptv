import subprocess

start = 100000
end = 100100

for i in range(start, end + 1):
    
    base = 'rtsp://112.245.125.47:1554/iptv/import/Tvod/iptv/001/001/ch15050917541659846769.rsc'
    url = f"{base}/{i}_Uni.sdp"

    print(f"正在测试播放: {url}")

    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'debug', url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )

        if "Video:" in result.stderr or "Stream #0" in result.stderr:
            print(f"成功获取视频流: {url}")
            exit()
            
    except subprocess.TimeoutExpired:
        print(f"超时: {url}")

    except Exception as e:
        print(f"发生错误 {e}，检查地址: {url}")
