from math import pow

def validacion_datos(peso_kg, altura_cm):
    if peso_kg <= 0 or altura_cm <= 0:
        return False
    return True

def calcular_imc(peso_kg, altura_cm):
    altura_m = altura_cm / 100
    imc = peso_kg / pow(altura_m, 2)
    return imc