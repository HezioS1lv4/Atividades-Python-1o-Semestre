# Hézio

class Minha_Classe:
    def tabuada(valor):
        lista_tabuada = []
        cont = 1
        while cont < 11:
            lista_tabuada.append(valor * cont)
            cont += 1
        return lista_tabuada


C1 = Minha_Classe.tabuada(5)
print(C1)
