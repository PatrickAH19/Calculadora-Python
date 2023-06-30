#Paquetes instalados
import time

# Funciones de la operacion
def sumarOp(var1, var2):
    print(var1 + var2)
def restaOp(var1, var2):
    print(var1 - var2)
def multiplicarOp(var1, var2):
    print(var1 * var2)
def dividirOp(var1, var2):
    print(var1 / var2)

# Iniciar la calculadora
while True:
    # Index principal
    print("------------------------------------------")
    print("||       Bienvenido a Calculadora       ||")
    print("|| Elige la operacion que desea hacer:  ||")
    print("|| 1. Sumar                             ||")
    print("|| 2. Restar                            ||")
    print("|| 3. Multiplicar                       ||")
    print("|| 4. Dividir                           ||")
    print("|| 0. Exit                              ||")
    print("------------------------------------------\n")
    time.sleep(3)

    # Elegir operacion
    print("----------------------------------------------")
    op = int(input("|| Ingresar la operacion a realizar: "))
    print("|| Espere un momento...                     ||")
    print("----------------------------------------------\n")
    time.sleep(8)

    # Salir de la calculadora
    if op == 0:
        print("Saliendo de la calculadora...")
        break

    # Pedir que ingrese los datos a trabajar
    print("---------------------------------------------")
    var1 = float(input("|| Ingrese el primer valor: "))
    var2 = float(input("|| Ingrese el segundo valor: "))
    print("|| Ya casi esta, espere unos segundos...    ||")
    print("---------------------------------------------\n")
    time.sleep(3)

    # Inprimir el resultado
    print("*"*63)
    if op != 0:
        if op == 1:
            print(f"|| La Suma de '{var1}' y '{var2}' son: ", end="")
            sumarOp(var1, var2)
        elif op == 2:
            print(f"|| La Resta de '{var1}' y '{var2}' son: ", end="")
            restaOp(var1, var2)
        elif op == 3:
            print(f"|| La Multiplicación de '{var1}' y '{var2}' son: ", end="")
            multiplicarOp(var1, var2)
        elif op == 4:
            # Si la variable no es 0 entonces continuara el codigo
            if var1 != 0 and var2 != 0:
                print(f"|| La Divición de '{var1}' y '{var2}' son: ", end="")
                dividirOp(var1, var2)
            # Si la variable es 0, entonces no se podra dividir
            else:
                print("No se puede dividir entre cero")
        # Si no se ha ingresado una opcion valida no se obtendra un resultado
        else:
            print("Error, Opción no valida...")
    # si la opcion es 0 entonces se producira un error y no se obtendra un resultado
    else:
        print("Error porfavor elije otro")
    print("*"*63, "\n")

    # Repetir el bucle con un ENTER
    print("~~~~~~~~~~~~~~~~~"*2)
    print("Porfavor, eliga")
    print("1. Continuar...")
    print("0. Exit")
    var = int(input(""))
    print("~~~~~~~~~~~~~~~~~"*2, "\n")

    if var == 0:
        break