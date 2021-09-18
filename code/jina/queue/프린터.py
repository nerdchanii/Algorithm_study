def solution(priorities, location):
    answer = []

    # [인덱스, 우선순위값] 리스트 생성
    ip = [[i, p] for i, p in enumerate(priorities)]
    
    # answer 리스트에 우선순위에 따라 출력하는 순서대로 인덱스값 넣어줌
    while len(answer) != len(priorities):

        # 판단해야 하는 요소를 factor로 지정
        factor = ip.pop(0)

        # 우선순위가 최대가 아니라면 ip에 맨 끝으로 추가
        if ip and factor[1] < max([i[1] for i in ip]):
            ip.append(factor)
        
        # 우선순위가 최대라면 answer값에 인덱스값을 추가
        else: 
            answer.append(factor[0])

            # answer에 넣어준 값이 location 값과 같으면 len(answer)는 원하는 문서의 인쇄 차례이므로 return
            if answer[-1] == location: 
                return len(answer)
