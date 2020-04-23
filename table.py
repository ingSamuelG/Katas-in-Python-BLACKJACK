from tkinter import *
from tkinter import messagebox
from funciones import construir_maso, pedir_carta, dame_valor, decide, valor_idividual

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
	posicartaC=0.5
	me_atrevi=0
	ya_lei_AS_C=0
	ya_lei_AS=0
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

	if int(MisFichasVar.get())<=0:
		perdiste()
	
	else:

		cont=0
		Apostado=0

		def crear_label_Carta(carta, x, y):
			carta=Label(Raiz, image=eval(carta))
			carta.place(relx=x, rely=y, relheight=0.136 ,relwidth=0.06)



		def dibujar_carta(jugador):
			global maso
			global casa
			global posicartaC
			global posicarta
			global ya_lei_AS
			global ya_lei_AS_C
			global mano

			nuevo_set=pedir_carta(maso)
			cartaNueva=nuevo_set[0]
			maso=nuevo_set[1]
			nueva_pedida=valor_idividual(cartaNueva)

			if jugador == casa:
				if carta3.startswith("A") or carta4.startswith("A") or cartaNueva.startswith("A") and ya_lei_AS_C==0:
					if casa+nueva_pedida>22:
						casa=(casa+nueva_pedida)-10
						ya_lei_AS=1
				elif casa+nueva_pedida>22 and cartaNueva.startswith("A") and ya_lei_AS==1:
					casa+=1
				else:
					casa+=nueva_pedida
					print("aqui entre")

				print(casa)
				posicartaC-=0.03
				crear_label_Carta(cartaNueva,posicartaC,0.3)

			else:
				if carta1.startswith("A") or carta2.startswith("A") or cartaNueva.startswith("A") and ya_lei_AS==0:
					if mano+nueva_pedida>22:
						mano=(mano+nueva_pedida)-10
						ya_lei_AS=1

				elif mano+nueva_pedida>22 and cartaNueva.startswith("A") and ya_lei_AS==1:
					mano+=1

				else:
					mano+=nueva_pedida

				posicarta-=0.03
				crear_label_Carta(cartaNueva,posicarta,0.5)


		def evalua_jugada(jugador):
			global casa
			global gano
			global Apostado

			if jugador==casa:
				if casa>=22:
					print(casa)
					messagebox.showwarning("Ganaste", "La casa se paso")
					gano+=1
					inicia(Apostado)
				elif casa==21:
					print(casa)
					messagebox.showwarning("Perdiste", "BlackJack de la casa")
					inicia(Apostado)
			else:
				if mano>=22:
					messagebox.showwarning("Perdiste", "Te pasaste del BlackJack")
					ApuestaVar.set("0")
					inicia(Apostado)
				elif mano==21:
					messagebox.showwarning("Ganaste", "BlackJack")
					gano=1
					inicia(Apostado)


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
				dibujar_carta(casa)
				evalua_jugada(casa)
				print("Pedi la carta")
				
			elif casa in range(15,17):

				print("Me atrevi a juagar")

				if decide()==True:
					dibujar_carta(casa)
					evalua_jugada(casa)
					print("jugue",casa)
					
				else:
					s_q_casa=1
					print("me quede")
						
			elif casa in range(18,21):
				print("me quedare")
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

			valorMano=dame_valor(carta1,carta2)
			valorCasa=dame_valor(carta3,carta4)

			if Apuesta.startswith("-"):
				sinMenos=Apuesta[1:]
			else:
				sinMenos=Apuesta

			Apostado=int(sinMenos)

			if casa<22 or mano< 22:
				if  int(sinMenos) > 0 and cont==0:
					cont+=1
					Apuesta_pasada=int(sinMenos)

					crear_label_Carta(carta1,0.5,0.75)
					crear_label_Carta(carta2,0.435,0.75)
					crear_label_Carta(carta3,0.5,0.1)
					crear_label_Carta(carta4,0.435,0.1)

					mano=valorMano
					casa= valorCasa

					if mano==21:
						messagebox.showinfo("Ganaste","BlackJack")
						gano=1
						inicia(Apostado)
					elif casa==21:
						messagebox.showinfo("Perdiste","BlackJack de la casa")
						inicia(Apostado)

					else:
						computadora_play()

				elif cont==1 and Apuesta_pasada!=Apostado:
					respuesta=messagebox.askquestion("Dooooooobleeeeee","en esta fase solo puedes apostar el doble deseas Hacerlo?")
					if respuesta =="yes":
						
						dibujar_carta(mano)

						if mano>=22:
							messagebox.showwarning("Perdiste", "Te pasaste del BlackJack")
							ApuestaVar.set("0")
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
					dibujar_carta(mano)
					evalua_jugada(mano)
					computadora_play()
				else:
					messagebox.showinfo("Apuesta", "No has apostado nada")
			else:
				inicia(Apostado)

			print("turno :", cont)
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



	#_______________________________Fin de Las Funciones de juego___________________________________________________________

	#______________________________Botones de Jugar_________________________________________________________________


		Boton_rojo=Button(Raiz,image=ImagenBotonRojo, command=quedarse)
		Boton_rojo.config(bd=0, bg="#8c2027",activebackground="#8c2027")
		Boton_rojo.place(relx=0.8, rely=0.85,relheight=0.15, relwidth=0.08)

		Boton_verde=Button(Raiz,image=ImagenBotonVerde, command=defiene_apuesta)
		Boton_verde.config(bd=0, bg="#a01c1f",activebackground="#a01c1f")
		Boton_verde.place(relx=0.7, rely=0.75,relheight=0.15, relwidth=0.088)

		Boton_Juega=Button(Raiz,image=ImagenBotonJuega, command= lambda:jugar(carta1,carta2,carta3,carta4, ApuestaVar.get()))
		Boton_Juega.config(bd=0, bg="#a01c1f",activebackground="#a01c1f")
		Boton_Juega.place(relx=0.75, rely=0.6,relheight=0.15, relwidth=0.088)

	#_____________________________Pantallas de Score__________________________________________________________________________________________

		MisFichas=Entry(textvariable=MisFichasVar ,font=("NI7seg",18),justify="right", cursor="pirate" , state=DISABLED,disabledbackground="black", disabledforeground="#03f943")
		MisFichas.place(relx=0.13, rely= 0.63, relheight=0.05, relwidth=0.1)

		ApuestaPantalla=Entry(textvariable=ApuestaVar ,font=("NI7seg",18),justify="right", cursor="pirate", state=DISABLED,disabledbackground="black", disabledforeground="red")
		ApuestaPantalla.place(relx=0.13, rely= 0.68, relheight=0.05, relwidth=0.1)

	#----------------------Fichas------------------------------------------------------------------------------------------------

		EtiquetaF10=Label(Raiz, image=imagenF10, bg="#88202a")
		EtiquetaF10.place(relx=0.05, rely= 0.75, relheight=0.1, relwidth=0.05)

		ficha10=Radiobutton(Raiz, text="10", value=10, variable=CantidadApostar,font=("Casino","20"),bg="#88202a", activebackground="#8c2027", cursor="hand2")
		ficha10.select()
		ficha10.place(relx=0.068, rely=0.85, relheight=0.035 ,relwidth=0.045)

		EtiquetaF50=Label(Raiz, image=imagenF50, bg="#941b22")
		EtiquetaF50.place(relx=0.120, rely= 0.75, relheight=0.09, relwidth=0.05)

		ficha50=Radiobutton(Raiz, text="40", value=50, variable=CantidadApostar,font=("Casino","20"), bg="#88202a", activebackground="#8c2027", cursor="hand2") #the font that im using have a bug that takes the character 4 for 5 and vice versa#
		ficha50.place(relx=0.14, rely=0.85, relheight=0.035 ,relwidth=0.045)

		EtiquetaF100=Label(Raiz, image=imagenF100, bg="#a31d24")
		EtiquetaF100.place(relx=0.192, rely= 0.75, relheight=0.1, relwidth=0.05)

		ficha100=Radiobutton(Raiz, text="100", value=100, variable=CantidadApostar, font=("Casino","20"), bg="#9f1f24",activebackground="#9f1f24",cursor="hand2")
		ficha100.place(relx=0.21, rely=0.85, relheight=0.035 ,relwidth=0.06)

		EtiquetaF500=Label(Raiz, image=imagenF500, bg="#a31d24")
		EtiquetaF500.place(relx=0.26, rely= 0.75, relheight=0.09, relwidth=0.05)

		ficha500=Radiobutton(Raiz, text="400", value=500, variable=CantidadApostar , font=("Casino","20"), bg="#a21e22", activebackground="#a21e22",cursor="hand2") #the font that im using have a bug that takes the character 4 for 5 and vice versa#
		ficha500.place(relx=0.28, rely=0.85, relheight=0.035 ,relwidth=0.06)	

