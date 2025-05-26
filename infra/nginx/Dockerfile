# Usamos la última imagen oficial de Nginx
FROM nginx:latest

# 1) Quitamos la configuración por defecto
RUN rm /etc/nginx/conf.d/default.conf

# 2) Copiamos nuestro archivo de configuración personalizado
COPY nginx.conf /etc/nginx/conf.d/nginx.conf

# 3) Exponemos el puerto 80 para recibir tráfico HTTP
EXPOSE 80

# 4) Arrancamos Nginx en primer plano (sin daemonizar)
CMD ["nginx", "-g", "daemon off;"]
