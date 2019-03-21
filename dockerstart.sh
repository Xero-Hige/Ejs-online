docker build . -t server-ejercicios
docker run -p 8000:8000 --env-file=config.env -v $(pwd):/server server-ejercicios