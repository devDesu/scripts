#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
__author__ = 'Desu'
act = ''
import vk
import requests
import json
import time
import random
from os import listdir, rename
from os.path import isfile, join
from time import sleep
from datetime import date, datetime, timedelta

def send(at, name, msg):    
        vkapi = vk.API(vk.Session(access_token=at))
        toSend = vkapi.photos.getMessagesUploadServer()  # (chat_id=37)
        r = requests.post(toSend['upload_url'], files={'photo': open(name, 'rb')})
        dc = json.loads(r.text)
        photoInfo = vkapi.photos.saveMessagesPhoto(server=dc['server'], photo=dc['photo'], hash=dc['hash'])[0]
        #print(str(photoInfo['id']))
        vkapi.messages.send(message=msg, attachment=str(photoInfo['id']), chat_id='37')
        return True

mypath = u'C:/Users/Антон/Pictures/EBIN/'
mypath = sys.argv[1]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and not('posted2' in f)]
left = len(onlyfiles)
msgFormat = u'осталось: {}, до семестровочки: {} :'
#print(mypath, onlyfiles)
kol = 0
for i in onlyfiles:
    f = datetime(2015, 12, 11, 12, 0, 0) - datetime.now()
    #print(str(f))
    b = send(act, mypath+'/'+i, msgFormat.format(left-1, str(f)[:8])+random.randint(2,5)*')')
    #b = True
    if b:
        kol += 1
        left -= 1
        rename(mypath+'/'+i, mypath+'/'+'posted-'+i)
        print('posted2-' + str(kol) + ' ' + time.strftime('%H:%M:%S', time.localtime()) + ' left ' + str(left))
    sleep(random.randint(20, 35))
#print(onlyfiles)
