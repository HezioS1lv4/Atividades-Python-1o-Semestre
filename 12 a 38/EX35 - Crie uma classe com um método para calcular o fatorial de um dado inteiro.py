# Hézio

class Minha_Classe:
    def fatorial(valor):
        if valor == 1:
            return 1
        resultado = valor*Minha_Classe.fatorial(valor-1)
        return resultado

C1 = Minha_Classe.fatorial(5)
print(C1)
