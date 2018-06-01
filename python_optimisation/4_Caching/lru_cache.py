from crypt import crypt
from functools import lru_cache 

salt = 'myperfectsalt'

users = {
	crypt('pass1', salt): 'user1',
	crypt('pass2', salt): 'user2',
	crypt('pass3', salt): 'user3',
}

# When we %timeit user_from_key('user2')
# Adding LRU cache decreases the time for access
@lru_cache(maxsize=1024)
def user_from_key(key):
	enc_key = crypt(key, salt)
	return users.get(enc_key)