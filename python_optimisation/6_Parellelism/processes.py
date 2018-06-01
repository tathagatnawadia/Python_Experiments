'''
Processes allow utiliztion of all the cores of the machine
Cost - cost of communication > serilize and deseralize data 
between 2 processes (called IPC) via pipes/sockets
  
So we compress some data and decompress it
'''

from concurrent.futures import ProcessPoolExecutor
# Compression library
import bz2

def unpack(requests):
	return [bz2.decompress(request) for request in requests]

def unpack_proc(requests):
	with ProcessPoolExecutor() as pool:
		return list(pool.map(bz2.compress, requests))

if __name__ == '__main__':
	with open('somedata.htm', 'rb') as fp:
		data = fp.read()

	bz2data = bz2.compress(data)
	# Compression ratio
	# print(len(bz2data) / len(data))
	# print(bz2.decompress(bz2data) == data)

	requests = [bz2data] * 300


'''
We notice that the wall time is comparable to CPU time

In [25]: %time _ = unpack(requests)
CPU times: user 8.3 s, sys: 171 ms, total: 8.47 s
Wall time: 8.49 s

In [26]: %prun -l 20 _ = unpack(requests)
         1205 function calls in 8.440 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      300    8.422    0.028    8.422    0.028 {method 'decompress' of '_bz2.BZ2Decompressor' objects}
        1    0.010    0.010    8.440    8.440 <string>:1(<module>)
        1    0.004    0.004    8.430    8.430 processes.py:14(<listcomp>)

Not we try to make the decompress method on multi process

In [28]: %prun -l 20 _ = unpack_proc(requests)
         17658 function calls in 1.819 seconds

   Ordered by: internal time
   List reduced from 153 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      753    1.753    0.002    1.753    0.002 {method 'acquire' of '_thread.lock' objects}
        8    0.011    0.001    0.011    0.001 {built-in method posix.fork}
      301    0.007    0.000    0.007    0.000 {built-in method posix.write}
        1    0.005    0.005    1.819    1.819 <string>:1(<module>)
'''

