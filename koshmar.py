#!/usr/bin/python3

import vk

api = vk.API(vk.Session(access_token='5ea99a15fe26fe5a5342215147d1a02cf276c87bcd234e9d847db3d1328a0afec6eb202bc737fd5cbb4c5'))

cd = "commentsSort('own':{},'post':{},'wall':{})".format(176751029, 54072, -38124154)

api.execute(code=cd)
