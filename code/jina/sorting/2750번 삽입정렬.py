N = int(input()) # 입력될 숫자의 수
data = [] # 입력되는 숫자들을 담을 리스트

# 데이터를 오름차순으로 정렬하기

# 삽입정렬 알고리즘
# 한 원소에 대해서 전체 data 요소를 비교하고 이를 N번 반복하므로 O(N^2)의 시간복잡도를 가짐

for _ in range(N):
    target = int(input()) # 새롭게 입력해주는 숫자를 target으로 지정

    # data 리스트에 아무 값이 없으면 target 추가
    if data == []:
        data.append(target)

    # data 리스트에 값이 존재하는 경우 target과 data의 숫자들과 비교해서 원하는 자리에 삽입 
    else:
        # data 리스트는 오름차순 정렬이 되어있는 상태
        # data의 끝값보다 target이 큰 경우 data 끝에 target 추가
        if target > data[-1]:
            data.append(target)
        
        # target이 data 리스트 중간에 삽입되어야 하는 경우
        else:
            for num in data:
            # target이 num보다 작은 경우 num의 인덱스가 target이 삽입되어야 하는 위치
            # target을 data에 삽입해주고 break
                if target < num: 
                    idx = data.index(num)
                    data.insert(idx, target)
                    break

# 출력
for number in data:
    print(number)
