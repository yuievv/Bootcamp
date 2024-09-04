mooie = input("Wat voor soort dag is het?: ")
dordrecht = input("In welke stad speelt het verhaal zich af?: ")
julia = input("Wie is de hoofdpersoon?: ")
supermarkt = input("Waar gaat de hoofdpersoon naartoe?: ")
oude = input("Hoe zou je de vrouw beschrijven die de hoofdpersoon ziet?: ")
kaarsen = input("Wat verkoopt de vrouw?: ")
park = input("Wat voor plek komt de hoofdpersoon tegen?: ")
dansen = input("Wat doet de groep mensen?: ")

verhaal = (
    f"Het was een {mooie} dag in {dordrecht}. {julia} liep door de straten, op zoek naar een {supermarkt}. "
    f"Plotseling zag {julia} een {oude} vrouw die {kaarsen} verkocht. {julia} besloot om een paar te kopen en liep verder. "
    f"Toen {julia} bij een {park} kwam, zag zij een groep mensen die {dansen}. "
    f"{julia} besloot om mee te doen en had de tijd van haar leven."
)

print("\n" + verhaal)
