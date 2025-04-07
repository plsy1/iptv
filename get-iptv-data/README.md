```bash
curl -X POST http://112.245.125.58:8080/iptvepg/function/frameset_builder.jsp \
  -H "Connection: keep-alive" \
  -H "Content-Length: 137" \
  -H "Pragma: no-cache" \
  -H "Cache-Control: no-cache" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" \
  -H "Origin: http://112.245.125.58:8080" \
  -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; SkyworthBrowser) AppleWebKit/534.24 (KHTML, like Gecko) Safari/534.24 SkWebKit-SD-CU" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Referer: http://112.245.125.58:8080/iptvepg/function/frameset_judger.jsp" \
  -H "Accept-Encoding: gzip,deflate" \
  -H "Accept-Language: zh-cn,en-us,en" \
  -H "Cookie: JSESSIONID=DCF282C4602D56DDF5F791F73C03CDFD" \
  --data-urlencode "MAIN_WIN_SRC=%2Fiptvepg%2Fframe205%2Fchannel_start.jsp%3Ftempno%3D-1" \
  --data-urlencode "NEED_UPDATE_STB=1" \
  --data-urlencode "BUILD_ACTION=FRAMESET_BUILDER" \
  --data-urlencode "hdmistatus=undefined" \
  --compressed \
  --output ip.txt
```

抓上面这个，gbk编码，只保留：

```javascript
                    jsSetConfig('Channel','ChannelID="ch00000000000000001128",ChannelName="CCTV1����",UserChannelID="1",ChannelURL="igmp://239.253.240.77:8000",TimeShift="1",ChannelSDP="igmp://239.253.240.77:8000|rtsp://124.132.240.33:554/live/ch12122514263996485740.sdp?playtype=1&boid=001&clienttype=1&time=20250407235707+08&life=172800&ifpricereqsnd=1&vcdnid=001&userid=053804273545&mediaid=ch12122514263996485740&ctype=5&TSTVTimeLife=10800&authid=0&UserLiveType=1&stbid=00000437001990001804C88F26A40177&nodelevel=3&terminalflag=1&profilecode=&AuthInfo=KDm3K2AxeC7UXvB6yhSxWgVa8oII%2BCRGuWrcsXPGqOS0Kz0d4JSyXiWnNGHVXV0qao7DtBd%2FI6J7wOATC1lpdQ%3D%3D&bitrate=8&distype=0&usersessionid=430449831",TimeShiftURL="rtsp://124.132.240.33:554/live/ch12122514263996485740.sdp?playtype=1&boid=001&clienttype=1&time=20250407235707+08&life=172800&ifpricereqsnd=1&vcdnid=001&userid=053804273545&mediaid=ch12122514263996485740&ctype=5&TSTVTimeLife=10800&authid=0&UserLiveType=1&stbid=00000437001990001804C88F26A40177&nodelevel=3&terminalflag=1&profilecode=&AuthInfo=KDm3K2AxeC7UXvB6yhSxWgVa8oII%2BCRGuWrcsXPGqOS0Kz0d4JSyXiWnNGHVXV0qao7DtBd%2FI6J7wOATC1lpdQ%3D%3D&bitrate=8&distype=0&usersessionid=430449831",ChannelLogURL="",PositionX="1",PositionY="1",BeginTime="0",Interval="-1",Lasting="0",ChannelType="2",ChannelPurchased="",LocalTimeShift="0",UserTeamChannelID="1",TimeShiftLength="10800",telecomcode="00000001000000050000000000000152",FCCEnable="1",FCCFunction="1",ChannelFCCIP="124.132.240.66",ChannelFCCPort="15970"');
                
```

运行a.js，生成iptv.json

