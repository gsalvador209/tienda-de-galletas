import NavBar from "~/components/nav-bar";
import React from "react";
import { Outlet } from "react-router";

export default function Home() {
  return (
    <main>
      <NavBar />
      <Outlet />
    </main>
  );
}
