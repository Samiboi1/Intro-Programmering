bok = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ord = input("Skriv ett ord: ")
step = int(input("Hur många steg ska vi hoppa för att kryptera?: "))
svar = ""
for bokstav in ord:
  if bokstav == "_":
      svar += "_";
  else:
      nytt_index = bok.index(bokstav)
      nytt_index = nytt_index - step
      svar += bok[nytt_index]
print(svar)