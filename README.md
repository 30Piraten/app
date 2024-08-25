# app
GO REST

#### Running Swagger-ui via Docker
- "docker run -p 4545:8080 -e SWAGGER_JSON=/src/openapi.json -v ./app:/src swaggerapi/swagger-ui"

- Where /src => mnt
- ./rest_api/app => path to swagger json file