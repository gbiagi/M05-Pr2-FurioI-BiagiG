menu_00 = "1.Introdueix una frase\n2.Elimina les vocals\n3.Elimina les consonants\n" \
          "4.Ordena la frase al revés i printala per pantalla\n5.Ordena les paraules de la frase en orde ascendent i printales per pantalla"
flg_00 = True
frase = ""
#alum2
while flg_00:
    print(menu_00)
    opc = input("Elige una opcion: ")
    if not opc.isdigit():
        print("Solo se pueden introducir numeros.")
    elif not int(opc) in range(1, 6):
        print("Opcion incorrecta.")
    else:
        opc = int(opc)
        if opc == 1:
            print()
        if opc == 2:
            print()
        if opc == 3:
            print("Elimina les consonants")
            if frase == "":
                print("Primero tienes que introducir una frase.")
            vocales = "aeiou "
            nueva_frase = ""
            for i in frase:
                if i in vocales:
                    nueva_frase += i
                else:
                    continue
            print(nueva_frase)
            input("Enter para continuar")
        if opc == 4:
            print()
        if opc == 5:
            if frase == "":
                print("Primero tienes que introducir una frase.")
            lista_palabras = frase.split(" ")
            print("Ordena les paraules de la frase en orde ascendent i printales per pantalla")
            for pasadas in range(len(lista_palabras) - 1):
                lista_ordenada = True
                for i in range(len(lista_palabras) - pasadas - 1):
                    if lista_palabras[i].lower() > lista_palabras[i + 1].lower():
                        lista_ordenada = False
                        aux = lista_palabras[i]
                        lista_palabras[i] = lista_palabras[i + 1]
                        lista_palabras[i + 1] = aux
            print(lista_palabras)
            input("Enter para continuar")