#let r=1.1
r=1.1

#the initial number is n=84
n=84

#How can I calculate the total number of infected individuals after 5 rounds of infection
#Use this math method to calculate
#x is the number of rounds. At the beginning, x=0
x=0

#I am going to calculate the total number of infected individuals after 5 rounds of infection.
#So x can not be more than 5.
while x<6:

#y is the total number of infected individuals after this round of infection.
   y=n+n*r

#Reset the "initial value" of one round of infection.
   n=y

#After one round of infection, x should equal x+1.
   x=x+1

#After 5 rounds of infection, the while loop ends.
   if x>=6:
      break

#Print the result.
print("The r rate is", str(r), ", the total number of individuals infected after 5 generations is", y)


