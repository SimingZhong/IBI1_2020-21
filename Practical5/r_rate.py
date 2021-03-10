#let r=1.2
r=1.2
#the initial number is n=84
n=84
#How can I calculate the total number of infected individuals after 5 rounds of infection
#Use this math method to calculate
x=0
while x<6:
   y=n+n*r
   n=y
   x=x+1
   if x>=6:
     break
print("The r rate is", str(r), ", the total number of individuals infected after 5 generations is", y)


