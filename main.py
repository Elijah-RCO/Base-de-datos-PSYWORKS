import show_menu


def main():
    print("Bienvenido")

    print("¿Que te gustaría hacer?")
    print("Consultar, Agregar, Cita")

    opcion = input("Escribe la opcion que deseas realizar: ")
    opcion = opcion.lower()

    show_menu.show_menu(opcion)


if __name__ == "__main__":
    main()
