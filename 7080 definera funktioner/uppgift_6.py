tal1 = float(input("Skriv ett tal: "))
def heltal(tal1):
  if tal1 % 2 == 0:
    return "Talet är jämnt"
  elif tal1 % 2 == 1:
    return "Talet är udda"
print(heltal(tal1))