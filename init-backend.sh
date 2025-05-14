#!/usr/bin/env bash
set -e

# Variables
BACKEND_DIR=services/backend

# Crear carpetas principales
mkdir -p $BACKEND_DIR/{config,products/auth,models,tests,migrations,seeds}

# Dentro de products y auth
mkdir -p $BACKEND_DIR/products/{routes,tests}
mkdir -p $BACKEND_DIR/auth/{routes,tests}

# Archivos base
touch $BACKEND_DIR/{app.py,requirements.txt,.env.sample,Dockerfile}
touch $BACKEND_DIR/config/{database.py,auth0.py}
touch $BACKEND_DIR/models/{__init__.py,product.py,user.py}
touch $BACKEND_DIR/products/routes/__init__.py
touch $BACKEND_DIR/auth/routes/__init__.py
touch $BACKEND_DIR/migrations/env.py
echo "# seed SQL scripts" > $BACKEND_DIR/seeds/README.md
