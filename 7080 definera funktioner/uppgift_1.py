def KelvinTocelsius(Kelvin):
  return Kelvin - 273.15
Kelvin = float(input("Ange temperaturen i grader Kelvin:"))
print("Det är", KelvinTocelsius(Kelvin), "grader celsius")