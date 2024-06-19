print("AHORCADO")


Reglas del juego del "Ahorcado":

    - Un jugador elige una palabra secreta y dibuja un espacio para cada letra de la palabra.

    - El otro jugador intenta adivinar letras para completar la palabra.

    - Si el jugador adivinador adivina una letra correctamente, se revela en su lugar correspondiente.

    - Si el jugador adivinador adivina incorrectamente, se dibuja una parte del cuerpo en la horca.

    - El objetivo del jugador adivinador es adivinar la palabra antes de que se dibuje el dibujo completo en la horca.")



import random
dibujo_ahorcado = [
        
        '''
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    ''',
        
        
        '''
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    ''',

    '''
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    ''',

    '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    ''',

    '''
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    ''',

    '''
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    '''
]

# Creamos variables para configurar el juego
lista_palabras = ["gato", "perro", "caballo", "ornitorrinco", "elefante"]

palabra_oculta = random.choice(lista_palabras)

solucion = list("_" * len(palabra_oculta))

vidas = 6

while vidas >0 and vidas <= 6: # Hacemos bucle while para iterar en el programa siempre que se cumplan las condiciones

    print(f"La palabra es {','.join(solucion)}")
  

    letra = input("Dime una letra para adivinar la palabra: ")
    print("------------------------------------------------")

    if letra: # evaluamos si el input es correcto
        
        if letra in palabra_oculta:
            for idx, char in enumerate(palabra_oculta): # Esta solución nos crea unos índices para cada caracter de la palabra y nos devuelva letras repetidas
                if char == letra:
                    solucion[idx] = letra
            #solucion[palabra_oculta.index(letra)] = letra
            print(f"BIEN!👌🏻 La letra {letra.upper()} está en la palabra \n {''.join(solucion)}")
            print("---------------------------------------------------------------------------")


        else:
            vidas -= 1
            print(f"la letra {letra.upper()} no está, te quedan {vidas} vidas.💔")
            dibujo = dibujo_ahorcado[vidas]
            print(dibujo)

        if palabra_oculta == "".join(solucion): # esta condición nos comprueba si hemos adivinado la palabra secreta
            print("✨✨Enhorabuena, has ganado✨✨!!!")
            break

            #paramos el juego

else:
    print("Oh, te has quedado sin vidas, has muerto⚰️⚰️")
    print (f"La palabra correcta era {palabra_oculta}")
        # el bucle se ha detenido porque te has quedado sin vidas
