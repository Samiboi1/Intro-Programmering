bok = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def kry(ord):
  svar = ""
  for bokstav in ord:
    nytt_index = bok.index(bokstav)
    if nytt_index + step > 25:
      nytt_index = 0 + step - (25 - nytt_index) - 1
    else:
      nytt_index = nytt_index + step
    svar += bok[nytt_index]
  return svar

def dekry(ord):
  svar = ""
  for bokstav in ord:
    if bokstav == "_":
      svar += "_";
    else:
      nytt_index = bok.index(bokstav)
      nytt_index = nytt_index - step
      svar += bok[nytt_index]
  return svar

ord = input("Skriv ett ord: ")
step = int(input("Hur många steg ska vi hoppa för att kryptera?: "))

hemligt = kry(ord)
print("hemligt", hemligt)

print("Nu dekrypterar vi")

läsbart = dekry(hemligt)
print("läsbart",läsbart)