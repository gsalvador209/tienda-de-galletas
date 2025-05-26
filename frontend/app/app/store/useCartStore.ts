import type { Product } from "@/lib/types";
import { create } from "zustand";

export interface ProductWithAmount extends Product {
  amount: number;
}

interface CartState {
  products: ProductWithAmount[];
  getProduct: (product: Product) => ProductWithAmount | undefined;
  addProduct: (product: Product) => void;
  removeProduct: (product: Product) => void;
  emptyCart: () => void;
  totalPrice: () => number;
}

const useCartStore = create<CartState>((set, get) => ({
  products: [],
  getProduct: (product) =>
    get().products.find((item) => item.id === product.id),
  addProduct: (product) => {
    const itemExists = get().products.find((item) => item.id === product.id);

    if (itemExists) {
      set((state) => ({
        products: state.products.map((item) =>
          item.id === product.id
            ? {
                ...item,
                amount: item.amount + 1,
              }
            : item
        ),
      }));
    } else {
      set((state) => ({
        products: [...state.products, { ...product, amount: 1 }],
      }));
    }
  },
  removeProduct: (product) => {
    const itemExists = get().products.find((item) => item.id === product.id);
    if (!itemExists) return;

    if (itemExists.amount === 1) {
      set((state) => ({
        products: state.products.filter((item) => item.id !== product.id),
      }));
    } else {
      set((state) => ({
        products: state.products.map((item) =>
          item.id === product.id ? { ...item, amount: item.amount - 1 } : item
        ),
      }));
    }
  },
  emptyCart: () => set((state) => ({ products: [] })),
  totalPrice: () =>
    get().products.reduce((sum, item) => sum + item.price * item.amount, 0),
}));

export default useCartStore;
