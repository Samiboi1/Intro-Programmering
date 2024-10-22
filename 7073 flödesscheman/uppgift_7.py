import random
fraga = input("Vill du spela sten, sax, påse? j/n: ")
while fraga == "j":
  svar = input("Sten, Sax, Påse: ")
  random_word = (random.randrange(1, 4))
  # 1 == "Sten"
  # 2 == "Påse"
  # 3 == "Sax"
  if svar == "Sten" or svar == "sten" and random_word == 2:
    print("Påse")
    print("Förlust")
  elif svar == "Sten" or svar == "sten" and random_word == 3:
    print("Sax")
    print("Vinst")
  elif svar == "Sten" or svar == "sten" and random_word == 1:
    print("Sten")
    print("Lika")
  elif svar == "Påse" or svar == "påse" and random_word == 3:
    print("Sax")
    print("Förlust")
  elif svar == "Påse" or svar == "påse" and random_word == 1:
    print("Sten")
    print("Vinst")
  elif svar == "Påse" or svar == "påse" and random_word == 2:
    print("Påse")
    print("Lika")
  elif svar == "Sax" or svar == "sax" and random_word == 1:
    print("Sten")
    print("Förlust")
  elif svar == "Sax" or svar == "sax" and random_word == 2:
    print("Påse")
    print("Vinst")
  elif svar == "Sax" or svar == "sax" and random_word == 3:
    print("Sax")
    print("Lika")
  svar = input("Vill du spela igen? j/n: ")
if fraga == "n":
  print("Tack för att du spelade!")
else:
  print("Oförskämda jävel")