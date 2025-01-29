import random
antalSexor = 0

tärningar = []
for i in range(10):
  tärningar.append(random.randint(1,6))

for sexor in tärningar:
  if (sexor == 6):
    antalSexor = antalSexor + 1

print('tärningskasten: ', tärningar)
print('sorterad: ', sorted(tärningar))
print('summa: ', sum(tärningar))
print('medel: ', sum(tärningar)/len(tärningar))
print('minsta: ', min(tärningar))
print('största: ', max(tärningar))
print('antal sexor: ', antalSexor)