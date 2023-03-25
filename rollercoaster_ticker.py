print("Welcome to the rollercoaster!")
height = int(input("What is your height in cms? "))

bill = 0

if height >= 120:
  age = int(input("What is your age? "))

  if age < 12:
    bill = 5
    print(f"Child tickets are ${bill}.")

  elif age <18:
    bill = 7
    print(f"Youth tickets are ${bill}.")

  elif age >= 45 & age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")

  else:
    bill = 12
    print(f"Adult tickets are ${bill}.")

  photo = input("Do you wanty to take a photo? Y or N. ")
  if photo == "Y":
    bill += 3                                                  #Add $3 to bill.
    print(f"Your final bill is ${bill}")
    print(f"Enjoy your ride!")

  else:
    print(f"Enjoy your ride!")
    
else:
  print("Sorry, You have to grow taller before you can ride! :( ")
