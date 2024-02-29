polinomioA = []
polinomioB = []

def Ingresar_Elementos(polinomio):
    cantidad = int(input("\nIngrese la Cantidad de Elementos que Desea Ingresar: "))

    for i in range(cantidad):
        elemento = input("Ingrese el Elemento No.{}: ".format(i + 1))
        polinomio.append(elemento)

def Ingresar_Componentes(polinomio):
    for i in range(len(polinomio)):
        componente = int(input("\nIngrese el Componente del Elemento No.{}:".format(i+1)))
        polinomio[i] = (componente,polinomio[i][1])

def Ingresar_Coeficientes(polinomio):
    for i in range (len(polinomio)):
        coeficiente = int(input("\nIngrese el Coefeciente del Elemento No.{}:".format(i+1)))
        polinomio[i] = (polinomio[i][0],coeficiente)

def Ingreso_PolinomioA():
    print("\n Ingreso Polinomio A")
    print("Los Polinomios estan Formados Por:")
    print("Los Elemento es la Cantidad de numeros del Polinomio es decir:")
    print("𝑎 = 3𝑥^2 + 18𝑥 − 10")
    print("Este Polinomio cuenta con 3 Elementos")
    print("\nEl Componente es el Número que acompaña cada Elemento del Polinomio es decir:")
    print("3𝑥^2")
    print("El Componente de este Elemento es 3")
    print("\nEl Coeficiente es la Potencia que acompaña al Elemento")
    print("3𝑥^2")
    print("El Coeficiente de este Elemento es 2, ya que esa es su potencia")
    print("\n¡IMPORTANTE!")
    print("La Letra Predeterminada para Trabajar los Polinomios es x, y no se puede cambiar ")
    print("Ya con esto dicho podemos Ingresar el Polinomio sin ningun Problema")

    Ingresar_Elementos(polinomioA)
    Ingresar_Componentes(polinomioA)
    Ingresar_Coeficientes(polinomioA)

def Ingreso_PolinomioB():
    print("\n Ingreso Polinomio B")
    print("Los Polinomios estan Formados Por:")
    print("Los Elemento es la Cantidad de numeros del Polinomio es decir:")
    print("𝑎 = 3𝑥^2 + 18𝑥 − 10")
    print("Este Polinomio cuenta con 3 Elementos")
    print("\nEl Componente es el Número que acompaña cada Elemento del Polinomio es decir:")
    print("3𝑥^2")
    print("El Componente de este Elemento es 3")
    print("\nEl Coeficiente es la Potencia que acompaña al Elemento")
    print("3𝑥^2")
    print("El Coeficiente de este Elemento es 2, ya que esa es su potencia")
    print("\n¡IMPORTANTE!")
    print("La Letra Predeterminada para Trabajar los Polinomios es x, y no se puede cambiar ")
    print("Ya con esto dicho podemos Ingresar el Polinomio sin ningun Problema")

    Ingresar_Elementos(polinomionB)
    Ingresar_Componentes(polinomioB)
    Ingresar_Coeficientes(polinomioB)

def Suma_Polinomios(polinomioA,polinomioB):
    resultado = []
    for i in range(max(len(polinomioA),len(polinomioB))):
        coeficienteA = polinomioA[i][1] if i < len(polinomioA) else 0
        coeficienteB = polinomioB[i][1] if i < len(polinomioB) else 0

        suma = coeficienteA + coeficienteB
        resultado.append((polinomioA[i][0],suma))

    return resultado
while True:
    print("\n	MENÚ PRINCIPAL")
    print("1. Ingresar Componentes de un Polinimio")
    print("2. Adición y Sustraccion")
    print("3. Evaluar Polinimios")
    print("4. SALIR")

    opcion = input("Ingrese el Número de la Opción que Desee: ")

    if opcion == "1":
        while True:
            print("\nIngreso de Componentes de Polinomios")
            print("1. Polinomio A")
            print("2. Polinomio B")
            print("3. Regresar al Menú Pirncipal")

            opcion2 = input("Ingrese el Número de la Ooción que Desee: ")

            if opcion2 == "1":
                Ingreso_PolinomioA()

            elif opcion == "2":
                Ingreso_PolinomioB()

            elif opcion2 == "3":
                break

            else:
                print("\n¡ERROR!")
                print("Opción Invalida. Intente de Nuevo")

    elif opcion == "2":
        while True:
            print("\nOperaciones")
            print("1. Adición")
            print("2. Sustracción")
            print("3. Regresar al Menú Pirncipal")

            opcion3 = input("Ingrese el Número de la Opción que Desee: ")

            if opcion3 == "1":
                resultado_suma = SumarPolinomios(polinomioA, polinomioB)

            elif opcio3 == "2":
                print("RESTA")

            elif opcion2 == "3":
                break

            else:
                print("\n¡ERROR!")
                print("Opción Invalida. Intente de Nuevo")


    elif opcion == "3":
        print("El Resultado de la Operacion del Polinomio es: ")
        print(resultado_suma)

    elif opcion == "4":
        print("Gracias por Utilizar mi Programa")
        print("Programa Hecho por: Angie Melissa Santiago Rodriguez - 1555123")
        exit()

    else:
        print("\n¡ERROR!")
        print("Opción Invalida. Intente de Nuevo")

