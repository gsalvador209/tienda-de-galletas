import { UserContext, type User } from "@/providers/user-provider";
import Logo from "./logo";
import { SheetContent, SheetHeader, SheetTrigger } from "./ui/sheet";
import { Button } from "./ui/button";
import { useContext } from "react";

interface UserSheetProps {
  user: User;
}

const UserSheet = ({ user }: UserSheetProps) => {
  const { setUser } = useContext(UserContext)!;
  return (
    <>
      <SheetTrigger>
        <div className="font-chewy">Hola, {user.name.split(" ")[0]}</div>
      </SheetTrigger>
      <SheetContent>
        <SheetHeader className="font-bold text-lg">
          <Logo />
        </SheetHeader>
        <div className="p-4 flex flex-col gap-y-5">
          <h1 className="font-chewy text-xl">{user.name}</h1>
          <Button
            className="w-full"
            variant="destructive"
            onClick={() => setUser(null)}
          >
            Cerrar sesión
          </Button>
        </div>
      </SheetContent>
    </>
  );
};

export default UserSheet;
