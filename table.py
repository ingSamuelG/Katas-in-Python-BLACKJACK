from tkinter import *


Raiz= Tk()


Micanvas=Canvas(Raiz, width= 1200, height=700)
Micanvas.pack()



def center(ventana):
	ventana.update_idletasks()
	width= ventana.winfo_width()
	height= ventana.winfo_height()
	x = (ventana.winfo_screenwidth() // 2) - (width // 2)
	y = (ventana.winfo_screenheight() //2) - (height// 2)
	ventana.geometry('{}x{}+{}+{}'.format(width,height,x,y))

FondoMesa=PhotoImage(file="asset/table.png")
ImagenBotonRojo=PhotoImage(file="asset/botones/botonr.png")
ImagenBotonVerde=PhotoImage(file="asset/botones/botonv.png")
Carta1=PhotoImage(file="asset/C/TC.png")
Carta2=PhotoImage(file="asset/H/AH.png")
imagenf10=PhotoImage(file="asset/fichas/F10.png")
Etiqueta_fondo=Label(Raiz, image=FondoMesa)
Etiqueta_fondo.place(relwidth=1, relheight=1)

#___________________________

Boton_rojo=Button(Raiz,image=ImagenBotonRojo)
Boton_rojo.config(bd=0, bg="#8c2027",activebackground="#8c2027")
Boton_rojo.place(relx=0.8, rely=0.85,relheight=0.15, relwidth=0.08)

Boton_verde=Button(Raiz,image=ImagenBotonVerde)
Boton_verde.config(bd=0, bg="#a01c1f",activebackground="#a01c1f")
Boton_verde.place(relx=0.7, rely=0.75,relheight=0.15, relwidth=0.088)


#----------------------Fichas-------------------------------------------------

ficha10=Radiobutton(Raiz, text="10", value=10, font=("Casino","20"))
ficha10.place(relx=0.1, rely=0.75, relheight=0.136 ,relwidth=0.05)

ficha50=Radiobutton(Raiz, text="40", value=50, font=("Casino","20")) #the font that im using have a bug that takes the character 4 for 5 and vice versa#
ficha50.place(relx=0.15, rely=0.75, relheight=0.136 ,relwidth=0.05)

ficha100=Radiobutton(Raiz, text="100", value=100, font=("Casino","20"))
ficha100.place(relx=0.2, rely=0.75, relheight=0.136 ,relwidth=0.05)

ficha500=Radiobutton(Raiz, text="400", value=500, font=("Casino","20")) #the font that im using have a bug that takes the character 4 for 5 and vice versa#
ficha500.place(relx=0.25, rely=0.75, relheight=0.136 ,relwidth=0.05)

#-------------------------------------------------------------------------------

CartaMano1=Label(Raiz, image=Carta1)
CartaMano1.place(relx=0.5, rely=0.75, relheight=0.136 ,relwidth=0.06)
CartaMano2=Label(Raiz, image=Carta2)
CartaMano2.place(relx=0.435, rely=0.75, relheight=0.136 ,relwidth=0.06)






center(Raiz)

Raiz.mainloop()