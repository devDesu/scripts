def nod(a,b):
    temp = []
    temp.append(max(a,b))
    temp.append(min(a,b))
    n = 1
    while temp[len(temp)-1] != 0:
        temp.append(temp[n-1]%temp[n])
        n+=1
    return temp[-2]

i1 = 1000000
i2 = 1500000
gMx = 0
mxI = 0
for i in range(i1, i2+1):
    mx = nod(i, 865546)
    if mx > gMx:
        mxI = i
        gMx = mx

print(mxI, gMx)
