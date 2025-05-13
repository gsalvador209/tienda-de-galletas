import type { Product } from "@/lib/types";
import { formatCurrency } from "@/lib/utils";

interface ProductCardProps {
  product: Product;
}

const ProductCard = ({ product }: ProductCardProps) => {
  return (
    <div className="w-[50%] md:w-[80%] xl:w-[70%]">
      <a
        key={product.id}
        href={product.id}
        className="group flex flex-col items-center"
      >
        <img
          alt={product.name}
          src={product.imageUrl}
          className="aspect-square w-full rounded-lg bg-gray-200 object-cover group-hover:opacity-75 xl:aspect-7/8"
        />
        <div className="w-full">
          <h3 className="mt-4 font-chewy">{product.name}</h3>
          <p className="mt-1 text-sm font-chewy text-gray-500">
            {formatCurrency(product.price)}
          </p>
        </div>
      </a>
    </div>
  );
};

export default ProductCard;
