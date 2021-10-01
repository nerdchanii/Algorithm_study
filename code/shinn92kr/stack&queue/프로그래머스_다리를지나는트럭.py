def solution(bridge_length, weight, truck_weights):
    answer = 0
    # bridge의 길이만큼 on_bridge에 o을 넣어 가상의 bridge 생성
    on_bridge = [0] * bridge_length
    
    # on_bridge에 요소가 존재할 동안
    while on_bridge:
        # 시간(answer)에 += 1을 해준 뒤 아래 작업 수행
        answer += 1
        # 시간 += 1이 되었기 때문에 한 단계 앞으로 나아감을 나타내기 위해
        # on_bridge에서 dequeue
        on_bridge.pop(0)

        # truck_weights에 요소가 남아 있는 동안
        if truck_weights:
            # 현재 on_bridge에 있는 트럭의 모든 무계의 합 + truck_weights[0]의 합이
            # 다리가 견딜 수 있는 무게(weight) 이하일 경우
            if sum(on_bridge) + truck_weights[0] <= weight:
                # on_bridge에 truck_weights[0]을 enqueue
                on_bridge.append(truck_weights[0])
                # on_bridge에 추가한 트럭을 dequeue
                truck_weights.pop(0)
            else:
                # 다리의 길이를 유지하기 위해 on_dridge에 0을 enqueue
                on_bridge.append(0)
    return answer
