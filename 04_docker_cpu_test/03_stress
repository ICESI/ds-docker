### Test de Stress

Ejecute el siguiente comando para desplegar un contenedor para un test de stress
```
docker run \
  -ti \
  --rm \
  --cpu-quota=50000 \
  --cpuset-cpus=0 \
  polinux/stress stress \
    --cpu 1 \
    --io 1 \
    --vm 1 \
    --vm-bytes 128M \
    --timeout 3600s \
    --verbose
```

La imagen polinux/stress tiene la aplicación de linux de nombre stress preinstalada. Consulte la documentación de cada
parametro empleado en el comando anterior.

### Referencias
* https://www.cyberciti.biz/faq/stress-test-linux-unix-server-with-stress-ng/
* https://docs.docker.com/config/containers/resource_constraints/
