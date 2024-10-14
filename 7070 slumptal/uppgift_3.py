import random
fraga = input("Vill du spela sten, sax, påse? j/n: ")
while fraga == "j":
  svar = input("Sten, Sax, Påse: ")
  words = ["Sten", "Sax", "Påse"]
  num_word = 1
  random_word = random.choices(words, num_word)
  print(random_word)
  if svar == "Sten" or svar == "sten" and random_word == "Påse":
    print("Förlust")
  elif svar == "Sten" or svar == "sten" and random_word == "Sax":
    print("Vinst")
  elif svar == "Påse" or svar == "påse" and random_word == "Sax":
    print("Förlust")
  elif svar == "Påse" or svar == "påse" and random_word == "Sten":
    print("Vinst")
  elif svar == "Sax" or svar == "sax" and random_word == "Sten":
    print("Förlust")
  elif svar == "Sax" or svar == "sax" and random_word == "Påse":
    print("Vinst")
  svar = input("Vill du spela igen? j/n: ")
if svar == "n":
  print("Tack för att du spelade!")
else:
  print("Oförskämda jävel")