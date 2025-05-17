import { Sheet, SheetContent, SheetHeader, SheetTrigger } from "./ui/sheet";
import Logo from "./logo";
import CartSheetTrigger from "./cart-sheet-trigger";
import useCartStore from "@/store/useCartStore";
import { formatCurrency } from "@/lib/utils";
import CartItem from "./cartItem";

const CartSheet = () => { //Componente funcional, pieza reutilizable de interfaz de usuario (deberá estar en las demás secciones)
  const cart = useCartStore()
  
  return (
    <Sheet>
      <SheetTrigger> 
         <CartSheetTrigger />
      </SheetTrigger>
      <SheetContent>
        <SheetHeader className="font-bold text-lg">
          <Logo />
        </SheetHeader>
        {cart.products.map((product) => (
          <CartItem
                key={product.id} 
                product={product} 
              />

        ))
      }
      </SheetContent>
    </Sheet>
  );
};

export default CartSheet;
