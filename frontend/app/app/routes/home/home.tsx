import type { Route } from "./+types/home";
import ProductGallery from "@/components/product-gallery";
import { testProduct, testProductList } from "@/lib/testdata";
import type { Product } from "@/lib/types";

export function meta({}: Route.MetaArgs) {
  return [{ title: "Home" }];
}

export default function Home() {
  return (
    <main>
      <ProductGallery products={testProductList} />
    </main>
  );
}
