fruit = ["appel", "banaan", "aardbei", "druif", "ananas", "framboos"]

index = int(input("Voer een nummer tussen (0-5): "))

if index < 0 or index >= len(fruit):
    print("Foute nummer!")
else:
    gepakt_fruit = fruit.pop(index)

    print(f"Het gepakte stuk fruit is: {gepakt_fruit}")
    print("De verbeterde lijst is:")
    print(fruit)