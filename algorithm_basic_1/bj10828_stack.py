# 2022 08 09 
# BOO.SK 

# Algorithm basic 1/2 in Baekjoon
# 1차시 : 시간 초과로 size 함수제거하고 사이즈를 변수로 저장
# 2차시 : input() 함수의 시간이 오래걸린다 하여 sys.stdin.readline()로 변경

import sys

N = int(sys.stdin.readline()) # 처음 명령은 총 명령의 수를 입력받음
stack = []
stack_size = 0

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.append(int(command[1]))
        stack_size += 1

    elif command[0] == 'pop':
        if stack_size == 0:
            print(-1)
        else:
            x = stack.pop()
            stack_size -= 1
            print(x)

    elif command[0] == 'size':
        print(stack_size)

    elif command[0] == 'empty':
        if stack_size == 0:
            print(1)
        else:
            print(0)

    else:
        if stack_size == 0:
            print(-1)
        else:
            print(stack[stack_size-1])

