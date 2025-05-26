# Usamos la última imagen oficial de Nginx
FROM nginx:latest 

RUN ls -la /etc/nginx/conf.d/ 
RUN rm -f /etc/nginx/conf.d/default.conf 
COPY nginx.conf /etc/nginx/conf.d/nginx.conf 

EXPOSE 80 

CMD ["nginx", "-g", "daemon off;"] 