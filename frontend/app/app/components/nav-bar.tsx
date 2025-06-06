import Logo from "./logo";
import { Link, NavLink } from "react-router";
import ProfileSheet from "./profile-sheet";
import CartSheet from "./cart-sheet";

interface Route {
  name: string;
  path: string;
}

const routes: Route[] = [
  {
    name: "Home",
    path: "/",
  },
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
];

const NavBar = () => {
  return (
    <div className="flex gap-x-1 w-full h-16 items-center justify-between px-10 shadow-sm sticky top-0 z-50 bg-background">
      <div className="flex gap-x-10 items-center">
        <Link to="/">
          <Logo />
        </Link>
        {routes.map((route, index) => (
          <NavLink
            key={index}
            to={route.path}
            className={({ isActive, isPending, isTransitioning }) =>
              [isActive ? "" : "opacity-50"].join("")
            }
          >
            <span className="font-chewy text-lg">{route.name}</span>
          </NavLink>
        ))}
      </div>
      <div className="flex gap-x-5">
        <CartSheet />
        <ProfileSheet />
      </div>
    </div>
  );
};

export default NavBar;
