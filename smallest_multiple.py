import math

mult=1
for i in range(1,21):
    mult*=i//math.gcd(i,mult)

print(mult)