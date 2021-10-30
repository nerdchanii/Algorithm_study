N = int(input()) # 입력될 숫자의 수
data = [] # 입력되는 숫자들을 담을 리스트

for _ in range(N):
    target = int(input()) # 새롭게 입력해주는 숫자를 target으로 지정
    data.append(target)

# 데이터를 오름차순으로 정렬하기

# 버블정렬 알고리즘
# data의 모든 인덱스를 탐색하는데 O(N), 탐색을 N번 반복해야하므로 O(N^2)의 시간복잡도를 가짐

for cnt in range(N-1): 
    # 한 번의 cnt마다 data의 끝에서부터 높은 값이 배치되므로 i의 범위를 1부터 N-1-cnt까지 돌게 for문 설정
    for i in range(1, N-cnt):
        # 양 옆의 요소를 비교해서 왼쪽 값이 오른쪽 값보다 크면 교환
        if data[i-1] > data[i]:
            data[i-1], data[i] = data[i], data[i-1]

for number in data:
    print(number)
