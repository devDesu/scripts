import vk
from time import sleep


act = 'вставл€й сюда токен'
vkapi = vk.API(vk.Session(access_token=act))
for i in range(1000000):
	vkapi.wall.restore(owner_id=-118751377,post_id=i)
	if i%4 == 0:
		sleep(3)