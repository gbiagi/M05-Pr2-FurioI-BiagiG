menu_00 = "1.Introdueix una frase\n2.Elimina les vocals\n3.Elimina les consonants\n4.Ordena la frase al revés i printala per pantalla\n5.Ordena les paraules de la frase en orde ascendent i printales per pantalla"

flg_00 = True
while flg_00:
    print(menu_00)
    opc = input("Elige una opcion: ")
    if not opc.isdigit():
        print("Solo se pueden introducir numeros.")
    elif not int(opc) in range(0, 6):
        print("Opcion incorrecta.")
    else:
         if opc == 1:
         if opc == 2:
         if opc == 3:
         if opc == 4:
         if opc == 5:
