import { ShoppingCart, UserIcon } from "lucide-react";
import Logo from "./logo";

interface Route {
  name: string;
  path: string;
}

const routes: Route[] = [
  {
    name: "Galletas",
    path: "/galletas",
  },
  {
    name: "Pasteles",
    path: "/pasteles",
  },
  {
    name: "Cupcakes",
    path: "/cupcakes",
  },
  {
    name: "Contacto",
    path: "/contacto",
  },
];

const NavBar = () => {
  return (
    <div className="flex gap-x-1 w-full h-16 items-center justify-between px-10 shadow-sm">
      <div className="flex gap-x-10 items-center">
        <Logo />
        {routes.map((route) => (
          <p>{route.name}</p>
        ))}
      </div>
      <div className="flex gap-x-5">
        <ShoppingCart className="size-5" />
        <UserIcon className="size-5" />
      </div>
    </div>
  );
};

export default NavBar;
