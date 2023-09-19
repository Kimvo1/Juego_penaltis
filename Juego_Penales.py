while True:
    print("Bienvenido al juego de atajar y cobrar penaltis")
    nombre = input("Cual es tu nombre?: ")
    print(nombre,",", '''Seleccione una opción:
    1. Atajar
    2. Cobrar
    para salir oprima: s''')

    opcion = input("Ingrese el número de la opción que desea seleccionar: ")
    if opcion == "1":
        print(''' ¿Hacia dónde quieres atajar? 
        1. Izquierda
        2. Centro
        3. Derecha
        para salir oprima: S'''
        )
        opcion_atajar = input("Ingrese el número de la opción que desea seleccionar: ")
        if opcion_atajar == "1":
            print("¡Atajaste hacia la izquierda!, Ganaste!")
        elif opcion_atajar == "2":
            print("¡Atajaste al centro!, Goool, Perdiste! :()")
        elif opcion_atajar == "3":
            print("¡Atajaste hacia la derecha!, Ganaste")
        elif opcion_atajar == "s":
            print("¡Gracias por jugar!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
    elif opcion == "2":
        print('''¿Hacia dónde quieres cobrar?
        1. Izquierda
        2. Centro
        3. Derecha''')
        opcion_cobrar = input("ingrese el numero de la opcion que desea seleccionar: ")
        if opcion_cobrar == "1":
            print("¡Cobraste hacia la izquierda!, ¡Se estrello en el travesaño!, Perdiste! :()")
        elif opcion_cobrar == "2":
            print("¡Cobraste hacia el centro!, Atajado, Perdiste! :()")
        elif opcion_cobrar == "3":
            print("¡Cobraste hacia la derecha!, Goool!, Ganaste")
    elif opcion == "s":
        print("¡Gracias por jugar!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
    
        

