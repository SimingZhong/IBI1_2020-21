a=101202
b=190784
c=100321
d=a-c
e=a-b
if d>e:
  print("d is greater")
elif d<e:
  print("e is greater")
else:
  print("d is equal to e")


X=True
Y=False
Z=(X and not Y) or (Y and not X)
print(Z)
