height = int(input("qual a sua altura?(em cm)"))
credits = int(input("Quantos créditos vc tem?"))

if height >= 170 and credits >= 20:
  print("Enoy the ride")
elif height < 170 and credits >= 20:
  print("You are not tall enought")
elif height >= 170 and credits < 20:
  print("You don't have enough credits")
else:
  print("You have not met either requirement")
