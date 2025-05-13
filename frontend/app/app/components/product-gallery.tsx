import type { Product } from "@/lib/types";
import ProductCard from "./product-card";

interface ProductGalleryProps {
  products: Product[];
}

const ProductGallery = ({ products }: ProductGalleryProps) => {
  return (
    <div className="py-10 grid grid-cols-1 gap-x-5 gap-y-10 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4 place-items-center">
      {products.map((product, i) => (
        <ProductCard key={i} product={product} />
      ))}
    </div>
  );
};

export default ProductGallery;
