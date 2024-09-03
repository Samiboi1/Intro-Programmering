tal = int(input("Ange ett heltal: "))
if tal > 0 and tal < 9:
  print(tal, "är ett ensiffrigt tal")
elif tal > 10 and tal < 99:
  print(tal, "är ett tvåsiffrigt tal")
elif tal > 100 and tal < 999:
  print(tal, "är ett tresiffrigt tal")
elif tal < 0:
  print(tal, "är negativt")
else:
  print(tal, "är minst ett fyrsiffrigt tal")