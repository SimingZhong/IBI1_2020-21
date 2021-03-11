#The first two places in the sequence are 1,1.
a = 1
b = 1

#Now the sequence is in its second place.
n = 2

#In the Fibonacci sequence, each number is the sum of the previous two numbers
#I want to use while loop, but I don't want to set any condition in the first line.

while 1 == 1:

#We know the previous two numbers now, so we calculate the next number (the sum of them).

    c = a+b
#Reset the value of "the previous two numbers", so we can let the while loop go on with no gap.

    a = b
    b = c

#Now the sequence go on to its next place.

    n = n+1

#Fibonacci calculated this sequence up to its 13 place
    if n == 13:
       break

print("The 13th value of this Fibonacci sequence is:", c)
