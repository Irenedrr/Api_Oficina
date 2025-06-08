# LibrosAPI
## API de FastAPI con SQLModel
API para la gestion de los datos de la app de un oficina virtual.

### Construir la imagen de Docker
En el directorio raíz de tu proyecto (donde se encuentra el archivo `Dockerfile`), ejecuta el siguiente comando para construir la imagen Docker:
```bash
docker build -t oficina_api .
```


### Ejecutar el contenedor Docker
Utilizando sqlite:
```bash
docker run -d -p 8000:8000 oficina_api
```
Utilizando otra bbdd:
```bash
docker run -d --name API_DB -e POSTGRES_USER=APIproduct -e POSTGRES_PASSWORD=APIpass -e POSTGRES_DB=API_DB -p 5432:5432 postgres

docker run -d -p 8000:8000 --name api_postgres -e DATABASE_URL="postgresql://APIproduct:APIpass@API_DB:5432/API_DB" productos_api

```