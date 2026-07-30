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
| 2026-02-04 | 上线频道: 财富天下 |
| 2026-04-01 | 下线频道: 茶高清 |
| 2026-04-17 | 上线频道: 陕西卫视高清, 内蒙古卫视高清; 下线频道: 陕西卫视, 内蒙古卫视 |
| 2026-05-20 | 下线频道: 中华特产 |
| 2026-07-30 | 上线频道: CCTV1综合, 山东卫视, CCTV2财经, CCTV3综艺, CCTV4中文国际, CCTV5体育, CCTV5体育赛事, CCTV6电影, CCTV7国防军事, CCTV8电视剧, CCTV9纪录, CCTV10科教, CCTV11戏曲, CCTV12社会与法, CCTV13新闻, CCTV14少儿, CCTV15音乐, CCTV17农业农村, CGTN英语, 齐鲁频道, 山东文旅, 山东生活, 山东综艺, 山东体育, 山东新闻, 山东农科, 山东少儿, 山东教育卫视, 湖南卫视, 浙江卫视, 东方卫视, 江苏卫视, 北京卫视, 安徽卫视, 天津卫视, 辽宁卫视, 深圳卫视, 东南卫视, 湖北卫视, 广东卫视, 黑龙江卫视, 贵州卫视, 河北卫视, 重庆卫视, 海南卫视, 四川卫视, 山西卫视标清, 河南卫视, 江西卫视, 广西卫视, 吉林卫视, 云南卫视, 陕西卫视, 内蒙古卫视, 宁夏卫视, 新疆卫视, 甘肃卫视, 青海卫视, 西藏卫视, 优漫卡通标清, 嘉佳卡通标清, 兵团卫视, 农林卫视标清, 厦门卫视标清, 中国教育1, 中国教育2标清, 中国教育4, 金鹰纪实, 延边卫视标清, 三沙卫视标清, 发现之旅标清, 中学生标清, 老故事标清, CGTN英文纪录, CGTN西班牙语, CGTN法语, CGTN阿拉伯语, CGTN俄语, CHC家庭影院, CHC动作电影, 动漫秀场, 金色学堂, 生活时尚, 都市剧场, 乐游, 法治天地, 游戏风云, 东方财经, 梨园, 武术世界, 文物宝库, 精彩影视, 快乐垂钓, 金鹰卡通, 优购物标清, 央广购物标清; 下线频道: CCTV1高清, 山东卫视高清, CCTV2高清, CCTV3高清, CCTV4高清, CCTV5高清, CCTV5高清, CCTV6高清, CCTV7高清, CCTV8高清, CCTV9高清, CCTV10高清, CCTV11高清, CCTV12高清, CCTV13高清, CCTV少儿高清, CCTV15高清, CCTV17农业高清, CGTN 英语, 齐鲁高清, 山东文旅高清, 山东生活高清, 山东综艺高清, 山东体育高清, 山东新闻高清, 山东农科高清, 山东少儿高清, 山东教育卫视高清, 湖南卫视高清, 浙江卫视高清, 东方卫视高清, 江苏卫视高清, 北京卫视高清, 安徽卫视高清, 天津卫视高清, 辽宁卫视高清, 深圳卫视高清, 东南卫视高清, 湖北卫视高清, 广东卫视高清, 黑龙江卫视高清, 贵州卫视高清, 河北卫视高清, 重庆卫视高清, 海南卫视高清, 四川卫视高清, 山西卫视, 河南卫视高清, 江西卫视高清, 广西卫视高清, 吉林卫视高清, 云南卫视高清, 陕西卫视高清, 内蒙古卫视高清, 宁夏卫视高清, 新疆卫视高清, 甘肃卫视高清, 青海卫视高清, 西藏卫视高清, 优漫卡通, 嘉佳卡通, 兵团卫视高清, 农林卫视, 厦门卫视, 中国教育1高清, 中国教育2, 中国教育4高清, 金鹰纪实高清, 延边卫视, 三沙卫视, 发现之旅, 中学生, 老故事, CGTN 英文纪录, CGTN 西班牙语, CGTN 法语, CGTN 阿拉伯语, CGTN 俄语, CHC家庭影院高清, CHC动作电影高清, 新动漫, 动漫秀场高清, 金色学堂高清, 生活时尚高清, 都市剧场高清, 乐游高清, 法治天地高清, 游戏风云高清, 东方财经高清, 梨园高清, 武术世界高清, 文物宝库高清, 精彩影视高清, 快乐垂钓高清, 金鹰卡通高清, 优购物, 央广购物 |
| 2026-07-30 | 上线频道: CCTV７国防军事; 下线频道: CCTV7国防军事 |

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