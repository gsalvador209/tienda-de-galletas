const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Bienvenido a la Tienda de Galletas');
});

app.listen(port, () => {
  console.log(`Servidor corriendo en el puerto ${port}`);
});
