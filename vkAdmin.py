#'pip install vk' to work properly

import vk
import re
from time import sleep
	
pattern = "v\d+([0-9]{3})\/"
regex = re.compile(pattern, flags=re.I|re.U)


def getAlbum(client, group):
    ofst = 0
    ret = client.photos.getAlbums(owner_id=group, need_system=1, offset=ofst)
    ret =ret['items']
    for i in ret:
        if i['id']<0:
            return i['id']


def getOldestPic(client, group, album):
    ofst = 0
    ret = client.photos.get(owner_id=group, album_id=album, offset=ofst, count=100)
    while ret['count'] == 100:
        ofst += 100
        ret = client.photos.get(owner_id=group, album_id=album, offset=ofst, count=100)
    ret = ret['items'][0]
    for key in ret:
        if 'photo' in key:
            return(ret[key])


def proceedUsers(client, group, needed, out, ofs):
    ofst = ofs
    ret = client.groups.getMembers(group_id=group, count=400, offset=ofst, sort='id_asc')
    it = ret['items']
    total = ret['count']
    while len(it)>0:
        f = open(out, 'a')
        for i in it:
            if str(i)[-3:]==needed:
                print >>f, '<a href="https://vk.com/id{k}">id{k}</a><br>'.format(k=str(i))
        f.close()
        ofst += 400
        ret = client.groups.getMembers(group_id=group, count=400, offset=ofst, sort='id_asc')
        it = ret['items']
        sleep(2)
        print 'done: {}, total: {}'.format(ofst, total)
    f = open(out, 'a')
    f.write('</body></html>')
    f.close()


def menu():
    f = open('config.txt', 'r')
    temp = f.readlines()
    f.close()
    needed = 0
    ofs = 0
    contin = raw_input('Maybe your already know last 3 digits(type y to confirm): ')
    if contin is 'y':
        needed = int(raw_input('digits: '))
        ofs = int(raw_input('needed offset: '))
    return int(temp[1]), temp[0][:-1], ofs, needed
    

group_id, tken, ofs, needed = menu()
client = vk.API(access_token=tken)
if ofs == 0 and needed == 0:
    album_id = getAlbum(client, group_id)
    print album_id
    oldest = getOldestPic(client, group_id, album_id)
    print oldest
    needed = regex.search(oldest).group(1)
    print needed
    f = open('results.html', 'w')
    f.write('<html><body>')
    f.close()
proceedUsers(client, str(group_id)[1:], str(needed), 'results.html', ofs)
