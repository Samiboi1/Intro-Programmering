import random
svar = input("Vill du spela? j/n: ")
while svar == "j":
  tal = (random.randrange(1, 7))
  print(tal)
  tal2 = (random.randrange(1, 7))
  print(tal2)
  if  tal == tal2:
    print("Vinst")
  else:
    print("Förlust")
  svar = input("Vill du spela igen? j/n: ")
if svar == "n":
  print("Tack för att du spelade!")
else:
  print("Oförskämda jävel")