#Juego de ahorcado
print("\n\n*** BIENVENIDO AL JUEGO DE AHORCADO ***")
Palabra=input("Digite una palabra: ").upper()
Palabra=list(Palabra)
print("hola mundo")

def isLetra():
    while True:
        try:
            Letra = input("\n\n Ingrese una letra: ").upper()
            if len(Letra) == 1 and Letra.isalpha():
                break
            else:
                print("\nSe detectó más de una letra o caracteres no alfabéticos.")
        except ValueError:
            None
    return Letra


def Ahorcado(Palabra, Intentos, Pb_Oculta, cntAcertadas):
    lgtd_Pb = len(Palabra)

    if lgtd_Pb == cntAcertadas:
        print("FELICIDADES, HAS DESCUBIERTO LA PALABRA")
        Intentos = -200
        return Intentos, cntAcertadas  # Salir de la función si se ha ganado

    AdivinoLetra = False
    Letra = isLetra()

    for i in range(len(Palabra)):
        if Letra in Palabra[i]:
            Pb_Oculta[i] = Letra
            cntAcertadas += 1
            AdivinoLetra = True

    if AdivinoLetra:
        print("Correcto, has acertado una(s) letra(s)")
        print("\n", (" ").join(Pb_Oculta))
    else:
        Intentos -= 1
        print(f"Incorrecto, le quedan {Intentos} vidas")

    return Intentos, cntAcertadas


Palabra_Oculta = ['_'] * len(Palabra)
Vidas = 5
Acertadas = 0
while Vidas > 0:
    Vidas, Acertadas = Ahorcado(Palabra, Vidas, Palabra_Oculta, Acertadas)
    if (Vidas == -200):  # Salir del ciclo si se ha ganado
        break
    
if(Vidas==0):
    print(f"\n\nHAS PERDIDO, LA PALABRA ERA: {Palabra}\n HAS ACERTADO {Acertadas} LETRA(S)")