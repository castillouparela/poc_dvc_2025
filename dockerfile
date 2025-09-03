# Usar la imagen oficial de Python como base
FROM python:3.12-slim

# Instalar manejador de paquetes uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copiar la aplicación en el contenedor
COPY . /app

# Instalar los paquetes necesarios
WORKDIR /app
RUN uv sync --frozen --no-cache

# # Copiar el resto del código de la aplicación en el contenedor
# COPY . .

# Exponer el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación FastAPI
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]

# Ejecutar en cmd mediante el comando -> docker build -t demo_dvc_2025 .
# Ejecutar en cmd mediante el comando -> docker run -p 8000:8000 -d demo_dvc_2025