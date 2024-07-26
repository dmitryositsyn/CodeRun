#  213. Автодополнение

num_words = int(input())

answer = 0
trie = {}

for word in input().split(" "):
	root = trie
	for c in word:
		if c not in root:
			root[c] = {}
		root = root[c]
		answer += 1

		if "memorized_word" not in root:
			root["memorized_word"] = word
		elif root["memorized_word"] == word:
			break
		else:
			root["memorized_word"] = None

print(answer)