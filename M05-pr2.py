menu_00 = "1.Introdueix una frase\n2.Elimina les vocals\n3.Elimina les consonants\n4.Ordena la frase al revés i printala per pantalla\n5.Ordena les paraules de la frase en orde ascendent i printales per pantalla"
#tareas 1, 2 y 4
flg_00 = True
frase = ""
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
            while frase == "":
                frase = input("Introduce una frase:\n")
                if frase == "":
                    print("Frase vacia, escribe algo.")
                else:
                    break

        if opc == 2: # elimina vocales
            if frase == "":
                print("Escribe primero una frase.")
                input("\nEnter to continue\n")
            else:
                vocales = "aeiou"
                frase_nueva = ""
                for letra in frase.strip():
                    if not letra in vocales:
                        frase_nueva += letra

                print(frase_nueva)
                input("Enter to continue.")

        if opc == 3:
            print()
        if opc == 4:
            if frase == "":
                print("Escribe primero una frase.")
                input("\nEnter to continue\n")
            else:
                frase_nueva = ""
                for letra in frase[::-1]:
                    frase_nueva += letra

                print(frase_nueva)
        if opc == 5:
            print()
