a=2
b=3
for x in range(10000):
    b=b+4/(a*(a+1)*(a+2))-4/((a+2)*(a+3)*(a+4))
    a=a+4
print(b)