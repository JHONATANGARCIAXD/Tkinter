

# Se imporata la libreria tkinter con todas su funciones  



from cgitb import scanvars, text
from tkinter import *
from tkinter import messagebox


#---------------------
# Funciones de la app
#---------------------


def Sumar():
    #messagebox.showinfo("Suma 1.0" , "Hizo click en el boton sumar....")
    c=int(a.get()) + int(b.get())
    t_resultado.insert(INSERT, " La Suma de " + a.get() + " + " +  b.get() + " Casi siempre es: "  + str(c)+"\n")

def Borrar():
    messagebox.showinfo("Suma 1.0" , "Hizo click en el boton borrar....")
    a.set("")
    b.set("")  
    t_resultado.delete("1.0" , "end")


def Salir():
    messagebox.showinfo("Suma 1.0" , "La APP se cerrara....")
    ventana_principal.destroy()


#-----------------------
#Ventana principal
#-----------------------

# Se declarauna variable llamada ventana principal y que adquiere las caracteristicas de un objeto Tk()

ventana_principal=Tk()

# Titulo de la ventana

ventana_principal.title("Jhonatan Garcia")

# Establecer tamaño a la ventana

ventana_principal.geometry("800x500")

# Icono de la ventana principal

# Desabilitar boton de maximar

ventana_principal.resizable(0,0)

# Color de fondo de la ventana principal

ventana_principal.config (bg="white")


#----------------
#Variables Globales
#------------------

a=StringVar()
b=StringVar()
c=StringVar()
#-----------------------
#Frame Entrada
#-----------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config (bg="grey1", width=780, height=240)
frame_entrada.place(x=10 ,y=10)

#-----------------------
# Frame Operaciones
#-----------------------

frame_operaciones= Frame(ventana_principal)
frame_operaciones.config (bg="grey2" , width=780, height=120)
frame_operaciones.place(x=10 ,y=260)

#-----------------------
# Frame Resultado
#-----------------------

frame_resultado= Frame(ventana_principal)
frame_resultado.config (bg="grey3", width=780, height=100)
frame_resultado.place(x=10 ,y=390)

# Etiqueta  para el titulo de la app

titulo= Label(frame_entrada, text="Colegio San José De Guanenta")
titulo.config (bg="grey1" , fg="medium blue" , font=("Calibri Light" , 15))
titulo.place(x=390 , y=10)

# Etiqueta  para el subtitulo de la app

titulo= Label(frame_entrada , text="Especialidad De Sistemas")
titulo.config(bg="grey1" , fg="medium blue" , font=("Bahnschrift SemiLight" , 15))
titulo.place(x=390 , y=40)

# Etiqueta  para el subtitulo2 de la app

titulo= Label(frame_entrada , text="Suma De Enteros")
titulo.config(bg="grey1" , fg="medium blue" , font=("Arial" , 15))
titulo.place(x=390 , y=70)

# Imagen de la app

logo = PhotoImage(file="Suma.png")
etiq_logo=Label(frame_entrada, image=logo)
etiq_logo.place(x=10 , y=10)

# Etiqueta  para el valor A

etiq_valor_A=Label(frame_entrada, text="A =")
etiq_valor_A.config(bg="grey1" , fg="medium blue" , font=("Arial" , 15), anchor=CENTER)
etiq_valor_A.place(x=390 ,y=120)

# entry para el valor A

entry_a= Entry(frame_entrada , width=8 , textvariable=a)
entry_a.config(font=("Arial",20), justify=CENTER)
entry_a.place(x=425, y=120)
entry_a.focus_set()

# Etiqueta  para el valor B

etiq_valor_B=Label(frame_entrada, text="B =")
etiq_valor_B.config(bg="grey1" , fg="medium blue" , font=("Arial" , 15),anchor=CENTER)
etiq_valor_B.place(x=585 ,y=120)

# entry para el valor B

entry_b= Entry(frame_entrada , width=8,textvariable=b )
entry_b.config(font=("Arial",20), justify=CENTER)
entry_b.place(x=620 , y=120)

# Boton Sumar Números - Texto

# bt_Sumar=Button(frame_operaciones , text="Salir" , width=10)
bt_Suma=PhotoImage(file="Suma1.png")
bt_Sumar=Button(frame_operaciones, bg="grey1",image=bt_Suma , text="Sumar" , width=105 , height=105, command=Sumar)
bt_Sumar.place(x=116,y=7)

# Boton Borrar Entradas y  Resultado

# bt_Borrar=Button(frame_operaciones , text="Borrar" , width=10)
bt_Bor=PhotoImage(file="BORRAR.png")
bt_Borrar=Button(frame_operaciones ,  bg="grey1", image=bt_Bor ,text="Borrar" , width=105, height=105, command=Borrar)
bt_Borrar.place(x=337,y=7)

# Boton Cerrar App

# bt_Salir=Button(frame_operaciones , text="Salir" , width=10)
bt_Sali=PhotoImage(file="Salida.png")
bt_Salir=Button(frame_operaciones, bg="grey1",  image=bt_Sali, width=105 , height=105 , command=Salir)
bt_Salir.place(x=558,y=7)


# Area de texto para resultado
t_resultado= Text(frame_resultado, width=52 , height=3)
t_resultado.config(bg="grey40" , fg="White", font=("Arial" , 20))
t_resultado.pack()










# Se ejecuta el metodo mainlooṕ() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton, escribir, etc). Cada accion del usuario del usuario se conoce como un un evento. El metodo mainloop() es un bucle infinito.

ventana_principal.mainloop()



