import random
tärningar = []
antal_ettor = 0
for i in range(5):
  tärningar.append(random.randint(1,6))
for tärning in tärningar:
    if tärning == 1:
      antal_ettor = antal_ettor + 1
print(tärningar)
print(antal_ettor)