<p align="center">
  <img src="https://img.shields.io/badge/Proyecto-Tienda%20de%20Galletas-blue?style=for-the-badge" alt="Proyecto Tienda de Galletas">
  <img src="https://img.shields.io/badge/Stack-Python%20%7C%20Flask%20%7C%20React%20%7C%20Docker-green?style=for-the-badge" alt="Tecnologías">
</p>

# 🍪 Tienda de Galletas

**Cookie-Cloud** es una **plataforma de e-commerce** que distribuye productos de repostería fina en tiempo real, aprovechando **microservicios** en contenedores Docker, un **backend en Flask**, y un **frontend en React**. Está diseñada para escalar, ofrecer alta disponibilidad y asegurar una experiencia de compra ágil y confiable.

---

## 🚀 Alcance del Proyecto

- **Objetivo general**  
  Construir una arquitectura distribuida que permita listar, gestionar y vender productos de galletas en línea, garantizando:
  - Escalabilidad horizontal con Docker & Docker Compose  
  - Seguridad en autenticación y autorización
  - Experiencia de usuario moderna y responsiva  

- **Alcances principales**  
  1. Gestión de catálogo de productos  
  2. Registro, login y perfiles de usuarios  
  3. Carrito de compras y proceso de pago  
  4. Persistencia confiable en MySQL  
  5. Orquestación completa con CI/CD para despliegue automático  

---
## 📷 Capturas
<p align="center">
  <img width="600" src="https://github.com/user-attachments/assets/06886c42-88e4-4834-9d3d-f5523132ccae" />
  <img width="150" src="https://github.com/user-attachments/assets/53c64a2a-2c4c-4bb4-8bed-dd8e67b66663" />
</p>
<img width="1397" height="668" alt="image" src="https://github.com/user-attachments/assets/c02d5296-ffa2-4663-a59f-5e9ea8505f81" />
<img width="1311" height="532" alt="image" src="https://github.com/user-attachments/assets/2b732242-0874-4519-93c3-63c557afc80f" />

---

## 🧩 Features destacadas

| Servicio / Módulo         | Descripción breve                                                                 |
|---------------------------|-----------------------------------------------------------------------------------|
| **Productos**             | CRUD de galletas: listar, crear, editar, eliminar. 🔄                            |
| **Auth & Usuarios**       | Registro y autenticación con Auth0 + perfil protegido. 🔒                         |
| **Carrito & Checkout**    | Añadir/quitar ítems y procesar pagos (simulado). 🛒                             |
| **Base de Datos**         | ER robusto en MySQL + migraciones con Alembic. 🗄️                                |
| **Orquestación Docker**   | 4 contenedores: frontend, backend, base de datos, nginx. 🐳                       |
| **Frontend React**        | Interfaz SPA con Axios + React Router + Jest para pruebas. ⚛️                     |
| **Despliegue & CI/CD**    | Pipeline en GitHub Actions + Render.com. 🤖                                       |


> Este proyecto demuestra aplicación de **Clean Architecture**, **DDD** y **principios SOLID**, además de un flujo de desarrollo colaborativo con **6 integrantes** y **12 casos de uso** distribuidos.

---

## 📂 Estructura del repositorio

```bash
tienda-de-galletas/
├── backend/                      # API en Flask
│   ├── services/
│   │   ├── products/             # Chava: endpoints y modelos de productos
│   │   └── auth/                 # Manuel: flujo Auth0 y JWT
│   ├── config/
│   │   ├── database.py
│   │   └── auth0.py
│   ├── migrations/               # Alembic
│   └── run.py
│
├── frontend/                     # App en React
│   ├── src/
│   │   ├── components/           # Dulce & Lalo: ProductList, Cart, Checkout…
│   │   ├── context/CartContext.js
│   │   └── api/
│   │       └── products.js
│   └── public/
│
├── database/                     # Scripts SQL
│   ├── schema.sql                # Mirna: esquema ER
│   └── seeds/                    # Datos de prueba
│
├── docker/                       # Orquestación
│   ├── frontend/Dockerfile
│   ├── backend/Dockerfile
│   ├── mysql/Dockerfile
│   ├── nginx/
│   │   ├── Dockerfile
│   │   └── nginx.conf
│   └── docker-compose.yml        # Ana Pau: toda la pila
│
├── docs/                         # Documentación
│   ├── arquitectura.md
│   ├── casos_de_uso.md           # 12 casos de uso (2 por integrante)
│   └── deployment.md
│
├── .gitignore
├── README.md                     # ← ¡Tú estás aquí!
└── package.json

```

👥 Equipo & Roles
Integrante	Rol / Responsabilidad
Chava	Backend Productos (Flask + MySQL)
Manuel	Backend Auth & Usuarios (Flask + Auth0)
Dulce	Frontend Productos (React)
Lalo	Frontend Carrito & Checkout (React)
Mirna	Diseño y migraciones de Base de Datos (MySQL)
Ana Pau	Orquestación Docker & Despliegue (Docker Compose + Render.com)

📈 Casos de Uso (Selección)
Listar productos

- Crear/Actualizar/Eliminar producto
- Registro de usuario
- Login + Perfil protegido
- Ver lista de productos
- Ver detalle de producto
- Añadir/Quitar ítems del carrito
- Procesar checkout
- Consultar productos/usuarios
- Registrar pedidos
- Levantar todo con docker-compose up
- Desplegar en Render.com con un solo push


📬 Conoce al equipo
¡Nos encantaría recibir tu feedback!
📧 Contacto: 
- **Chava** – [LinkedIn](https://www.linkedin.com/in/gsalvador209/)  
- **Manuel** – [LinkedIn]()  
- **Dulce** – [LinkedIn](https://www.linkedin.com/in/dulce-lopez-3233a7275/)  
- **Lalo** – [LinkedIn](https://www.linkedin.com/in/eddcervantesgarcia/)  
- **Mirna** – [LinkedIn](https://wwww.linkedin.com/in/MirnaMarquez)  
- **Ana Pau** – [LinkedIn]()  


🌐 Demo en producción: proximanete

<p align="center">Made with ❤️</p>
