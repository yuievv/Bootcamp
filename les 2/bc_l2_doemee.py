#Krijgt dit dezelfde uitkomst? 
# print( 5*2 -3+4/2 )
# print( 5*2 - 3+4 / 2 )

#En hoe zit het met deze?
# print( (5*2) - (3+4) /2 )
# print( ((5*2) -(3+4)) / 2 )

#Bekijk de volgende code, wat denk je dat eruit komt?
#print( (431 / 100) * 100 )

#Wat gebeurt hier nu weer:
# print( 3 * "hallo" ) 

prijs_appels = 3.40
prijs_druiven = 2.45
prijs_bananen = 1.95
btw = 9 / 100

# Bedrag
totaal_prijs = prijs_appels + prijs_druiven + prijs_bananen

# Berekening
btw_bedrag = totaal_prijs * btw

# Resultaten 
print(f"Totaalbedrag: €{totaal_prijs:.2f}")
print(f"BTW bedrag: €{btw_bedrag:.2f}")