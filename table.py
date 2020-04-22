from tkinter import *
from tkinter import messagebox
from funciones import construir_maso, pedir_carta, dame_valor, decide

def inicia(apostad=0):
	global cont
	global Apostado
	global Apuesta_pasada
	global gano
	global manoanteriorg
	global maso
	global posicarta
	global posicartaC
	global me_atrevi


	s_q_casa=0
	posicarta=0.5
	posicartac=0.5
	me_atrevi=0

	cartas=construir_maso()

	carta1= cartas[0][0]
	carta2=	cartas[0][1]
	carta3= cartas[1][0]
	carta4= cartas[1][1]

	maso=cartas[2]

	if gano==0 :
		ApuestaVar.set("0")
	else:
		MisFichasVar.set(int(MisFichasVar.get())+Apostado*2)
		ApuestaVar.set("0")
		gano=0

	cont=0
	Apostado=0



	def computadora_play():
		global cont
		global maso
		global casa
		global mano
		global gano
		global maso
		global posicarta
		global posicartaC
		global s_q_casa
				
		if casa in range(0,12) :
			print("hice algo")
			nuevo_set=pedir_carta(maso)
			cartaNueva=nuevo_set[0]
			maso=nuevo_set[1]
			casa+=dame_valor(cartaNueva)
			posicarta-=0.03
			CartaMano2=Label(Raiz, image=eval(cartaNueva))
			CartaMano2.place(relx=posicartaC, rely=0.3, relheight=0.136 ,relwidth=0.06)
			
			if casa>=22:
				messagebox.showwarning("Ganaste", "La casa se paso")
				gano+=1
				inicia(Apostado)
			elif casa==21:
				messagebox.showwarning("Perdiste", "BlackJack de la casa")
				inicia(Apostado)

		elif casa in range(10,18):

			lo_hago=decide()
			print("Me atrevi a juagar")

			if lo_hago==True and me_atrevi==0:

				nuevo_set=pedir_carta(maso)
				cartaNueva=nuevo_set[0]
				maso=nuevo_set[1]
				casa+=dame_valor(cartaNueva)
				posicarta-=0.03
				CartaMano2=Label(Raiz, image=eval(cartaNueva))
				CartaMano2.place(relx=posicarta, rely=0.3, relheight=0.136 ,relwidth=0.06)	
				if casa>=22:
					messagebox.showwarning("Ganaste", "La casa se paso")
					gano+=1
					inicia(Apostado)
				elif casa==21:
					messagebox.showwarning("Perdiste", "BlackJack de la casa")
					inicia(Apostado)
			else:
				s_q_casa=1
				print("me quede")
					
				
		elif casa in range(19,21):
			print("me quedarse")
			s_q_casa=1
		else:
			messagebox.showwarning("Ganaste", "Se paso")
			gano+=1
			inicia(Apostado)

	def jugar(carta1,carta2,carta3,carta4, Apuesta):

		global cont
		global Apostado
		global Apuesta_pasada
		global maso
		global casa
		global mano
		global gano
		global manoanterior
		global maso
		global posicarta
		global me_atrevi
		global s_q_casa

		valor1=dame_valor(carta1)
		valor2=dame_valor(carta2)

		valor4=dame_valor(carta4)
		valor3=dame_valor(carta3)

		if Apuesta.startswith("-"):
			sinMenos=Apuesta[1:]
		else:
			sinMenos=Apuesta

		Apostado=int(sinMenos)

		if casa<22 or mano< 22:
			if  int(sinMenos) > 0 and cont==0:
				cont+=1
				Apuesta_pasada=int(sinMenos)

				CartaMano1=Label(Raiz, image=eval(carta1))
				CartaMano1.place(relx=0.5, rely=0.75, relheight=0.136 ,relwidth=0.06)
				CartaMano2=Label(Raiz, image=eval(carta2))
				CartaMano2.place(relx=0.435, rely=0.75, relheight=0.136 ,relwidth=0.06)


				CartaMano1=Label(Raiz, image=eval(carta3))
				CartaMano1.place(relx=0.5, rely=0.1, relheight=0.136 ,relwidth=0.06)
				CartaMano2=Label(Raiz, image=eval(carta4))
				CartaMano2.place(relx=0.435, rely=0.1, relheight=0.136 ,relwidth=0.06)

				mano=valor1+valor2
				casa= valor3+valor4
				computadora_play()

			elif cont==1 and Apuesta_pasada!=Apostado:
				respuesta=messagebox.askquestion("Dooooooobleeeeee","en esta fase solo puedes apostar el doble deseas Hacerlo?")
				if respuesta =="yes":
					Apostado = Apuesta_pasada*2
					ApuestaVar.set("-"+str(Apostado))
					nuevo_set=pedir_carta(maso)
					cartaNueva=nuevo_set[0]
					maso=nuevo_set[1]
					mano+=dame_valor(cartaNueva)
					CartaMano1=Label(Raiz, image=eval(cartaNueva))
					CartaMano1.place(relx=0.5, rely=0.5, relheight=0.136 ,relwidth=0.06)
					if mano>=22:
						messagebox.showwarning("Perdiste", "Te pasaste del BlackJack")
						inicia(Apostado)
					elif mano==21:
						messagebox.showwarning("Ganaste", "BlackJack")
						gano=1
						inicia(Apostado)
					else:
						cont+=1
						Apuesta_pasada=Apostado
						mano=mano
				computadora_play()

			elif cont==2 and Apuesta_pasada!=Apostado:
				messagebox.showwarning("Error", "No puedes seguir apostando")
				ApuestaVar.set(Apuesta_pasada)
				MisFichasVar.set(5000-int(Apostado))

			elif cont==2 or cont==1 and Apuesta_pasada==Apostado:
					nuevo_set=pedir_carta(maso)
					cartaNueva=nuevo_set[0]
					maso=nuevo_set[1]
					mano+=dame_valor(cartaNueva)
					posicarta-=0.03
					CartaMano1=Label(Raiz, image=eval(cartaNueva))
					CartaMano1.place(relx=posicarta, rely=0.5, relheight=0.136 ,relwidth=0.06)
					if mano>=22:
						messagebox.showwarning("Perdiste", "Te pasaste del BlackJack")
						ApuestaVar.set("0")
						inicia(Apostado)
					elif mano==21:
						messagebox.showwarning("Ganaste", "BlackJack")
						gano=1
						inicia(Apostado)
					computadora_play()
			else:
				messagebox.showinfo("Apuesta", "No has apostado nada")
		else:
			inicia(Apostado)

		print("turno :", cont)
		print("Se esta Apostando: ", Apostado)
		print("la apuesta anterior era:" ,Apuesta_pasada)
		print("mano del juagdor", mano)
		print("mano de la casa: ",casa)

	def quedarse():
		global mano
		global manoanterior
		global casa
		global Apostado
		global s_q_casa

		s_q_mano=1

		if s_q_mano==1 and s_q_casa==0:

			if casa>21:
				computadora_play()
			else:
				print("no jugue porque no sirve")


		elif s_q_mano==1 and s_q_casa==1:
			if cont>0:
				if casa==mano:
					messagebox.showinfo("Split", "Un empate o split")
					MisFichasVar.set(int(MisFichasVar.get())+Apostado)
					inicia(Apostado)

				elif casa>mano:
					messagebox.showinfo("Perdiste", "La casa tiene: {}".format(casa))
					inicia(Apostado)

				elif casa<mano:
					messagebox.showinfo("Ganaste", "tu  mano tiene: {} y la casa tiene {}".format(mano,casa))
					ApuestaVar.set("0")
					MisFichasVar.set(int(MisFichasVar.get())+Apostado*2)
					gano=1
					inicia(Apostado)
				else:
					messagebox.showwarning("Apuesta", "No se ha juagado nada")
			else:
				messagebox.showwarning("Apuesta", "No se ha juagado nada")


	def defiene_apuesta():

		Cantidad=CantidadApostar.get()
		En_pantalla=ApuestaVar.get()
		if ApuestaVar.get()=="0":
			resultado= Cantidad + int(En_pantalla)
		
		else:
			sinMenos=En_pantalla[1:]
			resultado= Cantidad + int(sinMenos)
			
		MisFichas=MisFichasVar.get()
		Restante=int(MisFichas)-Cantidad
		MisFichasVar.set(str(Restante))

		ApuestaVar.set("-{}".format(resultado))


	Etiqueta_fondo=Label(Raiz, image=FondoMesa)
	Etiqueta_fondo.place(relwidth=1, relheight=1)


	Boton_rojo=Button(Raiz,image=ImagenBotonRojo, command=quedarse)
	Boton_rojo.config(bd=0, bg="#8c2027",activebackground="#8c2027")
	Boton_rojo.place(relx=0.8, rely=0.85,relheight=0.15, relwidth=0.08)

	Boton_verde=Button(Raiz,image=ImagenBotonVerde, command=defiene_apuesta)
	Boton_verde.config(bd=0, bg="#a01c1f",activebackground="#a01c1f")
	Boton_verde.place(relx=0.7, rely=0.75,relheight=0.15, relwidth=0.088)

	Boton_Juega=Button(Raiz,image=ImagenBotonJuega, command= lambda:jugar(carta1,carta2,carta3,carta4, ApuestaVar.get()))
	Boton_Juega.config(bd=0, bg="#a01c1f",activebackground="#a01c1f")
	Boton_Juega.place(relx=0.75, rely=0.6,relheight=0.15, relwidth=0.088)

	#----------------------Fichas-------------------------------------------------

	MisFichas=Entry( bg="black", textvariable=MisFichasVar ,font=("NI7seg",18),fg="#03f943",justify="right")
	MisFichas.place(relx=0.13, rely= 0.63, relheight=0.05, relwidth=0.1)

	ApuestaPantalla=Entry( bg="black", textvariable=ApuestaVar ,font=("NI7seg",18),fg="red",justify="right")
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

