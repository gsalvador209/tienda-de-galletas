// frontend/app/app/routes/home/home.tsx

import type { Route } from "./+types/home";
// ↓ Eliminado: import { testProduct, testProductList } from "@/lib/testdata";
import ProductGallery from "@/components/product-gallery";
import type { Product } from "@/lib/types";
// ↓ Agregado: Hooks de React para manejar estado y efectos
import { useEffect, useState } from "react";

export function meta({}: Route.MetaArgs) {
  return [{ title: "Home" }];
}

export default function Home() {
  // 1) Estado para productos, carga y posible error
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // 2) useEffect para ejecutar la petición al montar el componente
  useEffect(() => {
    // ruta relativa: el proxy Nginx la reenviará a http://backend:8000/products
    fetch("/products")
      .then(res => {
        // 2.a) Verificar que la respuesta sea exitosa (status 2xx)
        if (!res.ok) {
          throw new Error(`Error HTTP ${res.status}`);
        }
        return res.json();
      })
      .then((data: Product[]) => {
        // 2.b) Guardar los datos recibidos en el estado
        setProducts(data);
      })
      .catch(err => {
        // 2.c) Capturar y mostrar cualquier error
        console.error("Error al cargar productos:", err);
        setError("No se pudieron cargar los productos");
      })
      .finally(() => {
        // 2.d) Indicar que terminó la fase de carga
        setLoading(false);
      });
  }, []); // arreglo vacío → solo al montarse

  // 3) Mostrar indicador de carga
  if (loading) {
    return <div>Cargando productos…</div>;
  }
  // 4) Mostrar mensaje de error si falló la petición
  if (error) {
    return <div className="text-red-500">{error}</div>;
  }

  // 5) Renderizar la galería con los productos obtenidos
  return (
    <main>
      <ProductGallery products={products} />
    </main>
  );
}
