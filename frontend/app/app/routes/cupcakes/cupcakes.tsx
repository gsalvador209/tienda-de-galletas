import ProductGallery from "@/components/product-gallery";
import { testProductList } from "@/lib/testdata";

const CupcakesPage = () => {
  return (
    <main>
      <ProductGallery products={testProductList} />
    </main>
  );
};
export default CupcakesPage;
