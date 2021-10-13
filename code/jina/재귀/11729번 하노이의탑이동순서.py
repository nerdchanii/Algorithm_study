N = int(input())

# K는 N개의 탑을 1번에서 3번으로 옮기는 횟수
# N-1개의 탑을 1번에서 2번으로 옮기는 횟수 + N번째 판을 1번에서 3번으로 옮기기(1번) + N-1개 탑을 2번에서 3번으로 옮기는 횟수
# 1개를 옮기는 횟수는 1
# 2개를 옮기는 횟수는 1+1+1 = 3
# N-1개를 옮기는 횟수는 2**(N-1) -1
# N개를 옮기는 횟수는 2**N -1

K = 2**N - 1
print(K)

def hanoi(N): # 하노이 탑 이동 수행 과정
    # 1번에 1개의 판만 있는 경우 
    if N == 1:
        process = [[1,3]]
        return process

    # 1번에 2개 이상의 판이 있는 경우
    else:
        process = []

        # N-1개 판을 3번으로 옮기는 경우는 hanoi(N-1)
        # top은 요소를 2개 가지는 리스트 형태
        # 우선 N-1개 판을 먼저 2번으로 옮겨야 하므로 hanoi(N-1)의 리스트들을 탐색해서 2와 3을 바꿔줌 
        for top in hanoi(N-1):
            new = []
            if top[0] == 2:
                new.append(3)
            elif top[0] == 3:
                new.append(2)
            else:
                new.append(1)
            if top[1] == 3:
                new.append(2)
            elif top[1] == 2:
                new.append(3)
            else:
                new.append(1)
            process.append(new)
        
        # N-1개의 판은 2번에 옮겨진 상태고 1번에 있는 N번째 판을 3번에 옮겨야 하므로 [1,3] 추가
        process.append([1,3])

        # 2번에 있는 N-1개의 판을 3번으로 옮겨야 하므로 hanoi(N-1)의 리스트들을 탑색해서 1과 2를 바꿔줌
        for top in hanoi(N-1):
            new = []
            if top[0] == 2:
                new.append(1)
            elif top[0] == 1:
                new.append(2)
            else:
                new.append(3)
            if top[1] == 1:
                new.append(2)
            elif top[1] == 2:
                new.append(1)
            else:
                new.append(3)
            process.append(new)
        return process

for h in hanoi(N):
    print(' '.join(map(str, h)))
