### Windows
eval "$(docker-machine env default)"
docker pull redis:3.0.7
docker build -t compose_flask .
docker-compose up -d

### Other commands
docker-compose ps
docker-compose run -d web env

If build parameter is used in docker-compose.yml it is not neccesary to build compose_flask image
