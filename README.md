# 山东联通 IPTV 播放列表

本项目内容**禁止用于**任何形式的[商业行为](https://github.com/plsy1/iptv/issues/15)，使用本项目即表示您同意遵守此规定。

## 使用说明

### 单播

目前山东联通单播仅支持 RTP over UDP，处于 NAT 环境下的设备无法直接收到 RTP 数据，要正常收看单播需满足以下条件之一：

- 有公网 IPV4，通过 PPPoE 接口访问（山东联通默认分配公网 IP，如无，可在宽带账号后面加 `@e` 再拨号）  
- 无公网 IPV4，想办法穿透 NAT，可部署 [rtsproxy](https://github.com/plsy1/rtsproxy)
- 通过 IPTV 接口访问（仅支持宽带所在地区的单播源）

### 组播

- 推荐使用 [rtp2httpd](https://github.com/stackia/rtp2httpd) 代理组播数据，支持 FCC 快速频道切换，起播/换台体验接近单播  
- 播放设备可直接接收组播数据

## 订阅链接

### 单播

| 播放器    | 直链                                                                                    | 代理1                                                                                   | 代理2                                                                                                       |
| --------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| APTV      | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/unicast/unicast-aptv.m3u)      | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/unicast/unicast-aptv.m3u)      | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/unicast/unicast-aptv.m3u)      |
| 酷九      | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/unicast/unicast-ku9.m3u)       | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/unicast/unicast-ku9.m3u)       | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/unicast/unicast-ku9.m3u)       |
| rtp2httpd | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/unicast/unicast-rtp2httpd.m3u) | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/unicast/unicast-rtp2httpd.m3u) | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/unicast/unicast-rtp2httpd.m3u) |

### 组播

| 地区 | 直链                                                                                        | 代理1                                                                                       | 代理2                                                                                                           |
| ---- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| 济南 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-jinan.m3u)     | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-jinan.m3u)     | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-jinan.m3u)     |
| 青岛 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-qingdao.m3u)   | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-qingdao.m3u)   | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-qingdao.m3u)   |
| 淄博 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-zibo.m3u)      | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-zibo.m3u)      | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-zibo.m3u)      |
| 枣庄 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-zaozhuang.m3u) | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-zaozhuang.m3u) | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-zaozhuang.m3u) |
| 东营 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-dongying.m3u)  | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-dongying.m3u)  | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-dongying.m3u)  |
| 烟台 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-yantai.m3u)    | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-yantai.m3u)    | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-yantai.m3u)    |
| 潍坊 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-weifang.m3u)   | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-weifang.m3u)   | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-weifang.m3u)   |
| 济宁 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-jining.m3u)    | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-jining.m3u)    | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-jining.m3u)    |
| 泰安 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-taian.m3u)     | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-taian.m3u)     | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-taian.m3u)     |
| 威海 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-weihai.m3u)    | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-weihai.m3u)    | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-weihai.m3u)    |
| 日照 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-rizhao.m3u)    | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-rizhao.m3u)    | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-rizhao.m3u)    |
| 莱芜 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-laiwu.m3u)     | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-laiwu.m3u)     | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-laiwu.m3u)     |
| 临沂 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-linyi.m3u)     | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-linyi.m3u)     | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-linyi.m3u)     |
| 德州 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-dezhou.m3u)    | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-dezhou.m3u)    | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-dezhou.m3u)    |
| 聊城 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-liaocheng.m3u) | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-liaocheng.m3u) | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-liaocheng.m3u) |
| 滨州 | [直链](https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-binzhou.m3u)   | [代理1](https://fastly.jsdelivr.net/gh/plsy1/iptv@master/multicast/multicast-binzhou.m3u)   | [代理2](https://ghfast.top/https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-binzhou.m3u)   |

## 频道变动

| 时间       | 更新内容 |
| ---------- | -------- |
| 2025-09-27 | 上线频道: 山东卫视4K超高清, 湖南卫视4K超高清, 浙江卫视4K超高清, 江苏卫视4K超高清, 东方卫视4K超高清, 四川卫视4K超高清 |
| 2025-10-20 | 上线频道: 环球旅游; 下线频道: 环球旅游标清 |
| 2025-12-21 | 下线频道: 宁夏卫视, CCTV3, CCTV5, CCTV6, CCTV8 |
| 2025-12-31 | 下线频道: 先锋乒羽, 财富天下 |

## 相关仓库

| 功能说明                       | 仓库链接                                      |
| ------------------------------ | --------------------------------------------- |
| IPTV 机顶盒登录鉴权模拟        | https://github.com/plsy1/shandong-unicom-iptv |
| EPG 节目单                     | https://github.com/plsy1/epg                  |
| RTSP 代理工具                  | https://github.com/plsy1/rtsproxy             |
| IPTV 数据抓取与生成 M3U 工具   | https://github.com/plsy1/iptvTool             |
| 山东各区县频道（爱齐鲁网络源） | https://github.com/plsy1/iqilu                |

## 免责声明

本项目仅用于学习与技术交流，所有资源均来自互联网公开内容。作者不对内容的合法性、准确性或可用性作任何保证，使用本项目所产生的一切风险与后果由使用者自行承担，请于下载后 24 小时内删除。如有侵权请联系删除。

## 历史统计

[![Star History Chart](https://api.star-history.com/svg?repos=plsy1/iptv&type=date&legend=top-left)](https://www.star-history.com/#plsy1/iptv&type=date&legend=top-left)