import { cn } from "@/lib/utils";
import useCartStore from "@/store/useCartStore";
import { ShoppingCart } from "lucide-react";

const CartSheetTrigger = () => {
  const cart = useCartStore();
  return (
    <div className="relative">
      <span
        className={cn(
          cart.products.length > 0 ? "absolute" : "hidden",
          "left-4 bottom-2 text-xs bg-destructive text-white p-1 rounded-full"
        )}
      >
        {cart.products.length}
      </span>
      <ShoppingCart className="size-5" />
    </div>
  );
};

export default CartSheetTrigger;
