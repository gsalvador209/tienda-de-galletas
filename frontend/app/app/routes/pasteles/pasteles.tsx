// frontend/app/app/routes/pasteles.tsx
// Basado en tu versión original :contentReference[oaicite:2]{index=2}

import ProductGallery from "@/components/product-gallery";
// import { testProductList } from "@/lib/testdata";   // Eliminado: datos de prueba
import type { Product } from "@/lib/types";          // Agregado: definición de producto
import { useEffect, useState } from "react";         // Agregados: hooks de React

export default function PastelesPage() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const API = "tienda-de-galletas-production.up.railway.app"

  useEffect(() => {


    fetch(`${API}/products`)
      .then(res => {
        if (!res.ok) throw new Error(`Error HTTP ${res.status}`);
        return res.json();
      })
      .then((all: Product[]) => {
        // Filtramos por type === "pastel"
        const pasteles = all.filter(p => p.type === "pastel");
        setProducts(pasteles);
      })
      .catch(err => {
        console.error("Error cargando pasteles:", err);
        setError("No fue posible cargar los pasteles");
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Cargando pasteles…</div>;
  if (error)   return <div className="text-red-500">{error}</div>;

  return (
    <main>
      <ProductGallery products={products} />
    </main>
  );
}
