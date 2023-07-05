# importar librerías necesarias :p
import time
from math import sqrt


# Operación Aritmetica
class operacionesAritmeticas:
    def sumarOp(self, numeros):
        resultado = sum(numeros)
        return resultado

    def restarOp(self, numeros):
        if len(numeros) >= 2:
            resultado = numeros[0] - sum(numeros[1:])
            return resultado
        else:
            return None

    def multiplicarOp(self, numeros):
        resultado = 1
        if len(numeros) >= 2:
            for num in numeros:
                resultado *= num
            return resultado
        else:
            return None

    def dividirOp(self, numeros):
        if len(numeros) >= 2:
            resultado = numeros[0]
            for num in numeros[1:]:
                resultado /= num
            return resultado
        else:
            return None


# Operacion Avanzada
class operacionesAvanzadas:
    def factorizarOp(self, varAvNum):
        resultado = 1
        for i in range(2, varAvNum + 1):
            resultado *= i
        return resultado

    def raizOp(self, varAvNum):
        resultado = sqrt(varAvNum)
        return resultado

    def porcentajeOp(self, varAvNum, varAvNumBa):
        resultado = varAvNum * varAvNumBa / 100
        return resultado


# Creamos un while que este siempre activo
while True:
    # Menu de Inicio
    print("*********************************************************")
    print("||             Calculadora Simple Practica             ||")
    print("||                                                     ||")
    print("|| Por favor, elija que opcion desea realizar          ||")
    print("|| 1. Sumar                                            ||")
    print("|| 2. Restar                                           ||")
    print("|| 3. Multiplicar                                      ||")
    print("|| 4. Dividir                                          ||")
    print("||                                                     ||")
    print("|| 9. Opcion Avanzada                                  ||")
    print("|| 0. Exit                                        V1.0 ||")
    print("*********************************************************\n")

    # Elegir una opcion
    print("****************************************************")
    varOp = int(input("|| Eliga la opcion a realizar: "))
    print("|| Por favor espere un momento...                 ||")
    print("****************************************************\n")

    # Si el usuario elige la opcion Exit el código se parará
    if varOp == 0:
        break
    time.sleep(5)

    # Estetica creo, esta parte del codigo crea una variable 'str' para que el usuario verifique la opción que eligio
    varOpNom = ""
    if varOp == 1:
        varOpNom = "Sumar"
    elif varOp == 2:
        varOpNom = "Restar"
    elif varOp == 3:
        varOpNom = "Multiplicar"
    elif varOp == 4:
        varOpNom = "Dividir"
    else:
        varOpNom = "Error... Opcion no establecida"

    # Crea una lista donde se ingresaran todos los datos, esto sirve más para las operaciones aritmeticas simples
    numeros = []

    # Creamos una nueva variable para las opciones avanzadas
    varOpAv = 0
    varAvNum = 0
    varAvNumBa = 0

    # Como les explico que esto también es para que el código se vea más bonito :^
    varOpAvNom = ""

    # Si el usuario ingreso otra opción aparte del 9, el código se ejecutara normalmente
    # y gracias a las variables creadas el código le mostrara la opción que eligio
    if varOp != 9:
        print("***********************************************************************************")
        print(f"|| Usted a elegido {varOpNom}, porfavor Ingrese los datos y ingrese '0' para 'terminar':")

        # Creamos un bucle anidado, este se encargara de agregar los datos a la lista
        while True:
            varN = float(input("|| "))
            if varN == 0:
                break
            numeros.append(varN)
        print("***********************************************************************************\n")
    # si el usuario eligio la opcion 9 entonces se mostrara las opciones avanzadas
    else:
        # Menu de las opciones avanzadas
        print("**********************************************************************************")
        print("||      Has ingresado a Opciones Avanzadas, tienes las siguientes opciones:     ||")
        print("|| 1. Factorización                                                             ||")
        print("|| 2. Raiz Cuadrada                                                             ||")
        print("|| 3. Porcentaje                                                                ||")
        print("|| 0. Exit                                                               V.1.0. ||")
        print("**********************************************************************************\n")

        # Elegir una opción disponible
        print("*******************************************************************************")
        varOpAv = int(input("|| Eliga la opcion avanzada a realizar: "))
        print("|| Porfavor espere...")
        print("*******************************************************************************\n")

        # Como les explico... esto también es estetica y sirve para que se vea bonito
        if varOpAv != 0:
            if varOpAv == 1:
                varOpAvNom = "Factorizar"
            elif varOpAv == 2:
                varOpAvNom = "Raiz Cuadrada"
            elif varOpAv == 3:
                varOpAvNom = "Porcentaje"
        else:
            break

        # Si el usuario elige las otras opciones y no el 3 se ejecutará normalmente
        # Ingresar un dato para la operación
        if varOpAv != 3:
            print("********************************************")
            varAvNum = int(input(f"|| A seleccionado {varOpAvNom}, Ingresar un Numero entero:"))
            print("|| Ok, porfavor espere...")
            print("********************************************\n")
        # si ingreso la opcion 3, se agregará una nueva variable para realizar la operación
        else:
            print("***************************************************************************************************")
            print(f"|| A seleccionado {varOpAvNom}, debe ingresar el numero base y el porcentaje a sacar:")
            varAvNum = int(input("|| Ingrese el numero base: "))
            varAvNumBa = float(input("|| Ingresar el porcentaje que se desea sacar: "))
            print("|| Porfavor espere un momento...")
            print("***************************************************************************************************")
        time.sleep(5)

    # Creamos una instancia de la clase
    calculadora1 = operacionesAritmeticas()

    # Llamar a los metodos utilizando la instancia
    resul_suma = calculadora1.sumarOp(numeros)
    resul_resta = calculadora1.restarOp(numeros)
    resul_multiplicacion = calculadora1.multiplicarOp(numeros)
    resul_divicion = calculadora1.dividirOp(numeros)

    # Creamos una instancia de la clase
    calculadora2 = operacionesAvanzadas()

    # Llamar a los metodos utilizando la instancia
    resul_factorizar = calculadora2.factorizarOp(varAvNum)
    resul_raiz = calculadora2.raizOp(varAvNum)
    resul_porcentaje = calculadora2.porcentajeOp(varAvNum, varAvNumBa)

    # Selección y imprimir el resultado
    print("****************************************************")
    if varOp == 1:
        print(f"El resultado de {varOpNom} es: ", end="")
        print(resul_suma)
    elif varOp == 2:
        print(f"El resultado de {varOpNom} es: ", end="")
        print(resul_resta)
    elif varOp == 3:
        print(f"El resultado de {varOpNom} es: ", end="")
        print(resul_multiplicacion)
    elif varOp == 4:
        print(f"El resultado de {varOpNom} es: ", end="")
        print(resul_divicion)

    # Opciones Avanzadas
    elif varOpAv == 1:
        print(f"El resultado de {varOpAvNom} es: ", end="")
        print(resul_factorizar)
    elif varOpAv == 2:
        print(f"El resultado de la {varOpAvNom} es: ", end="")
        print(resul_raiz)
    elif varOpAv == 3:
        print(f"El resultado del {varOpAvNom} es: ", end="")
        print(resul_porcentaje)
    else:
        print("Ingrese una opción valida...")
        break
    print("****************************************************\n")

    time.sleep(6)
