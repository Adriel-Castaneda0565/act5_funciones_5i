print("funciones creadas por el usuario")
# las funciones
def Mi_lista():
    print("lista:")
    amigos=["Homero","paty","Lety"]
    for castaneda in amigos:
        print(castaneda)

def Mi_tupla():
    print("\nTupla:")
    rawrs=("rex","estego","spino","raptor")
    for dinos in rawrs:
        print(dinos)

def Mi_conjunto():
    print("\nConjunto:")
    camionetas=("raptor","escalade","tahoe","suburban\n")
    for troquita in camionetas:
        print(troquita)

def Mi_diccionario():
    print("\nDiccionario:")
    ark={
        "Rockdrake":"Aberration",
        "Managarmr":"Extintion",
        "Magmasaur":"Genesis1"
    }
    for mob in ark:
        print(mob)
# LLamadas a funciones
Mi_lista()
Mi_tupla()
Mi_conjunto()
Mi_diccionario()