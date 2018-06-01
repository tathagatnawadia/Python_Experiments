'''
Goal : Keep computation cache between program runs
E.g. data analysis
Redis, Memcached can store but lose data when restarted
Enter - joblib - ondisk caching & parellel computing
'''

'''
Edit Distance Program
pip install joblib
pip install edit_distance 

Usage:
> LDistance = edit_distance.SequenceMatcher(a="mango", b="manga").distance()
'''

from joblib import Memory
from os.path import expanduser

import edit_distance ad Levenshtein

# Memory object for caching on disk
memory = Memory(expanduser('./.cache/spell'), verbose=0)

# We cache load_words using the decorator
@memory.cache
def load_words():
	with open('words.txt') as fp:
		return tuple(line.strip().lower() for line in fp)

@memory.cache
def spell(word, count=10, dict_words=None):
	dict_words = load_words() if dict_words is None else dict_words
	return sorted(dict_words, key:lambda dw: Levenshtein(word, dw))