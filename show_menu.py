import register

CONSULT_DISORDER = "consultar"
ADD_DISORDER = "agregar"
TAKE_TERAPY = "cita"


def show_menu(option: str = CONSULT_DISORDER):
    disorders = register.Register()

    if option == CONSULT_DISORDER:
        name = input("Escribe el nombre del transtorno que quieres consultar : ")

        disorder = disorders.search_by_name(name)

        if disorder is None:
            print("""Parece que no tenemos este transtorno en nuestra base de datos.
            ¿Te gustaría añadirlo por tu cuenta?""")

            add_disorder = input("si/no: ")

            if add_disorder == "si":
                return show_menu(ADD_DISORDER)
            else:
                print("Suerte!")
                return

        name, description, source = disorder

        print(f"nombre del transtorno: {name}")
        print(f"descripcion: {description}")
        print(f"fuente: {source}")
    elif option == ADD_DISORDER:
        name = input("Escribe el nombre del transtorno :  ")
        description = input("Escribe la descripcion : ")
        source = input("Escribe la fuente del transtorno : ")

        disorders.create_disorder(name, description, source)
        print("Tu transtorno ha sido creado correctamente.")
    elif option == TAKE_TERAPY:
        print("Puedes tomar terapia en la universidad es de 8Am - 5Pm")
        print("Contactate con 320-346-7252")
    else:
        print("opcion incorrecta")


if __name__ == "__main__":
    show_menu()
