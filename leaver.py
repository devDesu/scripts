#!/usr/bin/python3
import sys
import vk
import time
import random

token = sys.argv[1]
vk = vk.API(vk.Session(access_token=token))
id_ = int(input())
while(True):
  if vk.messages.getChat(chat_id=54)['left']:
    vk.messages.removeChatUser(chat_id=54, user_id=id_)
  time.sleep(random.randint(1,5))
