from math import pow

def calcular_imc(peso_kg, altura_m):
    imc = peso_kg / pow(altura_m, 2)
    return imc