# Se imporata la libreria tkinter con todas su funciones  

from tkinter import *


#-----------------------
#Ventana principal
#-----------------------

# Se declarauna variable llamada ventana principal y que adquiere las caracteristicas de un objeto Tk()

ventana_principal=Tk()


# titulo de la ventana

ventana_principal.title("Jhonatan Garcia")


# Establecer tamaño a la ventana

ventana_principal.geometry("800x500")



# Se ejecuta el metodo mainlooṕ() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton, escribir, etc). Cada accion del usuario del usuario se conoce como un un evento. El metodo mainloop() es un bucle infinito.

ventana_principal.mainloop()



