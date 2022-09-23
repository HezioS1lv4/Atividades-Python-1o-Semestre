# Hézio

class Minha_Classe:
    def menor(lista):
        menor_valor = lista[0]
        for n in range(len(lista)):
            if lista[n] < menor_valor:
                menor_valor = lista[n]
        return menor_valor

minha_lista = [2, -3, 54, 87, -96, 5, 12]
C1 = Minha_Classe.menor(minha_lista)
print(C1)
