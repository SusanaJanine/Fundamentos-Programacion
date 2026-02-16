from calculadora import suma, resta, multiplicacion, division
from utilidades import fahrenheit_celsius, km_millas, lbs_kg, m_km, cm_m, hrs_minutos, pies_cm
from datetime import datetime
from math import sqrt, pow, log, exp, tan, cos, sin, radians

def menu ():
    print("¡BIENVENIDO A LA CALCULADORA MÁGICA!")
    print("Por favor elija una opcion: ")
    print("Operaciones Matematicas Basicas")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Raiz cuadrada")
    print("6. Potencia")
    print("7. Logaritmo")
    print("8. Exponencial")
    print("Conversiones")
    print("9. Km a Millas")
    print("10. Fahrenheit a celsius")
    print("11. Lbs a Kg")
    print("12. Mts a Km")
    print("13. Cm a Mts")
    print("14. Hrs a Min")
    print("15. Pie a Cm")
    print("Funciones Trigonometricas")
    print("16. Tangente")
    print("17. Seno")
    print("18. Coseno")
    print("Operaciones Avanzadas")
    print("19. Area rectangulo")
    print("20. Area circulo")
    print("21. Combo suma + raiz cuadrada")
    print("22. Salida")

if __name__ == "__main__":
    date= datetime.now() # Se obtiene la fecha y hora actual
    print("Fecha y hora actual:", date.strftime("%d/%m/%Y %H:%M:%S")) # Se muestra la fecha y hora actual

    opcion = 0
    while opcion != 15: # El programa se ejecuta hasta que el usuario elija la opcion 15 para salir
        menu() # Se manda a llamar la funcion "menu" para mostrarle las opciones al usuario
        opcion = int(input("Ingresar opcion: ")) # Solicitar al usuario una opcion
        
        if opcion < 1 or opcion > 15: # Verificar que la opcion elegida sea valida
            print("Opcion incorrecta, seleccione otra opcion")

        elif opcion == 1:
            print("Has elegido el camino de la suma")
            n1 = int(input("Favor de ingresar el primer numero a sumar: "))
            n2 = int(input("Favor de ingresar el segundo numero a sumar: "))
            print(f"El resultado de la suma es: {suma(n1, n2)}") # Se muestra el resultado de la suma.
            
        elif opcion == 2:
            print("Has elegido el camino de la resta")
            n1 = int(input("Favor de ingresar el primer numero a restar: "))
            n2 = int(input("Favor de ingresar el segundo numero a restar: "))
            print(f"El resultado de la resta es: {resta(n1, n2)}") # Se muestra el resultado de la resta.

        elif opcion == 3:
            print("Has elegido el camino de la multiplicacion")
            n1 = int(input("Favor de ingresar el primer numero a multiplicar: "))
            n2 = int(input("Favor de ingresar el segundo numero a multiplicar: "))
            print(f"El resultado de la multiplicacion es: {multiplicacion(n1, n2)}") # Se muestra el resultado de la multiplicacion.
            
        elif opcion == 4:
            print("Has elegido el camino de la division")
            n1 = float(input("Favor de ingresar el primer numero a dividir: "))
            n2 = float(input("Favor de ingresar el segundo numero a dividir: "))
            print(f"El resultado de la division es: {division(n1, n2):.4f}") # Se muestra el resultado de la division con 4 decimales
        
        elif opcion == 5:
            print("Has elegido el camino de la raiz cuadrada")
            n1 = float(input("Favor de ingresar el numero para sacar su raiz cuadrada: "))
            print(f"El resultado de la raiz cuadrada es: {sqrt(n1):.4f}") # Se muestra el resultado de la raiz cuadrada con 4 decimales
        
        elif opcion == 6:
            print("Has elegido el camino de la potencia")
            n1 = float(input("Favor de ingresar el numero base: "))
            n2 = float(input("Favor de ingresar el numero exponente: "))
            print(f"El resultado de la potencia es: {pow(n1, n2)}") # Se muestra el resultado de la potencia sin decimales porque la funcion "pow" devuelve un numero entero si el resultado es un numero entero, y un numero decimal si el resultado es un numero decimal. Por lo tanto, no es necesario mostrar el resultado con decimales.
        
        elif opcion == 7:
            print("Has elegido el camino del logaritmo")
            n1 = float(input("Favor de ingresar el numero para sacar su logaritmo: "))
            print(f"El resultado del logaritmo es: {log(n1):.4f}") # Se muestra el resultado del logaritmo con 4 decimales
        
        elif opcion == 8:
            print("Has elegido el camino de la exponencial")
            n1 = float(input("Favor de ingresar el numero para sacar su exponencial: "))
            print(f"El resultado de la exponencial es: {exp(n1):.4f}") # Se muestra el resultado de la exponencial con 4 decimales
            
        elif opcion == 9:
            print("Has elegido la conversion de km a millas: ")
            n1 = float(input("Favor de ingresar los km: "))
            print(f"El resultado de los km a millas es: {km_millas(n1)}") # Se muestra el resultado de la conversion de km a millas.

        elif opcion == 10:
            print("Has elegido la conversion de fahrenheit a celsius")
            n1 = float(input("Favor de ingresar el numero de los fahrenheit: "))
            print(f"El resultado de los fahrenheit a celsius es: {fahrenheit_celsius(n1)}") # Se muestra el resultado de la conversion de fahrenheit a celsius.

        elif opcion == 11:
            print("Has elegido la conversion de Lbs a Kg")
            n1 = float(input("Favor de ingresar la cantidad de las Lbs: "))
            print(f"El resultado de la conversion Lbs a Kg es: {lbs_kg(n1)}")

        elif opcion == 12:
            print("Has elegido la conversion de Mts a Km")
            n1 = float(input("Favor de ingresar la cantidad de los Mts: "))
            print(f"El resultado de la conversion Mts a Km es: {m_km(n1)}")

        elif opcion == 13:
            print("Has elegido la conversion de Cm a Mts")
            n1 = float(input("Favor de ingresar la cantidad de los Cm: "))
            print(f"El resultado de la conversion Cm a Mts es: {cm_m(n1)}")
        
        elif opcion == 14:
            print("Has elegido la conversion de Hrs a Min")
            n1 = float(input("Favor de ingresar la cantidad de las Hrs: "))
            print(f"El resultado de la conversion Hrs a Min es: {hrs_minutos(n1)}")

        elif opcion == 15:
            print("Has elegido la conversion de Pie a Cm")
            n1 = float(input("Favor de ingresar la cantidad de : "))
            print(f"El resultado de la conversion Pie a Cm es: {pies_cm(n1)}")
        
