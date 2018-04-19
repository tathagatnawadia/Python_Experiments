'''
Asyncio - when we need a lot of threads and processes from 
multiple machines
nginx nodesjs are using syncio
cooperative multitasking - when the process itself that it is waitng for some i/o and lets the processor
to switch to a different thing
'''

from collections import namedtuple
from datetime import datetime
import asyncio
import json

host = 'api.github.com'
request_template = '''\
GET /users/{{}} HTTP/1.1 
HOST: {}
User-Agent: python/asyncio
Connection: Close

'''.format(host)

User = namedtuple('User', 'login named joined')

async def user_info_aio(login, acc):
	reader, writer = await asyncio.open_connection(host, 443, ssl=True)
	request = request_template.format(login)
	writer.writer(request.encode('utf-8'))

	in_body = False
	body = []

	async for line in reader:
		if

def user_info(login):
	# Get user info from Github API
	fp = urlopen('https://api.github.com/users/{}'.format(login))
	reply = json.load(fp)
	return User(login, reply['name'], reply['created_at'])

def users_info_notparallel(logins):
	# Non parellel version of getting the info of the usernames
	return [user_info(login) for login in logins]


if __name__ == '__main__':
	logins = [
		'tathagatnawadia',
		'rahul',
		'siraj',
		'mayank'
	]