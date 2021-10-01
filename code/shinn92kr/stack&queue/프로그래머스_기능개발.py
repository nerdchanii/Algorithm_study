def solution(progresses, speeds):
    # ceil 함수 사용을 위한 math library import
    import math
    answer = []

    # 최고 우선 순위 작업(progresses[0])의 완료 시간을 계산하여 time에 할당
    time = math.ceil((100 - progresses[0]) / speeds[0])
    cnt = 0

    # progresses 안에 요소가 있는 동안
    while len(progresses) > 0:
        # progresses 안에 남아있는 작업 중 첫번째 작업이 완료되면
        if progresses[0] + (time *  speeds[0]) >= 100:
            # 완료된 작업과 작업 속도를 dequeue
            progresses.pop(0)
            speeds.pop(0)
            # 동시 배포 작업의 수를 구하기 위해 cnt += 1
            cnt += 1
        # progresses 안에 남아있는 작업 중 첫번째 작업이 완료되지 않았다면
        else:
            # 배포 필요한 작업이 있을 경우(cnt가 1보다 같거나 클 경우)
            if cnt >= 1:
                # 배포 필요한 작업의 수(cnt)를 answer에 append한 뒤 
                answer.append(cnt)
                # cnt 초기화
                cnt = 0
            
            # 작업 시간 += 1
            time += 1
    # 마지막 배포 작업의 경우 while문 안에서 answer에 append 되지 않았기 때문에
    # while문 밖에서 최종 배포 작업 append 처리
    answer.append(cnt)
    return answer
