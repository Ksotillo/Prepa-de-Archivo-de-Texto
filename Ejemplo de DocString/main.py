from operaciones import *

def main():
    print("Bienvenido a mi calculadora, selecciona una operación")

    print(
        '''
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        '''
    )

    seleccion = input("Selecciones una operación (1,2,3,4)")
    num1 = int(input("Ingrese el primer número"))
    num2 = int(input("Ingrese el segundo número"))

    if seleccion == '1':
       print(num1, "+", num2, '=', suma(num1, num2))
    elif seleccion == '2':
        print(num1, "+", num2, '=', resta(num1, num2))
    elif seleccion == '3':
        print(num1, "+", num2, '=', multiplicar(num1, num2))
    elif seleccion == '4':
        print(num1, "+", num2, '=', dividir(num1, num2))
    else:
        print("Ha ingresado una opción incorrecta")

main()