lista = ['ananas', 'avokado', 'bakpulver', 'potatis', 'ostkaka']

antalA = 0
for a in lista:
  for bokstav in a:
    if (bokstav == 'a'):
      antalA = antalA + 1
print('Antal A:', antalA)