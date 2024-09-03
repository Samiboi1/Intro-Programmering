tal1 = float(input("Mata in ett tal: "))
tal2 = float(input("Mata in ett till tal: "))
tal3 = float(input("Mata in ännu ett till tal: "))
if tal1 < tal2 and tal2 < tal3:
  print(tal1, tal2, tal3)
elif tal1 < tal3 and tal3 < tal2:
  print(tal1, tal3, tal2)
elif tal2 < tal1 and tal1 < tal3:
  print(tal2, tal1, tal3)
elif tal2 < tal3 and tal3 < tal1:
  print(tal2, tal3, tal1)
elif tal3 < tal1 and tal1 < tal2:
  print(tal3, tal1, tal2)
else:
  print(tal3, tal2, tal1)