export interface Product {
  id: string;
  name: string;
  description: string;
  price: number;
  type: "galleta" | "cupcake" | "pastel";
  imageUrl: string;
}
