def solution(priorities, location):
    answer = 0
    # 초기 순서를 기억하기 위해 indexed_priorities에
    # [idx, priority] 를 append
    indexed_priorities = [[idx, i] for idx, i in enumerate(priorities)]
    # 올바른 우선 순위로 정렬된 작업을 저장하기 위한 list 생성
    sorted_jobs = []
    
    # indexed_priorities에 요소가 있는 동안
    while indexed_priorities:
        # indexed_priorities[0][1](=priorities[0])이
        # priorities에서 가장 큰 요소가 아니라면
        if indexed_priorities[0][1] != max(priorities):
            # indexed_priorities & priorities에서 dequeue후 해당 항목을 enqueue
            indexed_priorities.append(indexed_priorities.pop(0))
            priorities.append(priorities.pop(0))
        # indexed_priorities[0][1](=priorities[0])이 가장 큰 요소이면
        else:
            # indexed_priorities dequeue 후 해당 항목을 sorted_jobs에 append
            sorted_jobs.append(indexed_priorities.pop(0))
            # 동기화를 위해 priorities에서도 dequeue 진행
            priorities.pop(0)
    
    # for문을 통해 내 작업의 작업 순서 확인
    for idx, j in enumerate(sorted_jobs):
        if j[0] == location:
            answer = idx + 1
            break
    return answer
