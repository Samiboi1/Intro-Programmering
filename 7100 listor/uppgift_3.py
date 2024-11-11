kons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
vok = ["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]
ord = input("Skriv ett ord: ")
svar = ""
for bokstav in ord:
  if bokstav in kons:
    svar += bokstav + "o" + bokstav
  elif bokstav in vok:
    svar += bokstav
print(svar)

# Skriven av Kevin Yeh