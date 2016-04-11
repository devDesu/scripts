def enters(delta, num):
    return num % delta == 0

ar = []
n = int(input())
fool = True
dt = 0
for i in range(0,n):
    ar.append(int(input()))
dt = ar[1]-ar[0]
for i in ar:
    fool = False if not enters(dt, i) else True
print fool
1+2)
