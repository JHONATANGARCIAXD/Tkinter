# Se imporata la libreria tkinter con todas su funciones  

from tkinter import *
from xml.dom.minidom import Document


#-----------------------
#Ventana principal
#-----------------------

# Se declarauna variable llamada ventana principal y que adquiere las caracteristicas de un objeto Tk()

ventana_principal=Tk()


# titulo de la ventana

ventana_principal.title("Jhonatan Garcia")


# Establecer tamaño a la ventana

ventana_principal.geometry("800x400")

# Icono de la ventana principal

# desabilitar boton de maximar

ventana_principal.resizable(0,0)

# color de fondo de la ventana principal

ventana_principal.config (bg="lime green")

# agregamos un widget a la ventana principal

letrero= Label(text="\n\nSistemas la mejor!!\n",bg="lime green")
letrero.pack()

# agregamos un widget a la ventana principal
letrero2= Label(text="\n\nJhonatan Garcia\n", bg="lime green")
letrero2.pack()

# agregamos un widget a la ventana principal
letrero3= Label(text="\n\nColegio San José de Guanentá\n", bg="lime green")
letrero3.pack()












# Se ejecuta el metodo mainlooṕ() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton, escribir, etc). Cada accion del usuario del usuario se conoce como un un evento. El metodo mainloop() es un bucle infinito.

ventana_principal.mainloop()



