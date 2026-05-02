# Despliegue con Docker

Este proyecto puede levantarse con tres contenedores:

- `db`: PostgreSQL
- `backend`: API Spring Boot
- `frontend`: web estática servida con Nginx

## Requisitos

- Tener Docker Desktop instalado y arrancado.

## Arranque

Desde `/Users/marinamr/Documents/GitHub/orsy`:

```bash
docker compose up --build
```

## URLs

- Frontend: `http://localhost:8081/login.html`
- Backend: `http://localhost:8080`
- Base de datos PostgreSQL: `localhost:5432`

## Parada

```bash
docker compose down
```

Si además quieres borrar el volumen de PostgreSQL:

```bash
docker compose down -v
```

## Cómo funciona

- El frontend sigue apuntando a `http://localhost:8080`, así que no ha sido necesario cambiar su código.
- El backend se conecta a PostgreSQL usando el nombre del servicio `db` dentro de Docker.
- Los datos de PostgreSQL se guardan en el volumen `postgres_data`.
