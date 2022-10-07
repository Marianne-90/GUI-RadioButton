from tkinter import *

def seleccionar():
    opcionSeleccionada.config(text="{}".format(selected.get()))

def reset():
    selected.set(None)
    opcionSeleccionada.config(text="")

# Configuración de la raíz
opcion = Tk()

selected = IntVar()

Radiobutton(opcion, text="Opción 1", variable=selected, 
            value=1, command=seleccionar).pack()
Radiobutton(opcion, text="Opción 2", variable=selected, 
            value=2, command=seleccionar).pack()
Radiobutton(opcion, text="Opción 3", variable=selected,   
            value=3, command=seleccionar).pack()

opcionSeleccionada = Label(opcion)
opcionSeleccionada.pack()

Button(opcion, text="Reiniciar", command=reset).pack()

# Finalmente bucle de la aplicación
opcion.mainloop()