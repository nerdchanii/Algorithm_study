def solution(bridge_length, weight, truck_weights):
    time = 0 

    # 트럭이 다리를 건너는 상황을 bridge로 표현하기 위해 bridge_length만큼 배열을 만들어줌
    bridge = [0] * bridge_length

    # bridge에 트럭이 존재하는 동안 while루프를 돌게 함
    while bridge:

        # 1초일 때 첫 번째 트럭이 bridge에 올라옴
        time += 1

        # 1초마다 트럭은 이동하므로 맨 앞의 트럭은 1초가 지나면 다리를 지난 트럭이므로 제거
        bridge.pop(0)

        # truck_weigths에 들어있는 트럭들을 bridge로 올리기
        if len(truck_weights) != 0:

            # bridge위에 올라와있는 트럭의 총 무게와 새로 bridge에 올라올 트럭의 무게의 합을 다리가 견딜 수 있는 무게 weight와 비교
            # weight값보다 작거나 같으면 bridge에 새로운 트럭 추가           
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))

            # weight값보다 크면 bridge에 올라올 수 없으므로 0 추가
            else:
                bridge.append(0)
 
    return time
