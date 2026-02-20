from datetime import datetime
from IMC_Calculos import calcular_imc, validacion_datos
from IMC_Recomendaciones import categoria_imc, recomendacion_por_categoria

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
            nombre = input("Nombre del paciente: ")
            edad = int(input("Edad del paciente: "))
            while True:
                try:
                    n1 = float(input("Peso del paciente (kg): "))
                    n2 = float(input("Altura del paciente (cm): "))
                    if validacion_datos(n1, n2):
                        imc = round(calcular_imc(n1, n2))
                        categoria = categoria_imc(imc)
                        recomendacion = recomendacion_por_categoria(categoria)
                        break
                    else:
                        print("El peso y la altura deben ser mayores de 0")
                except ValueError:
                    print("Ingresa un numero valido")
                    
            print(f"El IMC del paciente es: {imc}")
            print(f"Categoria: {categoria}")
            print(f"Recomendacion: {recomendacion}")
            guardar_historial(historial, f"Paciente: {nombre} Edad: {edad}años Peso: {n1}kg  Altura: {n2}cm  IMC: {imc:.2f}  Categoria: {categoria}") 
        
