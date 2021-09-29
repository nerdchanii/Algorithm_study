""" 
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
"""
priorities = [1, 1, 3, 2, 1, 4, 1, 1, 3, 1, 1, 1] # 사례 1
location = int(input())

def solution(p,l):
    front = 0 # 커서 제작
    count = 0 # 가장 큰 숫자 세면 카운팅
    m = max(p) # 초기 가장 큰 값 설정
    while True:
        
        # 가장 큰 값을 찾아내어 0으로 치환했을 때, 센 것으로 간주하여 함수 출력
        if p[l] == 0:
            return count
        
        # 가장 큰 값과 커서값이 겹칠 때
        if m == p[front]:
            count += 1 # 찾은 것이기 때문에 count + 1
            p[front] = 0
            m = max(p)
            
        # 커서 이동
        front += 1
        
        # 커서가 넘어가면 처음부터
        if front == len(p):
            front = 0

print(solution(priorities, location))
