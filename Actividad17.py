import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora ")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Escriba el primer numero: ")
etiqueta.pack(pady=5)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

etiqueta2 = tk.Label(ventana, text="Escriba el segundo numero: ")
etiqueta2.pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

etiqueta3 = tk.Label(ventana, text="Resultado: ")
etiqueta3.pack(pady=5)



class OperacionesMatematicas:
    def __init__(self, ventana, entrada,entrada2):
        self.ventana = ventana
        self.entrada = entrada
        self.entrada2 = entrada2
        self.resultado = 0

    def calcular_suma(self):
        num1 = int(self.entrada.get())
        num2 = int(self.entrada2.get())
        self.resultado = num1 + num2
        etiqueta3.config(text=f"El resultado de la suma es: {int(self.resultado)}")

    def calcular_multiplicacion(self):
        num1 = int(self.entrada.get())
        num2 = int(self.entrada2.get())
        self.resultado = num1 * num2
        etiqueta3.config(text=f"El resultado de la multiplicacion es: {int(self.resultado)}")

    def calcular_resta(self):
        num1 = int(self.entrada.get())
        num2 = int(self.entrada2.get())
        self.resultado = num1 - num2
        etiqueta3.config(text=f"El resultado de la resta es: {int(self.resultado)}")

    def calcular_dividir(self):
        num1 = int(self.entrada.get())
        num2 = int(self.entrada2.get())
        self.resultado = num1 / num2
        if num2 == 0:
            etiqueta3.config(text=f"No se puede dividir entre {num2}")
        else:
            etiqueta3.config(text=f"El resultado de la division es: {int(self.resultado)}")

class Limpiar:
    def __init__(self, ventana, entrada, entrada2):
        self.ventana = ventana
        self.entrada = entrada
        self.entrada2 = entrada2
        self.resultado = 0

    def limpiar(self):
        entrada.delete(0, tk.END)
        entrada2.delete(0, tk.END)
        etiqueta3.config(text="Resultado: ")
        etiqueta4.config(text="Suma")
        etiqueta5.config(text="Multiplicacion")
        etiqueta6.config(text="Resta")
        etiqueta7.config(text="Dividir")
        self.resultado = 0




operaciones_matematicas = OperacionesMatematicas(ventana, entrada, entrada2)
limpiar_ventana = Limpiar(ventana, entrada, entrada2)
etiqueta4 = tk.Label(ventana, text="Suma")
etiqueta4.pack(pady=5)
boton_sumar = tk.Button(ventana, text="Sumar", command=operaciones_matematicas.calcular_suma)
boton_sumar.pack(pady=5)

etiqueta5 = tk.Label(ventana, text="multiplicacion ")
etiqueta5.pack(pady=5)

boton_multiplicar = tk.Button(ventana, text="multiplicar", command=operaciones_matematicas.calcular_multiplicacion)
boton_multiplicar.pack(pady=5)

etiqueta6 = tk.Label(ventana, text="resta")
etiqueta6.pack(pady=5)
boton_restar = tk.Button(ventana, text="restar", command=operaciones_matematicas.calcular_resta)
boton_restar.pack(pady=5)

etiqueta7 = tk.Label(ventana, text="division ")
etiqueta7.pack(pady=5)
boton_dividir = tk.Button(ventana, text="dividir", command=operaciones_matematicas.calcular_dividir)
boton_dividir.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_ventana.limpiar)
boton_limpiar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()