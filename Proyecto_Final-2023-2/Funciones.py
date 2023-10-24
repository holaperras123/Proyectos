import json 

def nuevo_dato():
    num_registro = input("Cuál es su número de registro?: ")
    nombre = input("Cuál es su nombre?: ")
    materias = input("Qué materias desea inscribir?: ")

    diccionario = {

        "Código del estudiante: " : num_registro,
        "Nombre: " : nombre,
        "Materias: " : materias

    }

    with open("registro.json") as registro_previo:
        datos = json.load(registro_previo)
        datos[num_registro] = diccionario
    with open("registro.json", "w") as dato_agregado:
        json.dump(datos, dato_agregado, indent=1)

def modi_menu ():
    ajax = ["1. Número de registro", "2. Nombre", "3. Materias inscritas"]
    for i in range (4)[1::]:
        print (f"{ajax[i]}\n")
        input("Qué deseas modificar?")


def buscar_dato():
    mod_registro = input("Cuál regustro deseas modificar? Introduce su número: ")
    with open("registro.json") as modificacion: 
        dato = json.load(modificacion)
        if dato[mod_registro] in dato:
            modi_menu()

def continuar():
    h = input("desea continuar? y/n: ")
    if h == "n":
        print("chao profeDXFCGVHBJN")
    elif h == "y":
        print("\033c", end="")
        nuevo_dato()
        continuar()
    else:
        input("dato invalido, <enter> para continuar")
        continuar()


