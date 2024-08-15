## login
```shell
curl -X POST "http://202.99.114.14:35824/PORTAL/dsm/loginByUserId" \
-H "Content-Type: application/json; charset=utf-8" \
-H "Accept: application/json" \
-H "Host: 202.99.114.14:35824" \
-H "Connection: Keep-Alive" \
-c cookies.txt \
--data '{"accessChannel":"16","model":"E900V21C","osVersion":"4.4.2","userId":"","accessItem":"1","versionCode":"3200","mac":"00000FFFFFF","password":"","ip":""}'
```

## getChannelNameByChanneld

```shell
curl -X GET "http://112.245.125.58:8080/iptvepg/frame205/getChannelInfo.jsp?CHANNELID=26" \
-H "Host: 112.245.125.58:8080" \
-H "Connection: keep-alive" \
-H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; SkyworthBrowser) AppleWebKit/534.24 (KHTML, like Gecko) Safari/534.24 SkWebKit-SD-CU" \
-H "Cookie: JSESSIONID=; "
```

## channelData

```shell
curl -X GET "http://112.245.125.58:8080/iptvepg/frame205/action/channel_data.jsp?columnid=1D04" \
-H "Host: 112.245.125.58:8080" \
-H "Connection: keep-alive" \
-H "Pragma: no-cache" \
-H "Cache-Control: no-cache" \
-H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; SkyworthBrowser) AppleWebKit/534.24 (KHTML, like Gecko) Safari/534.24 SkWebKit-SD-CU" \
-H "Accept: */*" \
-H "Accept-Encoding: gzip,deflate" \
-H "Accept-Language: zh-cn,en-us,en" \
-H "Cookie: JSESSIONID=;" \
--output channel_data.gz
```

## getChannelProgram

```shell
curl -X GET "http://112.245.125.58:8080/iptvepg/frame205/action/getchannelprogram.jsp?channelcode=ch00000000000000001170&currdate=2024.08.14" \
-H "Host: 112.245.125.58:8080" \
-H "Connection: keep-alive" \
-H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; SkyworthBrowser) AppleWebKit/534.24 (KHTML, like Gecko) Safari/534.24 SkWebKit-SD-CU" \
-H "Cookie: JSESSIONID=; " 
```



