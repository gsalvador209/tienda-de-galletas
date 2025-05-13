import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Form, FormField, FormItem, FormLabel, FormMessage } from "./ui/form";
import { z } from "zod";
import { Input } from "./ui/input";
import { Label } from "./ui/label";
import { Button } from "./ui/button";

const formSchema = z.object({
  email: z.string().min(1, {
    message: "Ingrese un correo electrónico válido",
  }),
  password: z.string().min(1, {
    message: "Ingrese su contraseña",
  }),
});

const LoginForm = () => {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      email: "",
      password: "",
    },
  });

  const onSubmit = (values: z.infer<typeof formSchema>) => {
    console.log(values);
    //enviar a backend
  };
  return (
    <div className="p-4">
      <span className="text-xl font-chewy">Inicia Sesión</span>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)}>
          <FormField
            control={form.control}
            name="email"
            render={({ field }) => (
              <FormItem>
                <FormLabel className="mt-5">
                  <Label className="font-chewy">Correo electrónico</Label>
                </FormLabel>
                <Input placeholder="correo@mail.com" {...field} />
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
                <Input placeholder="•••••••••" {...field} type="password" />
                <FormMessage />
              </FormItem>
            )}
          />
          <Button type="submit" className="w-full mt-10 font-chewy">
            Ingresar
          </Button>
        </form>
      </Form>
    </div>
  );
};

export default LoginForm;
