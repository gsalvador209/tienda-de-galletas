import { UserIcon } from "lucide-react";
import { Sheet, SheetContent, SheetHeader, SheetTrigger } from "./ui/sheet";
import LoginForm from "./login-form";
import Logo from "./logo";

const LoginSheet = () => {
  return (
    <Sheet>
      <SheetTrigger>
        <UserIcon className="size-5" />
      </SheetTrigger>
      <SheetContent>
        <SheetHeader className="font-bold text-lg">
          <Logo />
        </SheetHeader>
        <LoginForm />
      </SheetContent>
    </Sheet>
  );
};

export default LoginSheet;
