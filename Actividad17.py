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

etiqueta4 = tk.Label(ventana, text="Suma ")
etiqueta4.pack(pady=5)


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
        etiqueta4.config(text=self.resultado)

    def calcular_multiplicacion(self):
        num1 = int(self.entrada.get())
        num2 = int(self.entrada2.get())
        self.resultado = num1 * num2
        etiqueta5.config(text=self.resultado)



operaciones_matematicas = OperacionesMatematicas(ventana, entrada, entrada2)
boton_sumar = tk.Button(ventana, text="Sumar", command=operaciones_matematicas.calcular_suma)
boton_sumar.pack(pady=5)

etiqueta5 = tk.Label(ventana, text="multiplicacion ")
etiqueta5.pack(pady=5)

boton_multiplicar = tk.Button(ventana, text="multiplicar", command=operaciones_matematicas.calcular_multiplicacion)
boton_multiplicar.pack(pady=5)



ventana.mainloop()