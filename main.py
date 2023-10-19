def future(day): #defining my function
  if day == 0: #just doing for future day 
    print("Tommorow is Monday!")
  elif day == 1:
    print("Tommorow is Tuesday")
  elif day == 2:
    print("Tommorow is Wednesday")
  elif day == 3:
    print("Tommorow is Thursday")
  elif day == 4:
    print("Tommorow is Friday")
  elif day == 5:
    print("Tommorow is Saturday")
  elif day == 6:
    print("Tommorow is Sunday")


todaysDate = int(
    input(
        "Enter the number of the day of the week!(Sunday is 0 Saturday is 6)"))
if todaysDate == 0: #just doing for present day
  print("Today is Sunday")
elif todaysDate == 1:
  print("Today is Monday")
elif todaysDate == 2:
  print("Today is Tuesday")
elif todaysDate == 3:
  print("Today is Wednesday")
elif todaysDate == 4:
  print("Today is Thursday")
elif todaysDate == 5:
  print("Today is Friday")
elif todaysDate == 6:
  print("Today is Saturday")

daysElapsed = int(input("Enter the number of days elapsed since today:"))
future((todaysDate + daysElapsed) % 7) #finding out the future date