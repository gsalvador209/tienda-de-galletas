# 1) Base: una imagen liviana de Python 3.11
FROM python:3.11-bullseye

# 2) Crea el directorio de trabajo
WORKDIR /app

# 3) Copia sólo lo necesario para instalar deps
COPY requirements.txt .

# 4) Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 4.5) Copia y da permisos de ejecucion a un script de espera
COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

# 5) Copia el resto del código al contenedor
COPY . .

# 6) Expone el puerto en el que el app escucha
EXPOSE 8000

# 7) Define la variable de entorno para que los logs salgan sin buffer
ENV PYTHONUNBUFFERED=1

# 8) Punto de entrada: 
#    1) Aplica migraciones con Alembic
#    2) Ejecuta el seed de datos
#    3) Arranca tu aplicación
CMD ["sh", "-c", "\
    /usr/local/bin/wait-for-it.sh mysql:3306 --timeout=30 --strict -- \
    alembic upgrade head && \
    python -m seeds.seed && \
    gunicorn --workers 4 --bind 0.0.0.0:8000 app:app\
"]
