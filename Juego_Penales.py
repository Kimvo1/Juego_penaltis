class JuegoPenaltis:
    def __init__(self):
        print("!Bienvenido al juego de atajar y cobrar penaltis¡")
        self.nombre_usuario = input("¿Cuál es tu nombre?: ")

    def menu_principal(self):
        print(self.nombre_usuario,","
            "Seleccione una opción:\n"
            "1. Atajar\n"
            "2. Cobrar\n"
            "Para salir, oprima: s")

    def iniciar_juego(self):
        while True:
            self.menu_principal()
            opcion = input("Ingrese el número de la opción que desea seleccionar: ")
            if opcion == "1":
                self.atajar()
            elif opcion == "2":
                self.cobrar()
            elif opcion == "s":
                print("¡Gracias por jugar!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def atajar(self):
        print("¿Hacia dónde quieres atajar?\n"
            "1. Izquierda\n"
            "2. Centro\n"
            "3. Derecha\n"
            "Para salir, oprima: s")

        opcion_atajar = input("Ingrese el número de la opción que desea seleccionar: ")

        if opcion_atajar == "1":
            print("¡Atajaste hacia la izquierda!, Ganaste!")
        elif opcion_atajar == "2":
            print("¡Atajaste al centro!, Goool, Perdiste! :()")
        elif opcion_atajar == "3":
            print("¡Atajaste hacia la derecha!, Ganaste")
        elif opcion_atajar == "s":
            print("¡Gracias por jugar!")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    def cobrar(self):
        print("¿Hacia dónde quieres cobrar?\n"
            "1. Izquierda\n"
            "2. Centro\n"
            "3. Derecha")

        opcion_cobrar = input("Ingrese el número de la opción que desea seleccionar: ")
        potencia = input("seleciona la potencia del disparo:\n"
                        "1. Suave\n"
                        "2. Medio\n"
                        "3. Fuerte\n"
                        "escribe la opcion: ")

        if opcion_cobrar == "1":
            print(potencia,"," "¡Cobraste hacia la izquierda!, ¡Se estrelló en el travesaño!, Perdiste! :(")
        elif opcion_cobrar == "2":
            print(potencia,"," "¡Cobraste hacia el centro!, Atajado, Perdiste! :(")
        elif opcion_cobrar == "3":
            print(potencia,"," "¡Cobraste hacia la derecha!, Goool!, Ganaste")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    juego = JuegoPenaltis()
    juego.iniciar_juego()

