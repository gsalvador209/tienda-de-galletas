FROM node:23-alpine AS build
WORKDIR /app

COPY . /app/

RUN npm install npm@latest -g
RUN npm update
RUN npm install --silent
RUN npm run build

CMD ["npm", "run", "start"]