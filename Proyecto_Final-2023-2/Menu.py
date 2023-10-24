from LlamarFunciones import * 
print("\033c", end="")
while True:
    x = 50 #Variable del tamaño del menú

    str1 = ""
    print("\n",str1.rjust(x,"-"),"\n") #Ralla separadora
    print(f'{"Programa para el manejo de estudiantes UNAL":^{str(x)}}') #Centrar el string en el valor de x
    print("\n",str1.rjust(x,"-"),"\n\n")

    nombres_menu = ["Crear registros", "Modificar registros", "Consultar refistros", "Eliminar registros"]

    for i in range(len(nombres_menu)+1)[1::]:
        print(f"{i:>{x//4}}.  {nombres_menu[i-1]}") # Iterar la lista por cada valor de opciones para hacer el menú

    print(f"\n{0:>{x//4}}.  <Terminar consulta>\n\n")
    opcion = input(f"{str1:>{(x//4)-1}}Digite una opción: ")

        
    if opcion == "0":
        print("\033c", end="")
        print(f'\n\n{"Gracias profesorsito por favor apruebanosss, si??":^{str(x)}}\n\n')
        break
    
    elif opcion == "1":
        print("\033c", end="")
        crear_registro()
    elif opcion == "2":
        print("\033c", end="")
        modificar_registros()
    else:
        print(f'\n\n{"Opción inválida, por favor introdusca una nueva":^{str(x)}}\n')
        input(f'{"<enter> para continuar":^{str(x)}}\n')
    print("\033c", end="")


