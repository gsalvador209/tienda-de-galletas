import { ShoppingCart } from "lucide-react";
import { Sheet, SheetContent, SheetHeader, SheetTrigger } from "./ui/sheet";
//import useCartStore from "@/store/useCartStore";
import type { ProductWithAmount } from "@/store/useCartStore";
import { formatCurrency } from "@/lib/utils";

interface CartItemProps{
    product: ProductWithAmount;
}

const CartItem: React.FC<CartItemProps> = ({ product }) => { //Pieza reutilizable de productos del carrito, usará las propos de un cartitem
    //const cart = useCartStore() No traeré todo el carrito, solo lo de la interface 

    return (
        <div
            className="bg-white rounded-lg shadow-md p-4 mb-0 flex items-start" //Es un contenedor flex
        >
            <div className="size-24 shrink-0 overflow-hidden rounded-md border border-gray-200">
                <img alt={product.name} src={product.imageUrl} className="size-full object-cover" />
            </div>
            <div className="flex-grow flex-col"//para ocupar todo el espacio del contenedor
            >
                <p className="font-semibold text-gray-800 text-center mb-1">{product.name}</p>
            </div>
        </div>
    );
};

export default CartItem;