import {
  type RouteConfig,
  index,
  layout,
  route,
} from "@react-router/dev/routes";

export default [
  layout("./routes/layout.tsx", [
    index("routes/home/home.tsx"),
    route("galletas", "routes/galletas/galletas.tsx"),
    route("pasteles", "routes/pasteles/pasteles.tsx"),
    route("cupcakes", "routes/cupcakes/cupcakes.tsx"),
    route("contacto", "routes/contacto/contacto.tsx"),
  ]),
] satisfies RouteConfig;
