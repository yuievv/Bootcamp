from random import randint

def speel_ronde():
    te_raden = randint(1,5)
    foute_gokken = 0
    while True:
        gok = int(input('Kies een getal van 1 t/m 5: '))
        if gok == te_raden:
            print("Je hebt het getal goed geraden!")
            break
        else:
            print("Je hebt het getal niet goed geraden!")
            foute_gokken += 1
    return foute_gokken

def speel_spel():
    totaal_foute_gokken = 0
    for i in range(3):
        print(f"Ronde {i+1}:")
        foute_gokken = speel_ronde()
        totaal_foute_gokken += foute_gokken
    score = 20 - totaal_foute_gokken
    print(f"Je eindscore is: {score}")

speel_spel()




