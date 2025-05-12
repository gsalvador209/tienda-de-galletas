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
];

const NavBar = () => {
  return (
    <div className="flex gap-x-15 bg-slate-100 w-full h-16 items-center">
      GalletasLogo
      <div className="flex gap-x-10">
        {routes.map((route) => (
          <p>{route.name}</p>
        ))}
      </div>
    </div>
  );
};

export default NavBar;
