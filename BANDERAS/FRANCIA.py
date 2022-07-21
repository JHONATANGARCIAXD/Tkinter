

from tkinter import *


ventana_principal= Tk()

ventana_principal.title("FRANCIA")

ventana_principal.config(bg="black")

ventana_principal.geometry("800x500")

ventana_principal.resizable(0,0)

frame_entrada=Frame(ventana_principal)
frame_entrada.config (bg="blue", width=270, height=780)
frame_entrada.place(x=10, y= 10)


frame_2=Frame(ventana_principal)
frame_2.config (bg="white", width=270, height=780)
frame_2.place(x=250 ,y=10)

frame_3=Frame(ventana_principal)
frame_3.config (bg="red", width=270, height=780)
frame_3.place(x=520, y=10)























ventana_principal.mainloop()
