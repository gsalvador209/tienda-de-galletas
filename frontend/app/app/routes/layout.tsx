import ImagesBanner from "@/components/images-banner";
import NavBar from "@/components/nav-bar";
import { Outlet } from "react-router";

export default function Home() {
  return (
    <main className="flex justify-center">
      <div className="">
        <NavBar />
        <ImagesBanner />
        <Outlet />
      </div>
    </main>
  );
}
