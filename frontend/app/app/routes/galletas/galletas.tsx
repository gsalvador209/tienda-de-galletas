import ProductGallery from "@/components/product-gallery";
import { testProductList } from "@/lib/testdata";

const GalletasPage = () => {
  return (
    <main>
      <ProductGallery products={testProductList} />
    </main>
  );
};
export default GalletasPage;
