#The first two places in the sequence are 1,1.
a = 1
b = 1
n = 2
#In the Fibonacci sequence, each number is the sum of the previous two numbers
while 1 == 1:
    c = a+b
    a = b
    b = c
    n = n+1
#Fibonacci calculated this sequence up to its 13 place
    if n == 13:
       break
print("The 13th value of this Fibonacci sequence is:", c)
