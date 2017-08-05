### docker-nes

```
xhost +
```

```
docker run -it --device /dev/snd -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY --device /dev/dri jess/nes /games/supermariobros.rom
```
