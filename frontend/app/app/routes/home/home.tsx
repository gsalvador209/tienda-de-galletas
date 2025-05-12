import { Button } from "@/components/ui/button";
import type { Route } from "./+types/home";

export function meta({}: Route.MetaArgs) {
  return [{ title: "Home" }];
}

export default function Home() {
  return (
    <main>
      <Button>Click</Button>
    </main>
  );
}
