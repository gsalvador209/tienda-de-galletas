# Diagrama Entidad-Relación (ER)

Este diagrama representa la estructura de la base de datos para el sistema de tienda de galletas.

## Entidades

### `users`
Contiene la información de los usuarios registrados.

- `id`: Identificador único del usuario (PK).
- `auth0_id`: ID de autenticación externa (e.g., Auth0).
- `email`: Correo electrónico del usuario.
- `name`: Nombre del usuario.
- `role`: Rol del usuario (cliente, administrador).
- `created_at` / `updated_at`: Timestamps de auditoría.

### `products`
Almacena la información de los productos disponibles.

- `id`: Identificador único del producto (PK).
- `name`: Nombre del producto.
- `description`: Descripción del producto.
- `price`: Precio unitario.
- `stock`: Cantidad disponible.
- `created_at` / `updated_at`: Timestamps.

### `orders`
Representa los pedidos realizados por los usuarios.

- `id`: Identificador del pedido (PK).
- `user_id`: FK referenciando al usuario que hizo el pedido.
- `status`: Estado del pedido (pendiente, enviado, completado).
- `total`: Total del pedido.
- `direction`: Dirección de entrega.
- `created_at` / `updated_at`: Timestamps.

### `order_items`
Contiene los detalles de cada producto en un pedido.

- `id`: Identificador único del item (PK).
- `order_id`: FK referenciando el pedido.
- `product_id`: FK referenciando el producto.
- `quantity`: Cantidad de ese producto.
- `price`: Precio unitario al momento del pedido.

## Relaciones

- Un `user` puede tener muchos `orders`.
- Un `order` puede tener muchos `order_items`.
- Cada `order_item` pertenece a un `product` y un `order`.
