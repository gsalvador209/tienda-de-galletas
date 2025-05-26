import { Sheet, SheetContent, SheetHeader, SheetTrigger, SheetClose} from "./ui/sheet";
import Logo from "./logo";
import CartSheetTrigger from "./cart-sheet-trigger";
import useCartStore from "@/store/useCartStore";
import { formatCurrency } from "@/lib/utils";
import CartItem from "./cartItem";
import { Link } from "react-router-dom";

const CartSheet = () => { //Componente funcional, pieza reutilizable de interfaz de usuario (deberá estar en las demás secciones)
  const cart = useCartStore()
  
  return (
    <Sheet>
      <SheetTrigger> 
         <CartSheetTrigger />
      </SheetTrigger>
      <SheetContent className="flex flex-col h-full">
        <SheetHeader className="font-bold text-lg pb-4 border-b">
          <Logo />
          <p className="font-bold text-center text-gray10000 mb-1">En tu carrito</p>
        </SheetHeader>
        <div className="flex-grow overflow-y-auto py-4">
          {cart.products.map((product) => (
              <div key={product.id} className="px-4 mb-3">
                <CartItem
                  product={product} 
                />
              </div>
            ))
          }
        </div>
        {cart.products.length > 0 && (
          <div className="border-t mt-auto p-4"> {/* mt-auto lo empuja hacia abajo, border-t para una línea, p-4 para padding */}
            <div className="flex justify-between font-semibold text-lg mb-4">
              <span>Total:</span>
              <span>{formatCurrency(cart.totalPrice())}</span>
            </div>
              <SheetClose asChild> 
                <Link 
                  to="/checkout" 
                  // Aplica los estilos del botón DIRECTAMENTE al Link
                  className="block w-full bg-rose-300 hover:bg-pink-300 text-white py-2 rounded-lg text-center" 
                > 
                  Checkout
                </Link>
               </SheetClose>
          </div>
        )}
      </SheetContent>
    </Sheet>
  );
};

export default CartSheet;
