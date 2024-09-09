text = input("Vilken månad är du född?")
if text == "december" or text == "januari" or text == "februari" or text == "December" or text == "Januari" or text == "Februari":
  print("Du är född under vintern")
elif text == "mars" or text == "april" or text == "maj" or text == "Mars" or text == "April" or text == "Maj":
  print("Du är född under våren")
elif text == "juni" or text == "juli" or text == "augusti" or text == "Juni" or text == "Juli" or text =="Augusti":
  print("Du är född under sommaren")
else:
  print("Du är född under hösten")