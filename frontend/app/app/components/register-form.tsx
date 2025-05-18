import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Form, FormField, FormItem, FormLabel, FormMessage } from "./ui/form";
import { z } from "zod";
import { Input } from "./ui/input";
import { Label } from "./ui/label";
import { Button } from "./ui/button";
import { useContext, useState } from "react";
import { UserContext } from "@/providers/user-provider";
import { CircleAlertIcon } from "lucide-react";

interface RegisterFormProps {
  onLoginClick: () => void;
}

const formSchema = z
  .object({
    name: z.string().min(1, { message: "El nombre es requerido" }),
    email: z
      .string()
      .min(1, {
        message: "Ingrese un correo electrónico válido",
      })
      .email("Ingrese un correo electrónico válido"),
    password: z.string().min(1, {
      message: "Ingrese su contraseña",
    }),
    confirmPassword: z.string(),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: "Las constraseñas no coinciden",
    path: ["confirmPassword"],
  });

const RegisterForm = ({ onLoginClick }: RegisterFormProps) => {
  const { setUser } = useContext(UserContext)!;
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      name: "",
      email: "",
      password: "",
      confirmPassword: "",
    },
  });

  const onSubmit = async (values: z.infer<typeof formSchema>) => {
    try {
      setIsLoading(true);
      setError(null);
      const response = await fetch(
        `${import.meta.env.VITE_BACKEND_BASE_URL}/auth/register`,
        {
          method: "POST",
          body: JSON.stringify(values),
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      if (response.status == 500) {
        setError("Error del servidor");
      }

      const jsonResponse = await response.json();
      const { id, name, email } = jsonResponse;
      setUser({ id, name, email });
      location.reload();
    } catch {
    } finally {
      setIsLoading(false);
    }
  };
  return (
    <div className="p-4">
      <span className="text-xl font-chewy">Registrate</span>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)}>
          <FormField
            control={form.control}
            name="name"
            render={({ field }) => (
              <FormItem>
                <FormLabel className="mt-5">
                  <Label className="font-chewy">Nombre</Label>
                </FormLabel>
                <Input placeholder="John Doe" {...field} disabled={isLoading} />
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="email"
            render={({ field }) => (
              <FormItem>
                <FormLabel className="mt-5">
                  <Label className="font-chewy">Correo electrónico</Label>
                </FormLabel>
                <Input
                  placeholder="correo@mail.com"
                  {...field}
                  disabled={isLoading}
                />
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="password"
            render={({ field }) => (
              <FormItem>
                <FormLabel className="mt-5">
                  <Label className="font-chewy">Contraseña</Label>
                </FormLabel>
                <Input
                  placeholder="•••••••••"
                  {...field}
                  type="password"
                  disabled={isLoading}
                />
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="confirmPassword"
            render={({ field }) => (
              <FormItem>
                <FormLabel className="mt-5">
                  <Label className="font-chewy">Confirmar contraseña</Label>
                </FormLabel>
                <Input
                  placeholder="•••••••••"
                  {...field}
                  type="password"
                  disabled={isLoading}
                />
                <FormMessage />
              </FormItem>
            )}
          />

          {error && (
            <div className="w-full bg-destructive/20 p-4 mt-4 text-destructive rounded-md flex justify-start items-center gap-x-4">
              <CircleAlertIcon className="size-4" />
              {error}
            </div>
          )}
          <Button
            type="submit"
            className="w-full mt-10 font-chewy"
            disabled={isLoading}
          >
            Ingresar
          </Button>

          <div className="w-full flex justify-center mt-4">
            <Button
              type="button"
              variant="link"
              className="text-black"
              onClick={onLoginClick}
            >
              Iniciar Sesión
            </Button>
          </div>
        </form>
      </Form>
    </div>
  );
};

export default RegisterForm;
