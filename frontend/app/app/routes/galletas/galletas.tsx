// frontend/app/app/routes/galletas.tsx
// Basado en tu versión original :contentReference[oaicite:1]{index=1}

import ProductGallery from "@/components/product-gallery";
// import { testProductList } from "@/lib/testdata";   // Eliminado: datos de prueba
import type { Product } from "@/lib/types";          // Agregado: definición de producto
import { useEffect, useState } from "react";         // Agregados: hooks de React

export default function GalletasPage() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const API = "tienda-de-galletas-production.up.railway.app"

  useEffect(() => {
    fetch(`${API}/products/`)
      .then(res => {
        if (!res.ok) throw new Error(`Error HTTP ${res.status}`);
        return res.json();
      })
      .then((all: Product[]) => {
        // Filtramos por type === "galleta"
        const galletas = all.filter(p => p.type === "galleta");
        setProducts(galletas);
      })
      .catch(err => {
        console.error("Error cargando galletas:", err);
        setError("No fue posible cargar las galletas");
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Cargando galletas…</div>;
  if (error)   return <div className="text-red-500">{error}</div>;

  return (
    <main>
      <ProductGallery products={products} />
    </main>
  );
}
