def fahrenheitTocelsius(fahrenheit):
  return (5/9) * (fahrenheit - 32)
fahrenheit = float(input("Ange temperaturen i grader fahrenheit:"))
print(fahrenheitTocelsius(fahrenheit))