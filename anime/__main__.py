#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Anton'
act = '486a04e13816cc7561a3ad768a8b94b0f926dede8d92436bbd8ac0c225bb9060e15ef64330c0aece4eff1'
import vk
import requests
import json
import time
import sys
from os import listdir, rename
from os.path import isfile, join
from time import sleep
from datetime import date, datetime, timedelta

def send(at, name, msg):
    try:
        vkapi = vk.API(access_token=at)
        toSend = vkapi.photos.getMessagesUploadServer()  # (chat_id=37)
        r = requests.post(toSend['upload_url'], files={'photo': open(name, 'rb')})
        dc = json.loads(r.text)
        photoInfo = vkapi.photos.saveMessagesPhoto(server=dc['server'], photo=dc['photo'], hash=dc['hash'])[0]
        vkapi.messages.send(message=msg, attachment='photo'+str(photoInfo['owner_id'])+'_'+str(photoInfo['id']), chat_id='37')
        return True
    except:
        return False

mypath = u'C:/Users/Антон/Pictures/EBIN/'
mypath = sys.argv[1]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and not('posted3' in f)]
left = len(onlyfiles)
msgFormat = u'осталось: {}, до семестровочки: {}'
kol = 0
for i in onlyfiles:
    f = datetime(2015, 5, 21, 9, 0, 0) - datetime.now()
    b = send(act, mypath+'/'+i, msgFormat.format(left-1, str(f)[:8]))
    if b:
        kol += 1
        left -= 1
        rename(mypath+'/'+i, mypath+'/'+'posted-'+i)
        print('posted ' + str(kol) + ' ' + time.strftime('%H:%M:%S', time.localtime()) + ' left ' + str(left))
    sleep(40)
print onlyfiles
