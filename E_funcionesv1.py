print("Manejo de funciones v1")
def hola_mundo():
    print("Hola aqui estoy")

def Mensa(msg):
    print(msg)
def EscribeNC(Nombre,Apellido):
    print(Nombre,Apellido)
    print(f"Tu nombre completo es: {Nombre} {Apellido}")
def suma2numeros(n1, n2):
    s=n1+n2
    return f"La suma de {n1} y de {n2} es de: ",s
#Llamando a la funcion
hola_mundo()
Mensa("Hola wasap")#Llama a mensa con 1 paramentro
Mensa("El profe me sorprendio enviando mensajes")#llama a mensa con 1 parametro
EscribeNC("Adriel","Castaneda")
print("Funcions que regresan valores")
print(suma2numeros(7, 3))
print(suma2numeros(15,45))