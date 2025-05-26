import { UserIcon } from "lucide-react";
import { SheetContent, SheetHeader, SheetTrigger } from "./ui/sheet";
import Logo from "./logo";
import LoginForm from "./login-form";
import RegisterForm from "./register-form";
import { useState } from "react";

const LoginSheet = () => {
  const [tab, setTab] = useState<"register" | "login">("login");
  return (
    <>
      <SheetTrigger>
        <UserIcon className="size-5" />
      </SheetTrigger>
      <SheetContent>
        <SheetHeader className="font-bold text-lg">
          <Logo />
        </SheetHeader>
        {tab === "login" ? (
          <LoginForm onRegisterClick={() => setTab("register")} />
        ) : (
          <RegisterForm onLoginClick={() => setTab("login")} />
        )}
      </SheetContent>
    </>
  );
};

export default LoginSheet;
