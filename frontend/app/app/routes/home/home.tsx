import type { Route } from "./+types/home";
import ProductGallery from "@/components/product-gallery";
import { testProduct, testProductList } from "@/lib/testdata";
import type { Product } from "@/lib/types";

export function meta({}: Route.MetaArgs) {
  return [{ title: "Home" }];
}

export default function Home() {
  const testProducts: Product[] = Array(25).fill(testProduct);

  return (
    <main>
      <ProductGallery products={testProductList} />
    </main>
  );
}
