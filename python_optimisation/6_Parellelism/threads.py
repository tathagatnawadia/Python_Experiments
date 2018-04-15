'''
When to use what - 

1. Threads = I/O Bound, Traditional drivers and networking

2. Processes = CPU bound, not a lot of communication

3. asyncio = Many connections, have async drivers
'''


from collections import namedtuple
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen
import json

User = namedtuple('User', 'login named joined')

def user_info(login):
	# Get user info from Github API
	fp = urlopen('https://api.github.com/users/{}'.format(login))
	reply = json.load(fp)
	return User(login, reply['name'], reply['created_at'])

def users_info_notparallel(logins):
	# Non parellel version of getting the info of the usernames
	return [user_info(login) for login in logins]

def users_info_parallel(logins):
	# Threaded version of getting the info of the usernames
	with ThreadPoolExecutor() as pool:
		return list(pool.map(user_info, logins))


if __name__ == '__main__':
	logins = [
		'tathagatnawadia',
		'rahul',
		'siraj',
		'mayank'
	]

'''
In [9]: %time users_info_notparallel(logins)
CPU times: user 62.1 ms, sys: 6.21 ms, total: 68.3 ms
Wall time: 4.8 s
Out[9]: 
[User(login='tathagatnawadia', named='Tathagat Nawadia', joined='2013-11-17T03:50:01Z'),
 User(login='rahul', named='Rahul Sarika', joined='2011-06-18T11:38:36Z'),
 User(login='siraj', named='Siraj Razick', joined='2008-05-21T08:13:53Z'),
 User(login='mayank', named='Mayank', joined='2012-09-06T18:44:03Z')]

Wall Time. >> CPU Time (Need threading)
Most of the time is spent in the network operations

 In [10]: %prun -l 20 users_info_notparallel(logins)
         4005 function calls in 4.829 seconds

   Ordered by: internal time
   List reduced from 223 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        4    2.378    0.595    2.378    0.595 {method 'do_handshake' of '_ssl._SSLSocket' objects}
        8    1.205    0.151    1.205    0.151 {method 'read' of '_ssl._SSLSocket' objects}
        4    1.133    0.283    1.133    0.283 {method 'connect' of '_socket.socket' objects}
        4    0.053    0.013    0.053    0.013 {built-in method _socket.getaddrinfo}
        4    0.039    0.010    0.039    0.010 {method 'set_default_verify_paths' of '_ssl._SSLContext' objects}

In [12]: %time users_info_parallel(logins)
CPU times: user 58.5 ms, sys: 8.26 ms, total: 66.8 ms
Wall time: 1.16 s
Out[12]: 
[User(login='tathagatnawadia', named='Tathagat Nawadia', joined='2013-11-17T03:50:01Z'),
 User(login='rahul', named='Rahul Sarika', joined='2011-06-18T11:38:36Z'),
 User(login='siraj', named='Siraj Razick', joined='2008-05-21T08:13:53Z'),
 User(login='mayank', named='Mayank', joined='2012-09-06T18:44:03Z')]


 In [13]: %prun -l  20 users_info_parallel(logins)
         339 function calls in 1.225 seconds

   Ordered by: internal time
   List reduced from 65 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       29    1.224    0.042    1.224    0.042 {method 'acquire' of '_thread.lock' objects}
        4    0.000    0.000    0.000    0.000 {built-in method _thread.start_new_thread}
        4    0.000    0.000    0.028    0.007 thread.py:119(_adjust_thread_count)
       11    0.000    0.000    0.000    0.000 threading.py:215(__init__)
        6    0.000    0.000    1.224    0.204 threading.py:263(wait)
'''
