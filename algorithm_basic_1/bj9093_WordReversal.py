# 2022 08 09 
# BOO.SK 

# Algorithm basic 1/2 in Baekjoon
# 9093 Word Reversal

import sys

N = int(sys.stdin.readline()) # 처음 명령은 총 명령의 수를 입력받음
reverse_word = []
for _ in range(N):
    sentence = sys.stdin.readline()
    sentence = sentence[:-1].split(' ')

    for word in sentence:
        for i in range(len(word)):
            reverse_word.append(word[len(word)-1-i])
        reverse_word.append(' ')  

    print(''.join(reverse_word[:-1]))
        

