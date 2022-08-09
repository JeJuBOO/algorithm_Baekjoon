# 2022 08 09 
# BOO.SK 

# Algorithm basic 1/2 in Baekjoon

N = int(input()) # 처음 명령은 총 명령의 수를 입력받음
stack = []

for _ in range(N):
    command = input().split()

    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if stack == []:
            print(-1)
        else:
            x = stack.pop()
            print(x)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)
    else:
        if stack == []:
            print(-1)
        else:
            print(stack[len(stack)-1])

