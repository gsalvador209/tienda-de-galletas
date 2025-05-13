import { ShoppingCart } from "lucide-react";
import { Sheet, SheetContent, SheetHeader, SheetTrigger } from "./ui/sheet";
import Logo from "./logo";

const CartSheet = () => {
  return (
    <Sheet>
      <SheetTrigger>
        <ShoppingCart className="size-5" />
      </SheetTrigger>
      <SheetContent>
        <SheetHeader className="font-bold text-lg">
          <Logo />
        </SheetHeader>
        Carrito
      </SheetContent>
    </Sheet>
  );
};

export default CartSheet;
