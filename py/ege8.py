ar = []
checksum = 0
ECheck = 0
max14 = 0
max14i = 0
maxN14 = 0
n = int(input())
for i in range(0, n):
    h = int(input())
    ar.append(h)
    if h % 14 != 0:
        if maxN14<h:
            maxN14 = h

    else:
        if max14i<h<max14:
            max14i = h
        elif max14<h:
            max14 = h
ECheck = int(input())
print max(max14i*max14, max14*maxN14)==ECheck