# Para las opciones 1, se solicita al usuario un numero pero primero se convierte ese numero a radianes. Porque las funciones trigonometricas en python trabajan con radianes, por lo que es necesario convertir el numero ingresado a radianes.
        elif opcion == 16:
            print("Has elegido el camino de la tangente")
            n1 = float(input("Favor de ingresar el numero para sacar su tangente: "))
            rad = radians(n1) # Se convierte el numero ingresado a radianes para poder calcular su tangente
            print(f"El resultado de la tangente es: {tan(rad):.4f}") # Se muestra el resultado de la tangente con 4 decimales
            
        elif opcion == 17:
            print("Has elegido el camino del seno")
            n1 = float(input("Favor de ingresar el numero para sacar su seno: "))
            rad = radians(n1) # Se convierte el numero ingresado a radianes para poder calcular su seno
            print(f"El resultado del seno es: {sin(rad):.4f}") # Se muestra el resultado del seno con 4 decimales

        elif opcion == 18:
            print("Has elegido el camino del coseno")
            n1 = float(input("Favor de ingresar el numero para sacar su coseno: "))
            rad = radians(n1) # Se convierte el numero ingresado a radianes para poder calcular su coseno
            print(f"El resultado del coseno es: {cos(rad):.4f}") # Se muestra el resultado del coseno con 4 decimales
        
        elif opcion == 19:
            print("Has elegido el camino para encontrar el Area del Rectangulo")
            n1 = float(input("Favor de ingresar :"))
            n2 = float(input("Favor de ingresar :"))
            print(f"El resultado de las lbs a kg es: {(n1)}")

        elif opcion == 20:
            print("Has elegido el camino del Area del Circulo")
            n1 = float(input("Favor de ingresar las lbs:"))
            print(f"El resultado de las lbs a kg es: {lbs_kg(n1)}")

        elif opcion == 21: # Esta opcion permite realizar dos operaciones al mismo tiempo, primero se haria la suma de dos numeros y posteriormente se sacaria la raiz cuadrada de esos dos numeros.
            print ("Has elegido el modo combo suma + raiz cuadrada")
            n1 = int(input("Favor de ingresar el primer numero a sumar: "))
            n2 = int(input("Favor de ingresar el segundo numero a sumar: "))
            resultado_suma = suma(n1,n2)
            print(f"El resultado de la suma es: {suma(n1, n2)} y la raiz cuadrada del resultado es: {sqrt(resultado_suma)}") 

        elif opcion == 22: # Si el usuario elige la opcion 14, el programa se termina.
            print("Has elegido salir")