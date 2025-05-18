import { Sheet } from "./ui/sheet";
import { useContext } from "react";
import { UserContext } from "@/providers/user-provider";
import LoginSheet from "./login-sheet";
import UserSheet from "./user-sheet";

const ProfileSheet = () => {
  const { user } = useContext(UserContext)!;
  return <Sheet>{user ? <UserSheet user={user} /> : <LoginSheet />}</Sheet>;
};

export default ProfileSheet;
