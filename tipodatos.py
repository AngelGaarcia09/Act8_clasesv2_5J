print(" Clases v2 Angel Garcia")
# zona de clase
class Datos:
    # el constructor funcion
    def __init__(self,estatura,peso):
        self.estatura = estatura
        self.peso = peso

    def mostrar_datos(self):
        print(f"Estatura {self.estatura}: mts, Peso {self.peso} kg")

    def mi_lista(self):
        vaquero = ["botas", "sombrero", "cinto"]
        print(vaquero)
        for vaquero in vaquero:
            print(vaquero)
        
    def mi_tupla(self):
        Trailer = ("Kenword", "Volvo", "Peterbil")
        print(Trailer)
        for Trailer in Trailer:
            print(Trailer)

    def mi_set(self):
        perfumes = {"Nautica", "Hugo Bos", "Carolina Real"}
        print(perfumes)
        for perfumes in perfumes:
            print(perfumes)

    def mi_diccionario(self):
        nombres= thisdict = {
        "Nombre": "Angel",
        "Apellido": "Garcia",
        "Edad": 2007
}
        print(nombres)
        for x, y in nombres.items():
            print(x, y) 

# creacion de objeto info
info=Datos(1.79 ,70)

# utilizando el obj. --> info
info.mostrar_datos()

print("Lista de Datos, Angel Garcia ")
info.mi_lista()

print("tupla de trailer Angel Garcia ")
info.mi_tupla()

print("Conjuntos de perfumes Angel Garcia ")
info.mi_set()

print("Diccionarios de nombres Angel Garcia ")
info.mi_diccionario()







