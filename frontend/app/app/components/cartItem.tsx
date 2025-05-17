import useCartStore from "@/store/useCartStore"; //se descomenta para acceder a addproduct y remove product
import type { ProductWithAmount } from "@/store/useCartStore";
import { formatCurrency } from "@/lib/utils";
import { Button } from "./ui/button"; //para agregar o dismunuir productos
import { MinusCircleIcon, PlusCircleIcon, ShoppingCart } from "lucide-react"; //iconos que usa Manu y shoppingcart

interface CartItemProps{
    product: ProductWithAmount;
}

const CartItem: React.FC<CartItemProps> = ({ product }) => { //Pieza reutilizable de productos del carrito, usará las propos de un cartitem
    const { addProduct, removeProduct } = useCartStore(); //traigo dos acciones del carrito, pero no todo

    return (
        <div
            className="bg-white rounded-lg shadow-md p-4 mb-0 flex items-start" //Es un contenedor flex
        >
            <div className="size-24 shrink-0 overflow-hidden rounded-md border border-gray-200 mr-4">
                <img alt={product.name} src={product.imageUrl} className="size-full object-cover" />
            </div>
            <div className="flex-grow flex-col"//para ocupar todo el espacio del contenedor
            >
                <p className="font-semibold text-gray-800 text-center mb-1">{product.name}</p>
                <p className="text-sm text-gray-600 mt-1">Precio: {formatCurrency(product.price)}</p>
                <p className="text-sm font-medium text-gray-700 mt-1">Subtotal: {formatCurrency(product.price * product.amount)}</p>
                <div className="flex items-center justify-center mt-2"> 
                    <Button 
                        size="icon" // Para que el botón sea pequeño y cuadrado para el icono
                            onClick={() => removeProduct(product)} // Llama a la acción del store para remover productos
                            className="h-7 w-7"
                    >
                        <MinusCircleIcon className="size-4" />
                    </Button>

                    <span className="mx-3 font-medium text-gray-800"> 
                        {product.amount}
                    </span>

                    <Button 
                        size="icon"
                        onClick={() => addProduct(product)} // Llama a la acción del store
                        className="h-7 w-7"
                    >
                        <PlusCircleIcon className="size-4" />
                    </Button>
                </div>
            </div>
        </div>
    );
};

export default CartItem;