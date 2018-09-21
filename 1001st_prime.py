
def isprime(n):
    if n%2==0:return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

c=3
i=1
while i!=10001:
    if isprime(c):
        i+=1
    c+=1
print(c-1)


