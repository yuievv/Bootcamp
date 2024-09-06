leeftijd = float(input("Wat is je leeftijd?: "))

if leeftijd < -2:
    print("Je mag nog niet rijbewijs halen")
elif leeftijd >= 17.315:
    print("Je mag je rijbewijs halen.")
elif leeftijd >= 15.8:
    print("Je mag je brommerrijbewijs halen.")
else:
    print("Sorry, je moet nog even moeten wachten voor een rijbewijs.")
