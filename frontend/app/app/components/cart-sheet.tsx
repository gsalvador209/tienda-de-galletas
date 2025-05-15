import { Sheet, SheetContent, SheetHeader, SheetTrigger } from "./ui/sheet";
import Logo from "./logo";
import CartSheetTrigger from "./cart-sheet-trigger";

const CartSheet = () => {
  return (
    <Sheet>
      <SheetTrigger>
        <CartSheetTrigger />
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
