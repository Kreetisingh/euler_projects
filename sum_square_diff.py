sq,sum=0,0
for i in range(1,101):
    sum,sq=sum+i,sq+(i**2)
print((sum**2)-sq)
