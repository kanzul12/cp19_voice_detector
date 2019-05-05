p=int(input("Enter the Number of pennies : "))
n = int(input("Enter the Number of nickels : "))
dimes = int(input("Enter the Number of dimes : "))
quarters =int(input("Enter the Number of quarters : "))
p1=p*1
n1=n*5
dimes1=dimes*10
quarters1=quarters*25

total=p1+n1+dimes1+quarters1
cash= total//100
change= total-cash*100
computeValue=(p1,n1,dimes1,quarters1)
print("You entered")
if (p1 == 1):
  print ("You have exactely 1 dollar")
elif (p1 < 1):
  print ("You have",pennies1,"which is less than 1 dollar")
elif (p1 > 1):
  print ("p:",p1,"\nn:",n1,"\ndimes:",dimes1,
        "\nquarters:",quarters1,"\nYou have",p1,"dollars and",p1,"cents")

