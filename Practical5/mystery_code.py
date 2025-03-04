# What does this piece of code do?
# Answer: This code prints a random number between 1 and 50 (include 1 and 50).

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil


p=False
while p==False:
	p = True
	n = randint(1,100)
	if n > 50:
		p = False
#If n <= 50, this while loop will not end. And n will not be printed.
print(n)
