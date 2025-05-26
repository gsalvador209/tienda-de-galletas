export interface Product {
  id: string;
  name: string;
  description: string;
  price: number;
  type: "galleta" | "cupcake" | "pastel";
  image_url: string;
}
