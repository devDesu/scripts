#!/usr/bin/python3
# -*- coding: utf-8 -*-

import vk
import psycopg2 as dbapi2
db = dbapi2.connect("host=localhost dbname=vk user=postgres password=123987")
cur = db.cursor()
act = 'c5a59372cd5c438ccf510ea7a55f3254bbecf94e4f29a96515b7f528e19aca19ecd7b54c84a0cb178a976'
api = vk.API(vk.Session(access_token=act))


def getBatch(api, cur, g_id, ofst, name, db):
	members = api.groups.getMembers(group_id=g_id, sort="id_asc", count=1000, offset=ofst, fields="sex,relation")
	# members = api.execute.get_members_optimized(id=g_id, cur_len=0, total_len=t_l, v='5.59')
	# members = members.split(',')[:-1]
	for m in members['users']:
		if m['sex'] == 1:
			sex = 1
		else:
			sex = 0
		try:
			relation = m['relation']
		except Exception:
			relation = -1
		fio = m['first_name']+' '+m['last_name']
		fio = fio.replace("'", "`")
		try:
			cur.execute("""INSERT INTO users(id, fio, sex, relation, group_name)
				       VALUES({}, '{}', {}, {}, '{}')""".format(m['uid'],
				       fio, sex, relation,
				       name))
		except dbapi2.IntegrityError as e:
			db.rollback()

def fill_group(api, db, cur, group_name, current=0):
	info = api.groups.getById(group_id=group_name, fields='members_count')
	print(info)

	total = info[0]['members_count']
	g_id = info[0]['gid']
	while(current < total):
		getBatch(api, cur, g_id, current, info[0]['screen_name'], db)
		db.commit()
		current += 1000
		print(current, '/', total)

def get_group_members(cur, group_name):
	cur.execute("""SELECT * FROM users WHERE group_name='{}' AND sex=1 AND relation NOT IN (2, 3, 4, 5, 7)""".format(group_name))
	# 6 - active search, -1 not stated
	re = set()
	rows = cur.fetchall()
	for row in rows:
		re.add(row[0])
	return re

#fill_group(api, db, cur, 'emoboys')
am = get_group_members(cur, 'abstract_memes')
rd = get_group_members(cur, 'russdeath')
emo = get_group_members(cur, 'emoboys')
inter = iter(am & rd & emo)
#print(len(inter))
for i in range(100):
	print(next(inter))