def perdiste():
	Etiqueta_fondo=Label(Raiz, image=FondoMesa)
	Etiqueta_fondo.place(relwidth=1, relheight=1)

	EtiquetaPerdiste=Label(Etiqueta_fondo,text= "Perdiste todas tus fichas",font=("Casino", 50), bg="#af1f24")
	EtiquetaPerdiste.place(relx=0.15,rely=0.05)

	Boton_rojo=Button(Raiz,image=ImagenBotonSa, command=salir)
	Boton_rojo.config(bd=0, bg="#a01c1f",activebackground="#8c2027")
	Boton_rojo.place(relx=0.5, rely=0.85,relheight=0.15, relwidth=0.08)

# __________________________________Fin de las Fichas_____________________________________________________________________________________________________________________________________________________________________________________________________________




# ___________________________________________Inicio del main windows_________________________________________________________________________________________________________________________________________________________________


Raiz= Tk()

#_________________________imagenes________________________________________

FondoMesa=PhotoImage(file="asset/table.png")
ImagenBotonRojo=PhotoImage(file="asset/botones/botonr.png")
ImagenBotonVerde=PhotoImage(file="asset/botones/botonv.png")
ImagenBotonJuega=PhotoImage(file="asset/botones/botonp.png")

ImagenBotonS=PhotoImage(file="asset/botones/botonS.png")
ImagenBotonSa=PhotoImage(file="asset/botones/botonSa.png")

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

#_________________________fin de las imagenes____________________________________________________

#_________________________Variables_______________________________________________________________

cont=0
Apostado=0
Apuesta_pasada=0
gano=0
me_atrevi=0
ya_lei_AS_C=0
ya_lei_AS=0

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

#_________________________Funciones de ventanas______________________

def borrartodo():
	ApuestaVar.set("0")
	MisFichasVar.set("5000")

def salir():
	respuesta=messagebox.askquestion("Salir", "Salir del Juego")
	if respuesta == "yes":
		Raiz.destroy()


#_________________________fin de las funciones de ventana_______________________________________________________________________________

#_________________________Menu__________________________________________


BarraMenu=Menu(Raiz)

NuevoMenu=Menu(BarraMenu, tearoff=0)
NuevoMenu.add_command(label="Nuevo", command=inicia)
NuevoMenu.add_command(label="Salir", command=salir)

BarraMenu.add_cascade(label="Menu", menu=NuevoMenu)
BarraMenu.add_command(label="Borrar pantalla", command=borrartodo)

#____________________Fin del menu_________________________________________

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


