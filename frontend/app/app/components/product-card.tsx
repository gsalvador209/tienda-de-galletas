import type { Product } from "@/lib/types";
import { formatCurrency } from "@/lib/utils";

interface ProductCardProps {
  product: Product;
}

const ProductCard = ({ product }: ProductCardProps) => {
  return (
    <div className="">
      <a key={product.id} href={product.id} className="group">
        <img
          alt={product.name}
          src={product.imageUrl}
          className="aspect-square w-[200px] rounded-lg bg-gray-200 object-cover group-hover:opacity-75 xl:aspect-7/8"
        />
        <h3 className="mt-4">{product.name}</h3>
        <p className="mt-1 font-medium text-gray-900">
          {formatCurrency(product.price)}
        </p>
      </a>
    </div>
  );
};

export default ProductCard;