# _______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


Raiz= Tk()

	#_________________________imagenes________________________________________

FondoMesa=PhotoImage(file="asset/table.png")
ImagenBotonRojo=PhotoImage(file="asset/botones/botonr.png")
ImagenBotonVerde=PhotoImage(file="asset/botones/botonv.png")
ImagenBotonJuega=PhotoImage(file="asset/botones/botonp.png")

Carta1=PhotoImage(file="asset/C/TC.png")
Carta2=PhotoImage(file="asset/H/AH.png")
imagenF10=PhotoImage(file="asset/fichas/F10.png")
imagenF50=PhotoImage(file="asset/fichas/F50.png")
imagenF100=PhotoImage(file="asset/fichas/F100.png")
imagenF500=PhotoImage(file="asset/fichas/F500.png")

AC=PhotoImage(file="asset/C/AC.png")
DOSC=PhotoImage(file="asset/C/2C.png")
TRESC=PhotoImage(file="asset/C/3C.png")
CUATROC=PhotoImage(file="asset/C/4C.png")
CINCOC=PhotoImage(file="asset/C/5C.png")
SEISC=PhotoImage(file="asset/C/6C.png")
SIETEC=PhotoImage(file="asset/C/7C.png")
OCHOC=PhotoImage(file="asset/C/8C.png")
NUEVEC=PhotoImage(file="asset/C/9C.png")
TC=PhotoImage(file="asset/C/TC.png")
JC=PhotoImage(file="asset/C/JC.png")
QC=PhotoImage(file="asset/C/QC.png")
KC=PhotoImage(file="asset/C/KC.png")

