// frontend/app/app/routes/cupcakes.tsx
// Basado en tu versión original :contentReference[oaicite:0]{index=0}

import ProductGallery from "@/components/product-gallery";
// import { testProductList } from "@/lib/testdata";   // Eliminado: datos de prueba
import type { Product } from "@/lib/types";          // Agregado: definición de producto
import { useEffect, useState } from "react";         // Agregados: hooks de React

export default function CupcakesPage() {
  // 1) Estado para la lista filtrada, indicador de carga y mensaje de error
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const API = "tienda-de-galletas-production.up.railway.app"


  // 2) Al montar, solicitamos todos los productos y luego filtramos por type === "cupcake"
  useEffect(() => {
    fetch(`${API}/products`)
      .then(res => {
        if (!res.ok) throw new Error(`Error HTTP ${res.status}`);
        return res.json();
      })
      .then((all: Product[]) => {
        const cupcakes = all.filter(p => p.type === "cupcake");
        setProducts(cupcakes);
      })
      .catch(err => {
        console.error("Error cargando cupcakes:", err);
        setError("No fue posible cargar los cupcakes");
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  // 3) Renderizado condicional según el estado
  if (loading) return <div>Cargando cupcakes…</div>;
  if (error)   return <div className="text-red-500">{error}</div>;

  // 4) Pasamos los cupcakes filtrados al componente
  return (
    <main>
      <ProductGallery products={products} />
    </main>
  );
}
