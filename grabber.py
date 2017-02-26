#!/usr/bin/python3
import vk
from time import sleep

def work(curr, api):
    full = []
    cd = ''
    head = 'var gc=[];var ids=[];var cl=[];'
    for j in range(12):
        f = ','.join([str(i) for i in range(500*(curr+j), 500*(curr+j+1))])
        cd += 'var groups = API.groups.getById({"group_ids": ['+f+'], "fields": "is_closed,members_count"});\
    gc=gc+groups@.members_count;ids=ids+groups@.gid;cl=cl+groups@.is_closed;'
    curr += 12
    r = api.execute(code=head+cd+'return [gc,ids,cl];')
        # res = vkapi.groups.getById(group_ids=f, fields='members_count,ban_info')
    for i in range(len(r[0])):
        try:
            if not int(r[2][i]) and int(r[0][i])>100000:
                full.append(str(r[1][i]))
        except TypeError:
            pass
        except Exception as e:
            print(e)
    print(curr)
    full = [f for f in full if f]
    if len(full) != 0:
        with open('/home/nulluser/output.txt', 'a+') as f:
            f.write("\n"+"\n".join(full))
        # sleep(1)
    return curr

token = '00b4ff40f89bc10f7849464c749c07c0eb092484036d738aca5f400508c3027bfc082f64f63446df41ee4'
vkapi = vk.API(vk.Session(access_token=token))
c = 145342
l = 150000
while c<l:
    try:
        c = work(c,vkapi)
    except:
        sleep(10)
        c = work(c, vkapi)