AS=PhotoImage(file="asset/S/AS.png")
DOSS=PhotoImage(file="asset/S/2S.png")
TRESS=PhotoImage(file="asset/S/3S.png")
CUATROS=PhotoImage(file="asset/S/4S.png")
CINCOS=PhotoImage(file="asset/S/5S.png")
SEISS=PhotoImage(file="asset/S/6S.png")
SIETES=PhotoImage(file="asset/S/7S.png")
OCHOS=PhotoImage(file="asset/S/8S.png")
NUEVES=PhotoImage(file="asset/S/9S.png")
TS=PhotoImage(file="asset/S/TS.png")
JS=PhotoImage(file="asset/S/JS.png")
QS=PhotoImage(file="asset/S/QS.png")
KS=PhotoImage(file="asset/S/KS.png")

AH=PhotoImage(file="asset/H/AH.png")
DOSH=PhotoImage(file="asset/H/2H.png")
TRESH=PhotoImage(file="asset/H/3H.png")
CUATROH=PhotoImage(file="asset/H/4H.png")
CINCOH=PhotoImage(file="asset/H/5H.png")
SEISH=PhotoImage(file="asset/H/6H.png")
SIETEH=PhotoImage(file="asset/H/7H.png")
OCHOH=PhotoImage(file="asset/H/8H.png")
NUEVEH=PhotoImage(file="asset/H/9H.png")
TH=PhotoImage(file="asset/H/TH.png")
JH=PhotoImage(file="asset/H/JH.png")
QH=PhotoImage(file="asset/H/QH.png")
KH=PhotoImage(file="asset/H/KH.png")

