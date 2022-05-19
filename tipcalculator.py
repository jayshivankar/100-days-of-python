print("Welcome to the tip calculator!")
a = int(input("What was the total bill ? $ "))
b = int(input("How much tip would you like to give ? 10,12,15? "))
c = int(input("How many people to split the bill? "))
totalbill= (a/c) * b/100
print(totalbill)