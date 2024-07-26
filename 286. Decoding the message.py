#  286. Расшифровка сообщения

import sys 


l_n = {'z':0,
       'a':1,
       'b':2,
       'c':3,
       'd':4,
       'e':5,
       'f':6,
       'g':7,
       'h':8,
       'i':9,
       'j':10,
       'k':11,
       'l':12,
       'm':13,
       'n':14,
       'o':15,
       'p':16,
       'q':17,
       'r':18,
       's':19,
       't':20,
       'u':21,
       'v':22,
       'w':23,
       'x':24,
       'y':25
}

n_l = {}
for sym in l_n.keys():
    n_l[l_n[sym]] = sym

words_from_the_book = {}
words = sys.stdin.readline().strip().split()
for word in words:
    if len(word) not in words_from_the_book:
        words_from_the_book[len(word)] = set()
    words_from_the_book[len(word)].add(word)

n = int(input())
for _ in range(n):
    inp_word = sys.stdin.readline().strip()
    for k in range(0, 26):
        current_word = []
        for sym in inp_word:
            current_word.append(n_l[(l_n[sym] + k) % len(l_n)])
        current_word = ''.join(current_word)
        if current_word in words_from_the_book[len(current_word)]:
            sys.stdout.write(current_word)
            print()
            break
    