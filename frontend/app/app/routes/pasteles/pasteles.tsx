import ProductGallery from "@/components/product-gallery";
import { testProductList } from "@/lib/testdata";

const PastelesPage = () => {
  return (
    <main>
      <ProductGallery products={testProductList} />
    </main>
  );
};
export default PastelesPage;
