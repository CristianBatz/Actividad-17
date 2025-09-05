import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora ")
ventana.geometry("500x300")
ventana.config(bg = "#1e1e1e")

etiqueta0 = tk.Label(ventana, text="Calculadora python",font=("Arial", 20,"bold italic"),bg="#1e1e1e",fg="white")
etiqueta0.place(x=150, y=10)

etiqueta = tk.Label(ventana, text="Escriba el primer numero ",font=("Arial", 10,"bold italic"),bg="#1e1e1e",fg="white")
etiqueta.place(x=20, y=60)
entrada = tk.Entry(ventana,bg="#abc5e0", fg="black", relief="flat",highlightbackground="#3a3a3a", highlightcolor="#007acc", highlightthickness=2)
entrada.place(x=200, y=60, width=150)

etiqueta2 = tk.Label(ventana, text="Escriba el segundo numero ",font=("Arial", 10,"bold italic"),bg="#1e1e1e",fg="white")
etiqueta2.place(x=20, y=100)
entrada2 = tk.Entry(ventana,bg="#abc5e0", fg="black", relief="flat",highlightbackground="#3a3a3a", highlightcolor="#007acc", highlightthickness=2)
entrada2.place(x=200, y=100, width=150)

etiquetaR = tk.Label(ventana, text="Resultado ",font=("Arial", 10,"bold italic"),bg="#1e1e1e",fg="white")
etiquetaR.place(x=20, y=140)
etiqueta3 = tk.Label(ventana,font=("Arial", 10,"bold italic"),bg="#1e1e1e",fg="white")
etiqueta3.place(x=200, y=140)



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
        etiqueta3.config(text=f"El resultado de la suma es: {self.resultado:.2f}")

    def calcular_multiplicacion(self):
        num1 = float(self.entrada.get())
        num2 = float(self.entrada2.get())
        self.resultado = num1 * num2
        etiqueta3.config(text=f"El resultado de la multiplicacion es: {self.resultado:.2f}")

    def calcular_resta(self):
        num1 = float(self.entrada.get())
        num2 = float(self.entrada2.get())
        self.resultado = num1 - num2
        etiqueta3.config(text=f"El resultado de la resta es: {self.resultado:.2f}")

    def calcular_dividir(self):
        num1 = float(self.entrada.get())
        num2 = float(self.entrada2.get())
        if num2 == 0:
            etiqueta3.config(text=f"No se puede dividir entre {num2}")
        else:
            self.resultado = num1 / num2
            etiqueta3.config(text=f"El resultado de la division es: {self.resultado:.2f}")

class Limpiar:
    def __init__(self, ventana, entrada, entrada2):
        self.ventana = ventana
        self.entrada = entrada
        self.entrada2 = entrada2
        self.resultado = 0

    def limpiar(self):
        entrada.delete(0, tk.END)
        entrada2.delete(0, tk.END)
        etiqueta3.config(text= "",font=("Arial", 10,"bold italic"),bg="black",fg="white")
        self.resultado = 0




operaciones_matematicas = OperacionesMatematicas(ventana, entrada, entrada2)
limpiar_ventana = Limpiar(ventana, entrada, entrada2)

etiquetaP = tk.Label(ventana, text="Operaciones ",font=("Arial", 10,"bold italic"),bg="#1e1e1e",fg="white")
etiquetaP.place(x=20, y=180)

boton_sumar = tk.Button(ventana, text="Sumar", command=operaciones_matematicas.calcular_suma, relief ="raised",bd = 3,activebackground ="grey",width=8, height=1,activeforeground="white",font=("Arial", 10,"bold italic"))
boton_sumar.place(x=200, y=180)

boton_multiplicar = tk.Button(ventana, text="multiplicar", command=operaciones_matematicas.calcular_multiplicacion, relief ="raised",bd = 3,activebackground ="grey",width=8, height=1,activeforeground="white",font=("Arial", 10,"bold italic"))
boton_multiplicar.place(x=200, y=220)

boton_restar = tk.Button(ventana, text="restar", command=operaciones_matematicas.calcular_resta, relief ="raised",bd = 3,activebackground ="grey",width=8, height=1,activeforeground="white",font=("Arial", 10,"bold italic"))
boton_restar.place(x=300, y=180)

boton_dividir = tk.Button(ventana, text="dividir", command=operaciones_matematicas.calcular_dividir, relief ="raised",bd = 3,activebackground ="grey",width=8, height=1,activeforeground="white",font=("Arial", 10,"bold italic"))
boton_dividir.place(x=300, y=220)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_ventana.limpiar, relief ="raised",bd = 3,activebackground ="grey",width=8, height=1,activeforeground="white",font=("Arial", 10,"bold italic"))
boton_limpiar.place(x=200, y=260)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit, relief ="raised",bd = 3,activebackground ="grey",width=8, height=1,activeforeground="white",font=("Arial", 10,"bold italic"))
boton_salir.place(x=300, y=260)

ventana.mainloop()