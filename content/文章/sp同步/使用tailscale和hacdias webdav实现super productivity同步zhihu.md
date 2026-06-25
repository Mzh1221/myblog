---
zhihu-title: 使用tailscale和hacdias webdav实现super productivity同步
zhihu-topics: 同步
zhihu-link: https://zhuanlan.zhihu.com/p/2036476902165190041/edit
zhihu-toc: "1"
---
![[Pasted image 20260508104901.png]]
# 前言

同步提供商选项中前三者都是国外的服务器，localfile 也弃用了，可以使用的只剩 WebDAV。我的需求是 windows 和 android 双向同步，了解到坚果云等 WebDAV 会有跨域限制，遂自建

# 各组件作用
- hacdias-webdav：轻量、稳定、跨平台私有 WebDAV 服务，作为同步核心存储
- Tailscale：零配置内网穿透，无需公网 IP、无需路由器端口映射，设备点对点加密传输

# 前期环境准备
- 服务端设备：Windows / Mac / Linux（常驻开机设备，作为同步服务器）
- 软件准备：
	- hacdias-webdav [hacdias/webdav: A simple and standalone WebDAV server.](https://github.com/hacdias/webdav)
	- Tailscale [Tailscale | Secure Connectivity for AI, IoT & Multi-Cloud](https://tailscale.com/)
- 客户端设备：手机、平板、其他电脑（需要同步的终端）
- 基础前置：设备可正常联网，服务端无 6065 端口占用

# 具体步骤
## tailscale
前往 tailscale 官网下载安装，运行后在托盘登陆
![[Pasted image 20260508211923.png]]
会跳转到官网，选择一个你方便的方式登陆
![[Pasted image 20260508212019.png]]
登陆后会发现本机已经加入了设备列表，然后手机端也是同样下载 tailscale （安卓用不了谷歌商店可以到 apkcombo 之类的网站下载）登陆相同的账号就会把手机自动加入设备列表
![[Pasted image 20260508212852.png]]
这样设置可以禁止密钥过期，以后就不用反复登陆了

## hacdias webdav
先单独建一个文件夹装同步的东西，从 github 在电脑端下载解压到这个文件夹里，再在这个文件夹里新建一个 config.yml 文件，写入以下（自己修改一下）保存
```yml
address: 0.0.0.0
port: 6065
directory: 该文件夹路径 # e.g. C:\sp_sync
permissions: crud
auth:
  type: basic
users:
- username: 随便写个账号 # spsync
  password: 随便写个密码 # sp1234
```
## 启动 webdav 服务
win+R 输入 cmd 打开 cmd，输入
```
cd /d 文件夹路径 # 例如 C:\sp_sync
webdav.exe -c config.yml
```
不要关闭

也可以直接写成 bat 批处理
```
cd /d 路径
webdav.exe -c config.yml
pause
```

## super productivity 配置
![[Pasted image 20260508214140.png]]
进入设置
![[Pasted image 20260508214302.png]]
选择 webdav
![[Pasted image 20260508214338.png]]
以下配置就这样填，账号密码填你之前 config.yml 里写的
![[Pasted image 20260508214503.png]]
点击测试链接，显示测试链接成功就说明通了，手机上一样配置，高级配置里还可以设置自动同步间隔和是否启用压缩

## 测试
你可以在电脑上创建任务点同步，你会发现那个新建文件夹多出来了个 sync-data.json 文件，这就是 sp 的数据，你再在手机 sp 点击同步会发现很快任务就拉到本地了，手机也是同样可以同步到电脑上
![[Pasted image 20260508215343.png]]

## 拓展
obsidian 也可以这样配置在 remotely save 插件，但是 obsidian 可以直接用坚果云不会有跨域的问题。如果搭好了 webdav 可以顺便简单得给 ob 一起同步过来