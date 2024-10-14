import random
svar = input("Skriv j för att spela, och n för att avsluta ")
while svar == "j":
  tal = (random.randrange(0, 10))
  print(tal)
  tal2 = (random.randrange(0, 10))
  print(tal2)
  tal3 = (random.randrange(0, 10))
  print(tal3)
  if tal == 7 and tal2 == 7 and tal3 == 7:
    print("DU FICK TRE 7:OR")
  elif  tal == tal2 == tal3:
    print("Vinst")
  elif tal == tal2:
    print("mini-vinst")
  elif tal3 == tal:
    print("mini-vinst")
  elif tal3 == tal2:
    print("mini-vinst")
  else:
    print("Förlust")
  svar = input("Vill du spela igen? Skriv j för att spela, och n för att avsluta: ")
if svar == "n":
  print("Tack för att du spelade!")
else:
  print("Oförskämda jävel")