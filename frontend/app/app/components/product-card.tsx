import type { Product } from "@/lib/types";
import { formatCurrency } from "@/lib/utils";
import { Button } from "./ui/button";
import useCartStore from "@/store/useCartStore";
import { MinusCircleIcon, PlusCircleIcon, ShoppingCart } from "lucide-react";

interface ProductCardProps {
  product: Product;
}

const ProductCard = ({ product }: ProductCardProps) => {
  const cart = useCartStore();
  const productInCart = cart.getProduct(product);
  return (
    <div className="w-[50%] md:w-[80%] xl:w-[70%]">
      <div key={product.id} className="group flex flex-col items-center">
        <div className="relative">
          <img
            alt={product.name}
            src={product.image_url}
            className="aspect-square w-full rounded-lg bg-gray-200 object-cover group-hover:opacity-75 xl:aspect-7/8"
          />
          <div className="hidden group-hover:block absolute top-[50%] left-[50%] transform -translate-x-1/2 -translate-y-1/2">
            <div className="flex items-center justify-center gap-x-4 bg-primary p-1 rounded-sm">
              <Button onClick={() => cart.removeProduct(product)}>
                <MinusCircleIcon />
              </Button>
              <span>
                {productInCart ? (
                  productInCart.amount
                ) : (
                  <ShoppingCart className="size-4" />
                )}
              </span>
              <Button onClick={() => cart.addProduct(product)}>
                <PlusCircleIcon />
              </Button>
            </div>
          </div>
        </div>
        <div className="w-full">
          <h3 className="mt-4 font-chewy">{product.name}</h3>
          <p className="mt-1 text-sm font-chewy text-gray-500">
            {formatCurrency(product.price)}
          </p>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;
