def tue(it):
    temp = []
    for i in it:
        if i:
            temp.append(1)
            temp.append(0)
        else:
            temp.append(0)
            temp.append(1)
    return temp

print "starting..."
f = [0b1]
for k in range(0,8):
	print(f)
	f = tue(f)
print f[235:240]