AD=PhotoImage(file="asset/D/AD.png")
DOSD=PhotoImage(file="asset/D/2D.png")
TRESD=PhotoImage(file="asset/D/3D.png")
CUATROD=PhotoImage(file="asset/D/4D.png")
CINCOD=PhotoImage(file="asset/D/5D.png")
SEISD=PhotoImage(file="asset/D/6D.png")
SIETED=PhotoImage(file="asset/D/7D.png")
OCHOD=PhotoImage(file="asset/D/8D.png")
NUEVED=PhotoImage(file="asset/D/9D.png")
TD=PhotoImage(file="asset/D/TD.png")
JD=PhotoImage(file="asset/D/JD.png")
QD=PhotoImage(file="asset/D/QD.png")
KD=PhotoImage(file="asset/D/KD.png")

cont=0
Apostado=0
Apuesta_pasada=0
gano=0
me_atrevi=0

Micanvas=Canvas(Raiz, width= 1200, height=700)
Micanvas.pack()

ApuestaVar=StringVar()
MisFichasVar=StringVar()
CantidadApostar=IntVar()

mano=0
manoanterior=0
posicarta=0.5
posicartaC=0.5
casa=0
s_q_casa=0

ApuestaVar.set("0")
MisFichasVar.set("5000")

def borrartodo():
	ApuestaVar.set("0")
	MisFichasVar.set("5000")

def salir():
	respuesta=messagebox.askquestion("Salir", "Salir del Juego")
	if respuesta == "yes":
		Raiz.destroy()

#-------------------------------------------------------------------------------------


BarraMenu=Menu(Raiz)

NuevoMenu=Menu(BarraMenu, tearoff=0)
NuevoMenu.add_command(label="Nuevo", command=inicia)
NuevoMenu.add_command(label="Salir", command=salir)

BarraMenu.add_cascade(label="Menu", menu=NuevoMenu)
BarraMenu.add_command(label="Borrar pantalla", command=borrartodo)

def center(ventana):
	ventana.update_idletasks()
	width= ventana.winfo_width()
	height= ventana.winfo_height()
	x = (ventana.winfo_screenwidth() // 2) - (width // 2)
	y = (ventana.winfo_screenheight() //2) - (height// 2)
	ventana.geometry('{}x{}+{}+{}'.format(width,height,x,y))

Raiz.config(menu=BarraMenu)
Raiz.title("BlackJack")
Etiqueta_fondo=Label(Raiz, image=FondoMesa)
Etiqueta_fondo.place(relwidth=1, relheight=1)
center(Raiz)

Raiz.mainloop()


