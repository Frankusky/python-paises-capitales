#coding:utf-8
###################	Librerias	#################
import getpass
import smtplib
import time

##################	Clase	####################
class enviarMail(object): #funcion para enviar correo
		def __init__(self, destinatario, cuenta, clave, mensaje):
			self.destinatario = destinatario
			self.cuenta = cuenta
			self.clave = clave
			self.mensaje = mensaje
#		def enviar(self):
			for x in listacorreos:
				try: #intentar mandar el correo
					fromaddr = self.cuenta
					toaddrs  = x
					msg = self.mensaje
					username = self.cuenta
					password = self.clave
					server = smtplib.SMTP('smtp.gmail.com:587')
					server.ehlo()
					server.starttls()
					server.login(username,password)
					server.sendmail(fromaddr, toaddrs, msg)
					server.quit()
					print "Mail enviado con exito a",x,"!"
				except (smtplib.SMTPAuthenticationError): #mostrar error si se fallo validacion de usuario/clave
					print "Error. Su usuario o contrasena es incorrecta"

################### Funciones ########################
def menu():
	print"""
Programa  Generador de Listas de Paises y Capitales manda Correos de Frank  y Brandon
***Mejor conocido por sus iniciales como el PGLPCCF&B (pegeilpececeefeybe)***
		
		
Porfavor, seleccione una opcion, puede elegir usar los numeros o sus nombres:

1. Ingresar pais y capital
2. Mostrar paises
3. Mostrar capitales
4. Mostrar todo
5. Mostrar todo ordenado
6. Enviar correo
7. Cerrar
"""
	opcion = raw_input("Ingrese opcion(1-7): ")
	return opcion
			
def comprobadorNombre(nombre):
	nombrevalido = True
	for x in nombre:
		if x.isalpha()==True or x == " " or x == ".":
			pass
		else:
			nombrevalido = False
	return nombrevalido
		
def listaDeCorreos():
	fincorreos=False
	while(fincorreos==False):
		nuevocorreo = raw_input("Ingrese destinatario: ")
		listacorreos.append(nuevocorreo)
		ingresocorrecto=False
		while (ingresocorrecto == False):
			mascorreos = raw_input("Desea ingresar mas correos? si/no ")
			mascorreos = mascorreos.lower()
			if mascorreos=="si":
				fincorreos = False
				ingresocorrecto=True
			elif mascorreos == "no":
				fincorreos = True
				ingresocorrecto = True
			else:
				print "Respuesta incorrecta. Vuelva a intentarlo."
				
def resetCorreos():
	for x in listacorreos:
		listacorreos.remove(x)

		

###################	Funciones del menu	#################
def enviarCorreo():
	listaDeCorreos()
	cuenta = raw_input("Emisor: ")
	clave = getpass.getpass("Ingrese contraseña: ")
	print "Procesando solicitud... Porfavor espere..."
	mensaje = "Pais\t-\tCapital\n"
	for x in paiscap:
		mensaje = mensaje + str(x) +"\t-\t"+ str(paiscap[x]) + "\n"
	mail = enviarMail(listacorreos, cuenta, clave, mensaje)
	time.sleep(3)

def ingresoPaisCapital():
	ingresofin = False
	while (ingresofin==False):
		pais = raw_input("Ingrese pais: ")
		capital = raw_input("Ingrese capital: ")
		nuevoingreso = pais+capital
		if comprobadorNombre(nuevoingreso)==True:
			print "Realizando ingreso... Porfavor espere..."
			time.sleep(1)
			paiscap[pais.capitalize()]=capital.capitalize()
			print str(pais)+",", capital, "ingresados exitosamente!"
			print "Gracias por agregar un país con su capital"
			time.sleep(1)
			opccorrecto=False
			while(opccorrecto==False):
				fin = raw_input("Desea volver a ingresar? si/no ")
				fin = fin.lower()
				if fin == "si":
					ingresofin = False
					opccorrecto=True
				elif fin == "no":
					ingresofin = True
					opccorrecto=True
				else:
					print "Ingreso invalido. Vuelva a intentarlo."
					opccorrecto=False
		else:
			print "Ingreso incorrecto, vuelva a intentarlo"
			
def mostrarPaises():
	cont=0
	for x in paiscap:
		print x
		cont+=1
	if cont==0:
		print "No se encontro ningun pais!"
	time.sleep(2)

def mostrarCapitales():
	cont = 0
	for x in paiscap:
		print paiscap[x]
		cont+=1
	if cont == 0:
		print "No se encontro ningun capital!"
	time.sleep(2)

def mostrarTodo():
	cont=0
	for x in paiscap:
		print "Pais:", str(x)+". Capital:", paiscap[x]
		cont+=1
	if cont==0:
		print "No se ha ingresado nada para mostrar!"
	time.sleep(2)
	
def ordenado():
	longitud = len(paiscap.values())
	cont = 0
	capordenado = sorted(paiscap.values())
	paisordenado = sorted(paiscap.keys())
	while (cont < longitud):
		print "Capital: "+str(capordenado[cont])+ ". Pais:", paisordenado[cont]
		cont+=1
	time.sleep(2)
####################	Diccionarios	##########################
paiscap = {}
paiscapordenado = {}
listacorreos=[]
####################	Programa inicial	##################

finprograma = False
while(finprograma==False):
	opcion = menu()
	opcion = opcion.lower()
	if (opcion=="1" or opcion=="ingresar pais o capital"):
		ingresoPaisCapital()
	elif (opcion == "2" or opcion == "mostrar paises"):
		mostrarPaises()
	elif (opcion=="3" or opcion == "mostrar capitales"):
		mostrarCapitales()
	elif (opcion=="4" or opcion == "mostrar todo"):
		mostrarTodo()
	elif (opcion == "5" or opcion == "mostrar todo ordenado") :
		ordenado()
	elif opcion=="6" or opcion=="enviar correo":
		resetCorreos()
		enviarCorreo()
	elif opcion=="7" or opcion=="cerrar":
		print "El PGLPCCF&B se esta apagando..."
		time.sleep(3)
		finprograma = True
	else:
		print "Opcion no reconocida. Vuelva a intentarlo"
		time.sleep(2)