# Stack 구현
# 백준 탑 - https://www.acmicpc.net/problem/2493
# memory: 
# time: timeover
def timeover(stack):
    answer = [0]*len(stack)
    while True:
        # 레이저 개수만큼 송수신 위치 확인되면 break
        if len(stack) == 1:
            break
        # 가장 끝 원소 pop해서 레이저 송신한다.
        send = stack.pop(-1)
        for idx in range(len(stack)-1, -1, -1):
            if stack[idx] > send:
                # print(idx, ":", stack[idx])
                answer[len(stack)] = idx+1
                break
    return answer

# num 개수만큼만 입력을 받는다.
num = int(input())
nums = list(map(int, input().split()))
print(*timeover(nums)) # answer list 원소들로만 출력