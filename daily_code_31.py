'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions,
deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: 
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
'''

'''
to clarfy the problem, it should be the minimum edit distance for both ways
- 'ABC' -> 'ABCD' = 1 insertion while 'ABCD' -> 'ABC' = 1 deletion
'''

def edit_distance(string1, string2):
	sub_12 = 0
	insert_12 = 0
	delete_12 = 0
	sub_21 = 0
	insert_21 = 0
	delete_21 = 0

	if len(string1) <= len(string2):
		shorter = string1
		longer = string2
	else:
		shorter = string2
		longer = string1

	#if same length, we only need to substitute and return
	if len(shorter) == len(longer):
		for i in range(len(shorter)):
			if shorter[i] != longer[i]:
				sub_12 += 1
				sub_21 += 1

	else:
		#padding 
		pad = len(longer) - len(shorter)
		shorter += '_' * pad

		for i in range(len(shorter) + 1):
			if shorter[i] == longer[i]:
				continue
			else:
				#insertion_12, deletion_21
				if shorter[i] == '_':
					#if shorter[i - 1] == longer[i] means its already counter as insertion, skip it...
					if shorter[i - 1] == longer[i]:
						insert_12 -= 1
						delete_21 -= 1
					insert_12 += 1
					delete_21 += 1
					if (i + 1) < len(longer):
						i += 1
						continue
					else:
						break
				#insertion_12, deletion_21
				elif shorter[i] == longer[i + 1]:
					insert_12 += 1
					delete_21 += 1
					i += 2
					continue
				#sub, insert, del
				elif shorter[i] != longer[i + 1]:
					sub_12 += 1
					sub_21 += 1
					#insert_12 += 1
					#delete_21 += 1
					i += 2
					continue

		shorter = shorter[ : len(shorter) - pad]

	print('minimum edit distance from {} --> {} are: insert: {}, delete: {}, sub: {}'.
		  format(shorter, longer, insert_12, delete_12, sub_12))
	print('minimum edit distance from {} --> {} are: insert: {}, delete: {}, sub: {}'.
		  format(longer, shorter, insert_21, delete_21, sub_21))
	print(" ")


string1 = 'abc'
string2 = 'abd'
edit_distance(string1, string2)
'''
minimum edit distance from abc --> abd are: insert: 0, delete: 0, sub: 1
minimum edit distance from abd --> abc are: insert: 0, delete: 0, sub: 1
'''
string3 = 'abd'
string4 = 'abcd'
edit_distance(string3, string4)
'''
minimum edit distance from abd --> abcd are: insert: 1, delete: 0, sub: 0
minimum edit distance from abcd --> abd are: insert: 0, delete: 1, sub: 0
'''
string5 = 'abc'
string6 = 'abde'
edit_distance(string5, string6)
'''
minimum edit distance from abc --> abde are: insert: 1, delete: 0, sub: 1
minimum edit distance from abde --> abc are: insert: 0, delete: 1, sub: 1
'''
edit_distance('abc', 'cba')
'''
minimum edit distance from abc --> cba are: insert: 0, delete: 0, sub: 2
minimum edit distance from cba --> abc are: insert: 0, delete: 0, sub: 2
'''
string7 = 'abcd'
string8 = 'efghij'
edit_distance('abcd', 'efghij')
'''
minimum edit distance from abcd --> efghij are: insert: 2, delete: 0, sub: 4
minimum edit distance from efghij --> abcd are: insert: 0, delete: 2, sub: 4
'''



