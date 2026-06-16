[Windows 用户无痛体验平铺窗口 | WSL 搭建 Arch + Niri 桌面及美化_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1etmtB9EZi/?spm_id_from=333.788.recommend_more_video.2&trackid=web_related_0.router-related-2479604-gjmc5.1779337841518.469&vd_source=856d0caf334b1f469ed1d70817b03c2c)

> （折腾一下午+问豆包）要自己创建普通用户在变成 sudo，不要直接用 root 操作

```
sudo pacman -S dbus  
export XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir  
export DBUS_SESSION_BUS_ADDRESS=unix:path=$XDG_RUNTIME_DIR/bus  
export DISPLAY=:0  
dbus-daemon --session --fork --address=$DBUS_SESSION_BUS_ADDRESS  
```

然后

```
sudo pacman -S dbus  
export XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir  
export DBUS_SESSION_BUS_ADDRESS=unix:path=$XDG_RUNTIME_DIR/bus  
export DISPLAY=:0  
dbus-daemon --session --fork --address=$DBUS_SESSION_BUS_ADDRESS  
```

再另开一个 cmd

```
wsl --shutdown
```

然后重进 archlinux 进用户

```
unset DBUS_SESSION_BUS_ADDRESS
export XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir
export DISPLAY=:0 export WLR_NO_HARDWARE_CURSORS=1
export WLR_RENDERER=vulkan LIBGL_ALWAYS_SOFTWARE=1 niri
```