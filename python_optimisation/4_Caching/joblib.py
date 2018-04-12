'''
Goal : Keep computation cache between program runs
E.g. data analysis
Redis, Memcached can store but lose data when restarted
Enter - joblib - ondisk caching & parellel computing
'''

'''
Edit Distance Program
pip install joblib
pip install Levenshtein
'''

from joblib import Memory
from os.path import expanduser

from Levenshtein import distance as levenshtein

memory = Memory(expanduser('./.cache/spell'), verbose=0)

@memory.cache
def load_words():
	with open