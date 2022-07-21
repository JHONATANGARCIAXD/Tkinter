from tkinter import *


ventana_principal= Tk()

ventana_principal.title("PERÚ")

ventana_principal.config(bg="red")

ventana_principal.geometry("800x500")

ventana_principal.resizable(0,0)




frame_entrada = Frame(ventana_principal)
frame_entrada.config (bg="white", width=240 , height=780)
frame_entrada.place(x=10,y=250)
frame_entrada.pack()
















ventana_principal.mainloop()
