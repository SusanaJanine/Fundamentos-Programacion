from datetime import datetime
from IMC_Calculos import calcular_imc
from IMC_Recomendaciones import categoria_imc

def menu ():
    print("¡BIENVENIDO A IMC LAB: TU CLÍNICA EXPRESS!")
    print("Por favor elija una opcion: ")
    print("1. Calcular IMC de un paciente")
    print("2. Ver historial e pacientes")
    print("3. Buscar paciente por nombre")
    print("4. Salir")

def guardar_historial (historial, texto):
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    historial.append(f"[{fecha}] {texto}")


if __name__ == "__main__":
    date = datetime.now()
    print("Fecha y hora actual:", date.strftime("%d/%m/%Y %H:%M:%S"))

    historial = []

    opcion = 0
    while opcion != 4:
        menu()
        opcion = int(input("Ingresar opcion: "))
        
        if opcion < 1 or opcion > 4:
            print("Opcion invalida. Por favor seleccione otra opcion.")

        elif opcion == 1:
            print("Has elegido calcular IMC de un paciente")
            nombre = input("Ingrese el nombre del paciente: ")
            edad = int(input("Ingrese la edad del paciente: "))
            n1 = float(input("Favor de ingresar el peso del paciente: "))
            n2 = float(input("Favor de ingresar la altura del paciente: "))
            imc = calcular_imc(n1, n2)
            print(f"El IMC del paciente es: {imc}")
            if imc >= 0 and imc <= 15.99 :
                print ("Delgadez severa")
            elif imc >= 16.00 and imc <= 16.99 :
                print ("Delgadez moderada")
            elif imc >= 17.00 and imc <= 18.49:
                print ("Delgadez leve")
            elif imc >= 18.50 and imc <= 24.99 :
                print ("Normal")
            elif imc >= 25.00 and imc <= 29.99:
                print ("Sobrepeso")
            elif imc >= 30.00 and imc <= 34.99:
                print ("obesidad leve")
            elif imc >= 35.00 and imc <= 39.00:
                print ("obesidad media")
            elif imc >= 40.00:
                print ("obesidad morbida") 
            guardar_historial(historial, f"Nombre: {nombre} Edad: {edad} Peso: {n1} Altura: {n2} IMC: {imc} Categoria: {categoria_imc}")
