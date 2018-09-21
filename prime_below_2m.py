def isprime(n):
    if n%2==0:return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

n=1
sum=0
while n<2000000:
    n+=2
    if isprime(n):
        sum+=n


print(sum+2)



