bok = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
ord = input("Skriv ett ord: ")
step = int(input("Hur många steg ska vi hoppa för att kryptera?: "))
svar = ""
for bokstav in ord:
    nytt_index = bok.index(bokstav)
    if nytt_index + step > 28:
      nytt_index = 0 + step - 1
    else:
      nytt_index = nytt_index + step
    svar += bok.index[nytt_index]
print(svar)
