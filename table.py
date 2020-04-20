from tkinter import *


Raiz= Tk()


Micanvas=Canvas(Raiz, width= 1200, height=700)
Micanvas.pack()

ApuestaVar=StringVar()
CantidadApostar=IntVar()

ApuestaVar.set("0")

def center(ventana):
	ventana.update_idletasks()
	width= ventana.winfo_width()
	height= ventana.winfo_height()
	x = (ventana.winfo_screenwidth() // 2) - (width // 2)
	y = (ventana.winfo_screenheight() //2) - (height// 2)
	ventana.geometry('{}x{}+{}+{}'.format(width,height,x,y))


def defiene_apuesta():
	Cantidad=CantidadApostar.get()
	En_pantalla= ApuestaVar.get()
	resultado= Cantidad + int(En_pantalla)

	ApuestaVar.set(resultado)

#_________________________imagenes________________________________________

FondoMesa=PhotoImage(file="asset/table.png")
ImagenBotonRojo=PhotoImage(file="asset/botones/botonr.png")
ImagenBotonVerde=PhotoImage(file="asset/botones/botonv.png")
Carta1=PhotoImage(file="asset/C/TC.png")
Carta2=PhotoImage(file="asset/H/AH.png")
imagenF10=PhotoImage(file="asset/fichas/F10.png")
imagenF50=PhotoImage(file="asset/fichas/F50.png")
imagenF100=PhotoImage(file="asset/fichas/F100.png")
imagenF500=PhotoImage(file="asset/fichas/F500.png")
Etiqueta_fondo=Label(Raiz, image=FondoMesa)
Etiqueta_fondo.place(relwidth=1, relheight=1)


BarraMenu=Menu(Raiz)

NuevoMenu=Menu(BarraMenu, tearoff=0)
NuevoMenu.add_command(label="Repartir de cartas")
NuevoMenu.add_command(label="Salir")

BarraMenu.add_cascade(label="Menu", menu=NuevoMenu)
BarraMenu.add_cascade(label="Borrar", menu=BorrarMenu)

#____________________Botones_________________________________________________

Boton_rojo=Button(Raiz,image=ImagenBotonRojo)
Boton_rojo.config(bd=0, bg="#8c2027",activebackground="#8c2027")
Boton_rojo.place(relx=0.8, rely=0.85,relheight=0.15, relwidth=0.08)

Boton_verde=Button(Raiz,image=ImagenBotonVerde, command=defiene_apuesta)
Boton_verde.config(bd=0, bg="#a01c1f",activebackground="#a01c1f")
Boton_verde.place(relx=0.7, rely=0.75,relheight=0.15, relwidth=0.088)


#----------------------Fichas-------------------------------------------------


ApuestaPantalla=Entry( bg="black", textvariable=ApuestaVar ,font=("NI7seg",18),fg="#03f943",justify="right")
ApuestaPantalla.place(relx=0.13, rely= 0.68, relheight=0.05, relwidth=0.1)

EtiquetaF10=Label(Raiz, image=imagenF10, bg="#88202a")
EtiquetaF10.place(relx=0.05, rely= 0.75, relheight=0.1, relwidth=0.05)

ficha10=Radiobutton(Raiz, text="10", value=10, variable=CantidadApostar,font=("Casino","20"),bg="#88202a", activebackground="#8c2027")
ficha10.select()
ficha10.place(relx=0.068, rely=0.85, relheight=0.035 ,relwidth=0.045)

EtiquetaF50=Label(Raiz, image=imagenF50, bg="#941b22")
EtiquetaF50.place(relx=0.120, rely= 0.75, relheight=0.09, relwidth=0.05)

ficha50=Radiobutton(Raiz, text="40", value=50, variable=CantidadApostar,font=("Casino","20"), bg="#88202a", activebackground="#8c2027") #the font that im using have a bug that takes the character 4 for 5 and vice versa#
ficha50.place(relx=0.14, rely=0.85, relheight=0.035 ,relwidth=0.045)

EtiquetaF100=Label(Raiz, image=imagenF100, bg="#a31d24")
EtiquetaF100.place(relx=0.192, rely= 0.75, relheight=0.1, relwidth=0.05)

ficha100=Radiobutton(Raiz, text="100", value=100, variable=CantidadApostar, font=("Casino","20"), bg="#9f1f24",activebackground="#9f1f24")
ficha100.place(relx=0.21, rely=0.85, relheight=0.035 ,relwidth=0.06)

EtiquetaF500=Label(Raiz, image=imagenF500, bg="#a31d24")
EtiquetaF500.place(relx=0.26, rely= 0.75, relheight=0.09, relwidth=0.05)

ficha500=Radiobutton(Raiz, text="400", value=500, variable=CantidadApostar , font=("Casino","20"), bg="#a21e22", activebackground="#a21e22") #the font that im using have a bug that takes the character 4 for 5 and vice versa#
ficha500.place(relx=0.28, rely=0.85, relheight=0.035 ,relwidth=0.06)

#-------------------------Mano jugador----------------------------------------------

CartaMano1=Label(Raiz, image=Carta1)
CartaMano1.place(relx=0.5, rely=0.75, relheight=0.136 ,relwidth=0.06)
CartaMano2=Label(Raiz, image=Carta2)
CartaMano2.place(relx=0.435, rely=0.75, relheight=0.136 ,relwidth=0.06)






Raiz.config(menu=BarraMenu)
Raiz.title("BlackJack")
center(Raiz)

Raiz.mainloop()