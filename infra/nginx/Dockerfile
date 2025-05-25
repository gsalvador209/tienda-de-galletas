
# Ruta: infra/nginx/Dockerfile

FROM nginx:latest

#Elimina la configuración default de Nginx
RUN rm /etc/nginx/conf.d/default.conf

#Copia lo que programé
COPY nginx.conf /etc/nginx/conf.de

#Expone el puerto 80 que será mapeado en docker-compose
EXPOSE 80