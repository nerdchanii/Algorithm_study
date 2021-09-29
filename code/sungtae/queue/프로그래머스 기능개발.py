# 예제 1
# progresses = [93, 30, 55]
# speeds = [1, 30, 5]
# return = [2, 1]

def solution(pro, sp):
    days = [] # 총 걸리는 일수 리스트
    for i in range(len(pro)):
        if (100 - pro[i]) % sp[i]: # 일수를 구하기 위해서 나머지 연산자 사용
            days.append((100 - pro[i]) // sp[i] + 1) # 나머지가 있으면, 하루 더 일해야 함
        else:
            days.append((100 - pro[i]) // sp[i]) # 나머지가 없으면 그 스피드에 딱 맞춰서 끝남
    
    # days = [7, 3, 9]
    
    front = 1 # 큐를 위한 front 설정 ★ 굳이 rear는 필요 없음
    count = [[days[0], 1]] # 맨 처음은 무조건 1일로 시작
    while front != len(days):
        if count[-1][0] >= days[front]: # 만약 다음보다 걸린 일수가 크다면, 그 일수는 기준 프로그레스 이후로 동시에 배포되기 때문에 count += 1을 해줌
            count[-1][1] += 1
        else:
            count.append([days[front], 1]) # 기준 프로그레스보다 오래 걸리면, 다음 기준은 오래 걸린 프로그레스로 바꿈
        front += 1 # 매번 다음 인덱스를 가리켜야 함
    answer = [] # 정답 리스트
    for i in range(len(count)): # 카운트의 길이만큼 실행
        answer.append(count[i][1]) # 카운트의 1번 인덱스인 배포 수를 append 함
    return answer

# 복잡도는 O(3n) 즉, O(n)으로 추정됩니다.
