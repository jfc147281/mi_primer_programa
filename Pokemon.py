
pokemon_elegido = input ("Contra que pokemon deseas luchar (Squirtle / Charmander / Bulbasur: ) ")

vida_pikachu = 100
vida_enemigo = 0
dano_enemigo = 0

if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    dano_enemigo = 8
elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
    dano_enemigo = 7
elif pokemon_elegido == "Bulbasur":
    vida_enemigo = 100
    dano_enemigo = 10

while vida_pikachu >0 and vida_enemigo > 0:
    ataque_elegido = input("Eliga un ataque (Chispazo / Bola voltio)")
    if ataque_elegido == "Chispazo":
        vida_enemigo -= 10
    elif ataque_elegido == "Bola voltio":
        vida_enemigo -= 12
    print("La vida de {} es {}".format(pokemon_elegido, vida_enemigo))
    print("{} te hace un ataque de {} de daño".format(pokemon_elegido, dano_enemigo))
    vida_pikachu -= dano_enemigo
    print("La vida de pikachu es de", vida_pikachu)
    print("Codigo combate")

if vida_enemigo > 0:
    ganador = pokemon_elegido
else:
    ganador = "Pikachu"

print("El combate ha finalizado")
print("El ganador es: ", ganador)