svar = int(input("Gissa vilket tal jag tänker på! "))
försök = 0
while svar != 42 and försök < 2:
  if svar < 42:
    svar = int(input("Talet är för litet. "))
    försök = försök + 1
  elif svar > 42:
    svar = int(input("Talet är för stort. "))
    försök = försök + 1
if svar == 42:
  print("Rätt")
else:
  print("God damn du är skit")