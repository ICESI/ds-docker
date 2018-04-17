# cmd is inherit from the parent if it is not specified

```
docker build -t base_container .
docker build -t dev_container .
docker run --rm dev_container
```
