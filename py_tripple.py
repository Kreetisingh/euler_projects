

print([x[0]*x[1]*x[2] for x in [(a,b,1000-b-a) for a in range(1,1000) for b in range(a+1,1000)] if x[0]**2 + x[1]**2==x[2]**2])
