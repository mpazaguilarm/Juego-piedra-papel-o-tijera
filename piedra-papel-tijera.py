nombre1 = input("¿Cómo se llamará el jugador 1?: ")
nombre2 = input("¿Cómo se llamará el jugador 2?: ")

jugador1 = input("Hola jugador1. ¿Qué eliges? ¿Piedra, papel o tijera?: ")
jugador2 = input("Hola jugador2. ¿Qué eliges? ¿Piedra, papel o tijera?: ")


if jugador1 == jugador2:
    print("Ha sido un empate")
elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
    print("Ha ganado: ", nombre1)
    #sino puedo escribirlas como condicion1, condicion 2, y condicion 3
else:
    print("Ha ganado: ", nombre2)