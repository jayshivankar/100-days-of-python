print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
if size == "S":
    sum += 15
elif size == "M":
    sum += 20
elif size == "L":
    sum += 25
    if add_pepperoni == "Y":
        if size == "S":
            sum += 2
        else:
            sum+=3:
            if extra_cheese == "Y":
                sum += 2
                else:
                 print(sum)
list()



