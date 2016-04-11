import string

def mtf(to_sort,slov,fl):
    result = []
    for i in to_sort:
        ind=slov.index(i)
        temp = slov[ind]
        slov.remove(temp)
        slov.insert(0,temp)
        result.append(ind)
        fl.write(ind)
    return result

slov = list(string.lowercase[:])
to_sort = open('d2.txt','r')
to_sort = to_sort.readlines()[0]
rest = open('output.txt', 'w')
result = mtf(to_sort,slov,rest)
rest.close()
