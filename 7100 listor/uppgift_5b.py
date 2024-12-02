import random
tärningar = []
antal_ettor = 0
for i in range(5):
  tärningar.append(random.randint(1,6))
if tärningar[0] == tärningar[1] and tärningar[0] == tärningar[2] and tärningar[0] == tärningar[3] and tärningar[0] == tärningar[4]:
  print("Yatzy!")
else:
  print("Inte yatzy")
print(tärningar)