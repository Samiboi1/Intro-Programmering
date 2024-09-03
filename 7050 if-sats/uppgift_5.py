tal1 = float(input("Mata in ett tal: "))
tal2 = float(input("Mata in ett till tal: "))
tal3 = float(input("Mata in ännu ett till tal: "))
if tal1 < tal2 and tal1 < tal3:
  print(tal1, "är minst")
elif tal2 < tal1 and tal2 < tal3:
  print(tal2, "är minst")
else:
  print(tal3, "är minst")