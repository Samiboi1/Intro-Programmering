bok = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
ord = input("Skriv ett ord: ")
svar = ""
for bokstav in ord:
    nytt_index = bok.index(bokstav) + 1
    if nytt_index > 27:
        nytt_index = 0
    svar += bok[nytt_index]
print(svar)
