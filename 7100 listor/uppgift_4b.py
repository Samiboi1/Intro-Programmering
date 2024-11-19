bok = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
ord = input("Skriv ett ord: ")
svar = ""
svar2 = ""
for bokstav in ord:
    nytt_index = bok.index(bokstav) + 1
    if nytt_index > 27:
        nytt_index = 0
    svar += bok[nytt_index]
print(svar)
print("Nu dekrypterar vi!")
for bokstav in svar:
    ny_index = bok.index(bokstav) - 1
    if ny_index < 0:
        ny_index = 27
    svar2 += bok[ny_index]
print(svar2)