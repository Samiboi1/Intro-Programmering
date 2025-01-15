def celsiusTofahrenheit(celsius):
  return (9/5) * celsius + 32
celsius = float(input("Ange temperaturen i grader celsius:"))
print("Det är", celsiusTofahrenheit(celsius), "grader fahrenheit")