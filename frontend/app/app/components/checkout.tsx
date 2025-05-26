import useCartStore from "@/store/useCartStore";
import type { ProductWithAmount } from "@/store/useCartStore"; 
import { formatCurrency } from "@/lib/utils";
import { Button } from "./ui/button";
import { Input } from "./ui/input";
import { Label } from "./ui/label";
import React, { useState, useEffect } from 'react';

// --- Expresiones regulares para simular validaciones del pago ---
const cardRegex = /^\d{16}$/; // Valida 16 dígitos exactos
const expiryRegex = /^(0[1-9]|1[0-2])\/\d{2}$/; // Valida MM/YY
const cvvRegex = /^\d{3,4}$/; // Valida 3 o 4 dígitos

const Checkout = () => {
  const { products, totalPrice, emptyCart } = useCartStore();

  // --- Estados para el formulario de pago ---
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [address, setAddress] = useState('');
  const [city, setCity] = useState('');
  const [zip, setZip] = useState('');
  const [cardNumber, setCardNumber] = useState('');
  const [expiry, setExpiry] = useState('');
  const [cvv, setCvv] = useState('');

  // --- Estado de validación de datos bancarios ---
  const [isFormValid, setIsFormValid] = useState(false);

  // --- Efecto para validar el boton de pago cada que el formulario cambia ---
  useEffect(() => {
    const isNameValid = name.trim() !== '';
    const isEmailValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    const isAddressValid = address.trim() !== '';
    const isCityValid = city.trim() !== '';
    const isZipValid = /^\d{5}$/.test(zip); 
    const isCardValid = cardRegex.test(cardNumber);
    const isExpiryValid = expiryRegex.test(expiry);
    const isCvvValid = cvvRegex.test(cvv);

    setIsFormValid(
      isNameValid &&
      isEmailValid &&
      isAddressValid &&
      isCityValid &&
      isZipValid &&
      isCardValid &&
      isExpiryValid &&
      isCvvValid
    );
  }, [name, email, address, city, zip, cardNumber, expiry, cvv]);


  // --- Manejador del Envío ---
  const handleConfirmOrder = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!isFormValid) {
        alert("Por favor, revisa los datos del formulario. Hay errores o campos incompletos.");
        return;
    }

    // ---Posible JSON que se envíe a un endpoint ---
    const orderPayload = {
      items: products.map(item => ({
        id: item.id,
        amount: item.amount,
        price: item.price, // Precio unitario al momento de la compra
      })),
      total: totalPrice(),
      orderDate: new Date().toISOString(),
    };

    // --- Simular Envío al Backend ---
    console.log("--- ENVIANDO A CONSOLA ---");
    console.log(JSON.stringify(orderPayload, null, 2)); // Muestra el JSON bonito

    try {
        // const response = await fetch('/api/orders', { // <-- URL DEL ENDPOINT DE CHAVA SI IMPLEMENTAMOS ESTO
        //     method: 'POST',
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify(orderPayload),
        // });

        // if (!response.ok) { //VERIFICAR RESPUESTA DEL ENDPOINT
        //     throw new Error('Hubo un problema al crear el pedido.');
        // }
        
        // PROCESAR PAGO DE LA RESPUESTA SI SI SE HACE EL ENDPOINT
        console.log("--- RESPUESTA DEL BACKEND (SIMULADA): ÉXITO ---");
        
        // Mostrar Éxito
        alert("¡Gracias por tu compra! Tu pedido ha sido confirmado.");

        // Vaciar carrito
        emptyCart();

        // Redirigir (ej. a la home)
        // navigate('/'); 
        console.log("¡Carrito vaciado! Redirigiendo...");

    } catch (error) {
        console.error("Error al enviar el pedido:", error);
        alert("Lo sentimos, hubo un error al procesar tu pedido. Inténtalo de nuevo.");
    }
  };

  if (products.length === 0) {
    return (
      <div className="container mx-auto p-8 text-center">
        <h1 className="text-3xl mt-10 font-chewy  mb-4">Checkout</h1>
        <p className="text-xl">Tu carrito está vacío. ¡Animate a revisar todos nuestros productos!</p>
      </div>
    );
  }

  return (
    <div className="container mx-auto p-8">
      <h1 className="text-3xl font-bold mb-8 text-center">Finalizar Compra</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-12">

        {/* --- Columna 1: Formulario--- */}
        <div>
          <h2 className="text-2xl font-semibold mb-6">Tus Datos y Pago</h2>
          <form onSubmit={handleConfirmOrder} className="space-y-4">
            {/* --- Datos Personales --- */}
            <fieldset className="border p-4 rounded-lg">
                <legend className="text-lg font-medium px-2">Información Personal</legend>
                <div className="space-y-3 pt-2">
                    <div>
                        <Label htmlFor="name">Nombre Completo</Label>
                        <Input id="name" type="text" placeholder="Tu nombre" required value={name} onChange={e => setName(e.target.value)} className="mt-1" />
                    </div>
                    <div>
                        <Label htmlFor="email">Correo Electrónico</Label>
                        <Input id="email" type="email" placeholder="tu@correo.com" required value={email} onChange={e => setEmail(e.target.value)} className="mt-1" />
                    </div>
                </div>
            </fieldset>

            {/* --- Dirección --- */}
            <fieldset className="border p-4 rounded-lg">
                <legend className="text-lg font-medium px-2">Dirección de Envío</legend>
                <div className="space-y-3 pt-2">
                    <div>
                        <Label htmlFor="address">Calle y Número</Label>
                        <Input id="address" type="text" placeholder="Av. del Imán" required value={address} onChange={e => setAddress(e.target.value)} className="mt-1" />
                    </div>
                    <div className="grid grid-cols-2 gap-4">
                        <div>
                            <Label htmlFor="city">Ciudad</Label>
                            <Input id="city" type="text" placeholder="Ciudad de México" required value={city} onChange={e => setCity(e.target.value)} className="mt-1" />
                        </div>
                        <div>
                            <Label htmlFor="zip">Código Postal</Label>
                            <Input id="zip" type="text" placeholder="07900" required value={zip} onChange={e => setZip(e.target.value)} className="mt-1" />
                        </div>
                    </div>
                </div>
            </fieldset>

            {/* --- Pago --- */}
            <fieldset className="border p-4 rounded-lg">
                <legend className="text-lg font-medium px-2">Información de Pago </legend>
                 <div className="space-y-3 pt-2">
                    <div>
                        <Label htmlFor="card">Número de Tarjeta (16 dígitos)</Label>
                        <Input id="card" type="text" placeholder="0000 0000 0000 0000" required value={cardNumber} onChange={e => setCardNumber(e.target.value.replace(/\s/g, ''))} className="mt-1" maxLength={16} />
                        {!cardRegex.test(cardNumber) && cardNumber.length > 0 && <p className="text-red-500 text-xs mt-1">Debe tener 16 dígitos.</p>}
                    </div>
                    <div className="grid grid-cols-2 gap-4">
                        <div>
                            <Label htmlFor="expiry">Expiración (MM/YY)</Label>
                            <Input id="expiry" type="text" placeholder="01/26" required value={expiry} onChange={e => setExpiry(e.target.value)} className="mt-1" maxLength={5} />
                            {!expiryRegex.test(expiry) && expiry.length > 0 && <p className="text-red-500 text-xs mt-1">Formato MM/YY.</p>}
                        </div>
                        <div>
                            <Label htmlFor="cvv">CVV</Label>
                            <Input id="cvv" type="text" placeholder="123" required value={cvv} onChange={e => setCvv(e.target.value)} className="mt-1" maxLength={4} />
                             {!cvvRegex.test(cvv) && cvv.length > 0 && <p className="text-red-500 text-xs mt-1">Debe tener 3 o 4 dígitos.</p>}
                        </div>
                    </div>
                </div>
            </fieldset>

            {/* --- Botón --- */}
            <Button 
                type="submit" 
                className="w-full mt-10 font-chewy bg-rose-300 hover:bg-pink-300 text-lg py-3 disabled:bg-gray-400 disabled:cursor-not-allowed"
                disabled={!isFormValid} // El botón se deshabilita si el form no es válido
            >
              Confirmar y Pagar
            </Button>
            {!isFormValid && <p className="text-center text-sm text-gray-600 mt-2">Completa todos los campos correctamente para pagar.</p>}
          </form>
        </div>

        {/* --- Columna 2: Resumen del Pedido (es una implementación similar a CartSheet) --- */}
        <div className="bg-gray-50 p-6 rounded-lg shadow-sm">
          <h2 className="text-2xl font-semibold mb-6 border-b pb-3">Resumen de tu Pedido</h2>
          <div className="space-y-4 mb-6 max-h-64 overflow-y-auto pr-2">
            {products.map((item) => (
              <div key={item.id} className="flex items-center justify-between border-b pb-3">
                <div className="flex items-center">
                   <img src={item.imageUrl} alt={item.name} className="size-16 rounded object-cover mr-4" />
                   <div>
                      <p className="font-medium">{item.name}</p>
                      <p className="text-sm text-gray-500">Cantidad: {item.amount}</p>
                   </div>
                </div>
                <p className="font-medium">{formatCurrency(item.price * item.amount)}</p>
              </div>
            ))}
          </div>
          <div className="border-t pt-6 space-y-3">
             <div className="flex justify-between text-xl font-bold">
                <span>Total:</span>
                <span>{formatCurrency(totalPrice())}</span>
             </div>
          </div>
        </div>

      </div>
    </div>
  );
};

export default Checkout;