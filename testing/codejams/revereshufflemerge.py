from itertools import permutations, combinations
import sys

def shuffle(S):
	perms = [''.join(p) for p in permutations(S)]
	return perms
def reverse(S):
	return S[::-1]

def merge(S1, S2):
# S1 is string
# S2 is list
	S3 = S1 + S2
	return shuffle(S3)

def reverseShuffleMerge(A):
	return merge(reverse(A), shuffle(A))
def checkForAllZero(letter_dictionary):
	valid = True
	for key, value in letter_dictionary.items():
		if value != 0:
			valid = False
			break
	return valid
def splitWordsLexicographically(word, letter):
	reverse_word = reverse(word)
	j = 0
	match = False
	for i in reverse_word:
		if i == letter:
			match = True
			break
		j = j + 1
	if match == True:
		return reverse(reverse_word[j:])
	else:
		return None

import collections,string, copy
S = input("Enter a string : ")
S_letters = collections.Counter(S)
invalid = False
A_partial = ""
for key, value in S_letters.items():
	if value % 2 != 0:
		invalid = True
	else:
		for i in range(int(value/2)):
			A_partial = A_partial + key

if invalid == True:
	print("Entered string not valid")
	sys.exit(0)

A_partial_letters = collections.Counter(A_partial)
A_partial_alphabets = list(A_partial_letters.keys())

# A = ""
# satisfy_counter = copy.deepcopy(A_partial_letters)
# print(S)
# for i in S:
# if i in A_partial_alphabets and satisfy_counter[i] != 0:
# A = A + i
# satisfy_counter[i] = satisfy_counter[i] - 1
# print("Answer", reverse(A))

for i in list(string.ascii_lowercase):
	sample = splitWordsLexicographically(S, i)
	if sample != None:
		#print(sample)
		A = ""
		satisfy_counter = copy.deepcopy(A_partial_letters)
		for i in sample:
			if i in A_partial_alphabets and satisfy_counter[i] != 0:
				A = A + i
				satisfy_counter[i] = satisfy_counter[i] - 1
		print(i," ---> " , sample, " --> " ,satisfy_counter, " ---> ",reverse(A))

