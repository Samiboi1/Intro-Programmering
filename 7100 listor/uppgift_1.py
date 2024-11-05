import random
tärningar = []
for i in range(10):
  tärningar.append(random.randint(1,6))
print(tärningar)
tärningar.sort()
print("sorterad: ", tärningar)
print("summa", sum(tärningar))
medel = sum(tärningar) / len(tärningar)
print("medel: ", medel)
print("min", min(tärningar))
print("max", max(tärningar))
antal_sexor = 0
for tärning in tärningar:
  if tärning == 6:
    antal_sexor = antal_sexor + 1
print("antal sexor:", antal_sexor)