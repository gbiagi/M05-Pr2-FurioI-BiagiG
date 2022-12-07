menu_00 = "1.Introdueix una frase\n2.Elimina les vocals\n3.Elimina les consonants\n" \
          "4.Ordena la frase al revés i printala per pantalla\n5.Ordena les paraules de la frase en orde ascendent i printales per pantalla"
flg_00 = True
frase = "Frase de prueba"
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
            vocales = "aeiou "
            nueva_frase = ""
            for i in frase:
                if i in vocales:
                    nueva_frase += i
                else:
                    continue
            print(nueva_frase)
            input("Enter to continue")
        if opc == 4:
            print()
        if opc == 5:
            print("Ordena les paraules de la frase en orde ascendent i printales per pantalla")

