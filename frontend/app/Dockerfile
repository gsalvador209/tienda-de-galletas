# Dockerfile
# Etapa 1: Construcción
FROM node:20 AS builder

WORKDIR /app

# Copiamos los archivos necesarios
COPY ./frontend/app/package*.json ./
COPY ./frontend/app/tsconfig.json ./
COPY ./frontend/app/vite.config.ts ./
COPY ./frontend/app/react-router.config.ts ./
COPY ./frontend/app ./

# Instalamos dependencias y construimos
RUN npm install
RUN npm run build

# Etapa 2: Producción
FROM node:20-slim

WORKDIR /app

# Instalamos solo lo necesario para servir
COPY --from=builder /app /app

EXPOSE 3000

CMD ["npm", "start"] 
#Explicar cada linea de este archivo 
