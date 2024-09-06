kleuren = ["rood", "orange", "geel", "groen", "blauw", "paars"]

naam = input("Hoe heet je? ")
favoriete_kleur = input("Wat is je favoriete kleur? ")

if favoriete_kleur.lower() in [kleur.lower() for kleur in kleuren]:
    print(f"Hallo {naam}, je favoriete kleur {favoriete_kleur} is prachtig!")
    print("Je kleur is als een zonnestraal op een wolkeloze dag,")
    print("een vleugje vreugde in een wereld vol kleur!")
else:
    print(f"Psst {naam}, deze kleur is niet zo geweldig!")
    print("Waarom probeer je niet paar van deze kleuren uit?")
    print(", ".join(kleuren))