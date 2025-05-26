# Usa una imagen base ligera con Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia archivos al contenedor
COPY ./services/backend/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la app
COPY . .

# Variables de entorno por defecto (puedes sobreescribir con .env)
ENV FLASK_APP=app.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_ENV=production

# Expone el puerto configurado
EXPOSE 5000

# Usa Gunicorn como servidor de producción
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:create_app()"]
