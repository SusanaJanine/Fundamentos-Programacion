from calculadora import suma, resta, multiplicacion, division
from utilidades import fahrenheit_celsius, km_millas, lbs_kg, m_km, cm_m, hrs_minutos, pies_cm
from datetime import datetime
from math import sqrt, pow, log, exp, tan, cos, sin, radians, pi

def menu ():
    print("¡BIENVENIDO A LA CALCULADORA MÁGICA!")
    print("Por favor elija una opcion: ")
    print("--- Operaciones Matematicas Basicas ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("--- Operaciones Avanzadas ---")
    print("5. Raiz cuadrada")
    print("6. Potencia")
    print("7. Logaritmo")
    print("8. Exponencial")
    print("--- Conversiones ---")
    print("9. Km a Millas")
    print("10. Fahrenheit a celsius")
    print("11. Lbs a Kg")
    print("12. Mts a Km")
    print("13. Cm a Mts")
    print("14. Hrs a Min")
    print("15. Ft a Cm")
    print("--- Funciones Trigonometricas ---")
    print("16. Tangente")
    print("17. Seno")
    print("18. Coseno")
    print("--- Funciones extras ---")
    print("19. Area rectangulo")
    print("20. Area circulo")
    print("21. Combo suma + raiz cuadrada")
    print("22. Modo Mision (Terreno)")
    print("----------------------")
    print("23. Ver historial")
    print("24. Salida")

def guardar_historial (historial, texto):
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    historial.append(f"[{fecha}] {texto}") # Crea el formato para el historial


if __name__ == "__main__":
    date = datetime.now() # Se obtiene la fecha y hora actual
    print("Fecha y hora actual:", date.strftime("%d/%m/%Y %H:%M:%S")) # Se muestra la fecha y hora actual

    historial = [] # Permite crear un historial que no se elimine.

    opcion = 0
    while opcion != 24: # El programa se ejecuta hasta que el usuario elija la opcion 24 para salir
        menu() # Se manda a llamar la funcion "menu" para mostrarle las opciones al usuario
        opcion = int(input("Ingresar opcion: ")) # Solicitar al usuario una opcion
        
        if opcion < 1 or opcion > 24: # Verificar que la opcion elegida sea valida
            print("Opcion incorrecta, seleccione otra opcion")

# Opcion definida para realizar operaciones de suma.
        elif opcion == 1:
            print("Has elegido el camino de la suma")
            n1 = int(input("Favor de ingresar el primer numero a sumar: "))
            n2 = int(input("Favor de ingresar el segundo numero a sumar: "))
            print(f"El resultado de la suma es: {suma(n1, n2)}") # Se muestra el resultado de la suma.
            guardar_historial(historial, f"Suma: {n1} + {n2} = {suma(n1, n2)}")

# Esta opcion permite realizar operaciones de resta.
        elif opcion == 2:
            print("Has elegido el camino de la resta")
            n1 = int(input("Favor de ingresar el primer numero a restar: "))
            n2 = int(input("Favor de ingresar el segundo numero a restar: "))
            print(f"El resultado de la resta es: {resta(n1, n2)}") # Se muestra el resultado de la resta.
            guardar_historial(historial, f"Resta: {n1} - {n2} = {resta(n1, n2)}")

        elif opcion == 3:
            print("Has elegido el camino de la multiplicacion")
            n1 = int(input("Favor de ingresar el primer numero a multiplicar: "))
            n2 = int(input("Favor de ingresar el segundo numero a multiplicar: "))
            print(f"El resultado de la multiplicacion es: {multiplicacion(n1, n2)}") # Se muestra el resultado de la multiplicacion.
            guardar_historial(historial, f"Multiplicacion: {n1} x {n2} = {multiplicacion(n1, n2)}")
            
        elif opcion == 4:
            print("Has elegido el camino de la division")
            while True:
                try:
                    n1 = float(input("Favor de ingresar el primer numero a dividir: "))
                    break
                except ValueError: # Funciona para que el programa no se rompa y continue, permitiendole al usuario ingresar un numero valido.
                    print("No se puede dividir entre 0. Intenta con otro numero")
            while True:
                try:
                    n2 = float(input("Favor de ingresar el segundo numero a dividir: "))
                    if n2 == 0:
                        print("No se puede dividir entre 0. Intenta con otro numero")
                    else:
                        break
                except ValueError: # Funciona para que el programa no se rompa y permita al usuario ingresar nuevamente un numero valido.
                    print("Invalido. Intenta con otro numero")
            print(f"El resultado de la division es: {division(n1, n2):.1f}") # Se muestra el resultado de la division con 4 decimales
            guardar_historial(historial, f"Division: {n1} / {n2} = {division(n1, n2):.1f}")
        
        elif opcion == 5:
            print("Has elegido el camino de la raiz cuadrada")
            while True:
                try:
                    n1 = float(input("Favor de ingresar el numero para sacar su raiz cuadrada: "))
                    if n1 < 0:
                        print("No se puede calcular la raiz cuadrada en numeros negativos.")
                    else:
                        break
                except ValueError: # Funciona para que el programa no se rompa y continue
                    print("Invalido, ingresa un numero: ")
            print(f"El resultado de la raiz cuadrada es: {sqrt(n1):.4f}") # Se muestra el resultado de la raiz cuadrada con 4 decimales
            guardar_historial(historial, f"Raiz cuadrada: {n1} = {sqrt(n1):.4f}")
        
        elif opcion == 6:
            print("Has elegido el camino de la potencia")
            n1 = float(input("Favor de ingresar el numero base: "))
            n2 = float(input("Favor de ingresar el numero exponente: "))
            print(f"El resultado de la potencia es: {pow(n1, n2)}") # Se muestra el resultado de la potencia sin decimales porque la funcion "pow" devuelve un numero entero si el resultado es un numero entero, y un numero decimal si el resultado es un numero decimal. Por lo tanto, no es necesario mostrar el resultado con decimales.
            guardar_historial(historial, f"Potencia: {n1} ^ {n2} = {pow(n1, n2)}")

        elif opcion == 7:
            print("Has elegido el camino del logaritmo")
            n1 = float(input("Favor de ingresar el numero para sacar su logaritmo: "))
            print(f"El resultado del logaritmo es: {log(n1):.4f}") # Se muestra el resultado del logaritmo con 4 decimales
            guardar_historial(historial, f"Logaritmo: Log{n1} = {log(n1):.4f}")

        elif opcion == 8:
            print("Has elegido el camino de la exponencial")
            n1 = float(input("Favor de ingresar el numero para sacar su exponencial: "))
            print(f"El resultado de la exponencial es: {exp(n1):.4f}") # Se muestra el resultado de la exponencial con 4 decimales
            guardar_historial(historial, f"Exponencial: {n1} = {exp(n1):.4f}")

        elif opcion == 9:
            print("Has elegido la conversion de km a millas: ")
            n1 = float(input("Favor de ingresar los km: "))
            print(f"El resultado de los km a millas es: {km_millas(n1)}") # Se muestra el resultado de la conversion de km a millas.
            guardar_historial(historial, f"Km a Mph: {n1}km = {km_millas(n1):.4f}mph")

        elif opcion == 10:
            print("Has elegido la conversion de fahrenheit a celsius")
            n1 = float(input("Favor de ingresar el numero de los fahrenheit: "))
            print(f"El resultado de la conversion fahrenheit a celsius es: {fahrenheit_celsius(n1)}°C") # Se muestra el resultado de la conversion de fahrenheit a celsius.
            guardar_historial(historial, f"Fahrenheit a Celsius: {n1}°F = {fahrenheit_celsius(n1)}°C")

        elif opcion == 11:
            print("Has elegido la conversion de Lbs a Kg")
            n1 = float(input("Favor de ingresar la cantidad de las Lbs: "))
            print(f"El resultado de la conversion de Lbs a Kg es: {lbs_kg(n1):.2f}kg")
            guardar_historial(historial, f"Lbs a Kg: {n1}lbs = {lbs_kg(n1):.2f}kg")

        elif opcion == 12:
            print("Has elegido la conversion de Mts a Km")
            n1 = float(input("Favor de ingresar la cantidad de los Mts: "))
            print(f"El resultado de la conversion Mts a Km es: {m_km(n1):.4f}km")
            guardar_historial(historial, f"Mts a Km: {n1}mts = {m_km(n1):.4f}km")

        elif opcion == 13:
            print("Has elegido la conversion de Cm a Mts")
            n1 = float(input("Favor de ingresar la cantidad de los Cm: "))
            print(f"El resultado de la conversion Cm a Mts es: {cm_m(n1)}mts")
            guardar_historial(historial, f"Cm a Mts: {n1}cm = {cm_m(n1)}mts")

        elif opcion == 14:
            print("Has elegido la conversion de Hrs a Min")
            n1 = float(input("Favor de ingresar la cantidad de las Hrs: "))
            print(f"El resultado de la conversion Hrs a Min es: {hrs_minutos(n1):.1f}min")
            guardar_historial(historial, f"Hrs a Min: {n1}hrs = {hrs_minutos(n1):.1f}min")

        elif opcion == 15:
            print("Has elegido la conversion de Ft a Cm")
            n1 = float(input("Favor de ingresar la cantidad de : "))
            print(f"El resultado de la conversion Ft a Cm es: {pies_cm(n1):.2f}cm")
            guardar_historial(historial, f"Ft a Cm: {n1}ft = {pies_cm(n1):.2f}cm")

# Para las opciones 16, 17 y 18 se solicita al usuario un numero pero primero se convierte ese numero a radianes. Porque las funciones trigonometricas en python trabajan con radianes, por lo que es necesario convertir el numero ingresado a radianes.

# Opcion que permite calcular la tangente de un numero, mediante el uso de radiantes, el resultado puede no ser un numero exacto pero si cercano.  
        elif opcion == 16:
            print("Has elegido el camino de la tangente")
            n1 = float(input("Favor de ingresar el numero para sacar su tangente: "))
            rad = radians(n1) # Se convierte el numero ingresado a radianes para poder calcular su tangente
            print(f"El resultado de la tangente es: {tan(rad):.4f}") # Se muestra el resultado de la tangente con 4 decimales
            guardar_historial(historial, f"Tangente: Tan{n1} = {tan(rad):.4f}")

# Opcion que permite calcular el seno de un numero, mediante el uso de radiantes.
        elif opcion == 17:
            print("Has elegido el camino del seno")
            n1 = float(input("Favor de ingresar el numero para sacar su seno: "))
            rad = radians(n1) # Se convierte el numero ingresado a radianes para poder calcular su seno
            print(f"El resultado del seno es: {sin(rad):.4f}") # Se muestra el resultado del seno con 4 decimales
            guardar_historial(historial, f"Seno: Sin{n1} = {sin(rad):.4f}")

# Opcion que permite calcular el coseno de un numero, mediante el uso de radiantes
        elif opcion == 18:
            print("Has elegido el camino del coseno")
            n1 = float(input("Favor de ingresar el numero para sacar su coseno: "))
            rad = radians(n1) # Se convierte el numero ingresado a radianes para poder calcular su coseno
            print(f"El resultado del coseno es: {cos(rad):.4f}") # Se muestra el resultado del coseno con 4 decimales
            guardar_historial(historial, f"Coseno: cos{n1} = {cos(rad):.4f}")

# Esta opcion permite calcular el area de un rectangulo
        elif opcion == 19:
            print("Has elegido el camino para calcular el Area de un Rectangulo")
            n1 = float(input("Favor de ingresar la base del rectangulo:"))
            n2 = float(input("Favor de ingresar la altura del rectangulo :"))
            print(f"El area del rectangulo es: {multiplicacion(n1, n2)}")
            guardar_historial(historial, f"Area de un Rectangulo: {n1}b * {n2}h = {multiplicacion(n1, n2):.2f}")

# Esta opcion permite calcular el área de un circulo.
        elif opcion == 20:
            print("Has elegido el camino para calcular el Area de un Circulo")
            n1 = float(input("Favor de ingresa el radio del circulo:"))
            print(f"El area del circulo es: {pi * (n1**2):.4f}")
            guardar_historial(historial, f"Area de un Circulo: {n1} x {pi} = {pi * (n1**2):.4f}")

# Esta opcion permite realizar dos operaciones al mismo tiempo, primero se haria la suma de dos numeros y posteriormente se sacaria la raiz cuadrada de esos dos numeros.
        elif opcion == 21:
            print ("Has elegido el modo combo suma + raiz cuadrada")
            n1 = int(input("Favor de ingresar el primer numero a sumar: "))
            n2 = int(input("Favor de ingresar el segundo numero a sumar: "))
            resultado_suma = suma(n1,n2)
            print(f"El resultado de la suma es: {suma(n1, n2)} y la raiz cuadrada del resultado es: {sqrt(resultado_suma)}") 
            guardar_historial(historial, f"Suma: {n1} + {n2} = {suma(n1, n2)} y Raiz cuadrada: √{suma(n1, n2)} = {sqrt(resultado_suma)}")

# Esta es un opcion que determina el area y el precio total de un terreno
        elif opcion == 22:
            print("Has elegido el Modo Mision (Terreno)")
            while True:
                try:
                    n1 = float(input("Favor de ingresar el ancho del terreno: "))
                    if n1 <= 0:
                        print("No se pueden calcular numeros negativos. Intente con otro numero.")
                    else:
                        break
                except ValueError:
                    print("Invalido, ingrese otro numero")
            while True:
                try:  
                    n2 = float(input("Favor de ingresar el largo del terreno: "))
                    if n2 <= 0:
                        print("No se pueden calcular numeros negativos. Intente con otro numero.")
                    else:
                        break
                except ValueError:
                    print("Invalido, ingrese otro numero")
            while True:
                try:        
                    n3 = float(input("Por favor ingrese el precio por metro cuadrado: "))
                    if n3 <= 0:
                        print("No se pueden calcular numeros negativos. Intente con otro numero.")
                    else:
                        break
                except ValueError:
                    print("Invalido, ingrese otro numero")
            area = multiplicacion(n1, n2)
            print(f"Área del terreno: {multiplicacion(n1,n2):.4f}m² Precio total: ${multiplicacion(area, n3):.2f} ")
            guardar_historial(historial, f"Modo Mision (Terreno): Area = {n1} x {n2} = {multiplicacion(n1, n2)} Precio total = ${multiplicacion(area, n3):.2f}")

# Opcion creada para obtener el historial de las operaciones y funciones utilizadas
        elif opcion == 23:
            print("--- Historial ---")
            if historial:
                for registro in historial:
                    print(registro)
            else:
                print("No hay registros aún.")

# Si el usuario elige la opcion 24, el programa se termina y se cierra.
        elif opcion == 24:
            print("Has elegido salir")