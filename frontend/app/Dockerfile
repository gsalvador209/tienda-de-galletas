# Stage 1 — build
FROM node:20 AS builder
WORKDIR /app

# 1) Copy only package files first (cache npm install)
COPY package*.json ./
# 2) Copy your TS & Vite config
COPY tsconfig.json vite.config.ts react-router.config.ts ./
# 3) Copy the rest of your source
COPY . .

# 4) Install & build
RUN npm install
RUN npm run build

# Stage 2 — runtime
FROM node:20-slim
WORKDIR /app

# 5) Grab the compiled output + node_modules
COPY --from=builder /app /app

# 6) Expose & start
EXPOSE 3000
CMD ["npm", "start"]
