import Autoplay from "embla-carousel-autoplay";
import { Carousel, CarouselContent, CarouselItem } from "./ui/carousel";

const ImagesBanner = () => {
  return (
    <Carousel
      opts={{
        loop: true,
        active: true,
        duration: 20,
      }}
      plugins={[
        Autoplay({
          delay: 5000,
        }),
      ]}
      className="flex items-center justify-center w-full p-1"
    >
      <CarouselContent>
        <CarouselItem>
          <div className="flex justify-center">
            <img src="/banner1.png" className="w-[1400px] object-fill" />
          </div>
        </CarouselItem>
        <CarouselItem>
          <div className="flex justify-center">
            <img src="/banner2.png" className="w-[1400px] object-fill" />
          </div>
        </CarouselItem>
      </CarouselContent>
    </Carousel>
  );
};

export default ImagesBanner;
