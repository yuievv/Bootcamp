prijs_appels = 3.40
prijs_druiven = 2.45
prijs_bananen = 1.95
btw = 9 / 100


totaal_prijs = prijs_appels + prijs_druiven + prijs_bananen
btw_bedrag = totaal_prijs * btw

print(f"Totaalbedrag: €{totaal_prijs:.2f}")
print(f"BTW bedrag: €{btw_bedrag:.2f}")