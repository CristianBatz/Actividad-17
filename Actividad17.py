import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora ")
ventana.geometry("300x200")
ventana.config(bg = "black")

etiqueta0 = tk.Label(ventana, text="Calculadora python",font=("Arial", 20,"bold"),bg="grey",fg="white")
etiqueta0.pack(pady=5)

etiqueta = tk.Label(ventana, text="Escriba el primer numero: ",font=("Arial", 10,"bold"),bg="grey",fg="white")
etiqueta.pack(pady=5)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

etiqueta2 = tk.Label(ventana, text="Escriba el segundo numero: ",font=("Arial", 10,"bold"),bg="grey",fg="white")
etiqueta2.pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

etiqueta3 = tk.Label(ventana, text="Resultado: ",font=("Arial", 10,"bold"),bg="grey",fg="black")
etiqueta3.pack(pady=5)



class OperacionesMatematicas:
    def __init__(self, ventana, entrada,entrada2):
        self.ventana = ventana
        self.entrada = entrada
        self.entrada2 = entrada2
        self.resultado = 0

    def calcular_suma(self):
        num1 = float(self.entrada.get())
        num2 = float(self.entrada2.get())
        self.resultado = num1 + num2
        etiqueta3.config(text=f"El resultado de la suma es: {float(self.resultado)}")

    def calcular_multiplicacion(self):
        num1 = float(self.entrada.get())
        num2 = float(self.entrada2.get())
        self.resultado = num1 * num2
        etiqueta3.config(text=f"El resultado de la multiplicacion es: {float(self.resultado)}")

    def calcular_resta(self):
        num1 = float(self.entrada.get())
        num2 = float(self.entrada2.get())
        self.resultado = num1 - num2
        etiqueta3.config(text=f"El resultado de la resta es: {float(self.resultado)}")

    def calcular_dividir(self):
        num1 = float(self.entrada.get())
        num2 = float(self.entrada2.get())
        if num2 == 0:
            etiqueta3.config(text=f"No se puede dividir entre {num2}")
        else:
            self.resultado = num1 / num2
            etiqueta3.config(text=f"El resultado de la division es: {float(self.resultado)}")

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

        self.resultado = 0




operaciones_matematicas = OperacionesMatematicas(ventana, entrada, entrada2)
limpiar_ventana = Limpiar(ventana, entrada, entrada2)

boton_sumar = tk.Button(ventana, text="Sumar", command=operaciones_matematicas.calcular_suma, relief ="raised",bd = 3,activebackground ="grey",width=8, height=1,activeforeground="white")
boton_sumar.pack(pady=7)

boton_multiplicar = tk.Button(ventana, text="multiplicar", command=operaciones_matematicas.calcular_multiplicacion, relief ="raised",bd = 3,activebackground ="grey",width=8, height=1,activeforeground="white")
boton_multiplicar.pack(pady=7)

boton_restar = tk.Button(ventana, text="restar", command=operaciones_matematicas.calcular_resta, relief ="raised",bd = 3,activebackground ="grey",width=8, height=1,activeforeground="white")
boton_restar.pack(pady=7)

boton_dividir = tk.Button(ventana, text="dividir", command=operaciones_matematicas.calcular_dividir, relief ="raised",bd = 3,activebackground ="grey",width=8, height=1,activeforeground="white")
boton_dividir.pack(pady=7)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_ventana.limpiar, relief ="raised",bd = 3,activebackground ="grey",width=8, height=1,activeforeground="white")
boton_limpiar.pack(pady=7)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit, relief ="raised",bd = 3,activebackground ="grey",width=8, height=1,activeforeground="white")
boton_salir.pack(pady=7)

ventana.mainloop()