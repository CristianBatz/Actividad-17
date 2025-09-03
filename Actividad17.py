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


class Sumar:
    def __init__(self, ventana, entrada,entrada2):
        self.ventana = ventana
        self.entrada = entrada
        self.entrada2 = entrada2
        self.resultado = 0

    def calcular_suma(self):
        self.resultado = self.entrada.get() + self.entrada2.get()
        etiqueta3.config(text=self.resultado)


suma = Sumar(ventana, entrada, entrada2)
boton_sumar = tk.Button(ventana, text="Sumar", command=suma.calcular_suma)
boton_sumar.pack(pady=5)

ventana.mainloop()