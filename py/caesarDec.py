#--encoding=utf-8

def dec(alphabet, st, k):
    temp = []
    for f in st:
        if f==u'.':
            temp.append(u'.')
        elif f==u' ':
            temp.append(u' ')
        elif f==u',':
            temp.append(u',')
        else:
            temp.append(alphabet[(alphabet.find(f)-k+len(alphabet)) % len(alphabet)])
    return temp

alph = u'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
st = u'ЭРБИБДГ'
for i in range(1, 30):
    print ''.join(dec(alph, st, i))
