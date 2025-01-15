def KelvinTofahrenheit(Kelvin):
  return (Kelvin - 273.15) * 1.8 + 32
Kelvin = float(input("Ange temperaturen i grader Kelvin:"))
print("Det är", KelvinTofahrenheit(Kelvin), "grader fahrenheit")