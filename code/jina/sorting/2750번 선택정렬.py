N = int(input()) # 입력될 숫자의 수
data = [] # 입력되는 숫자들을 담을 리스트

for _ in range(N):
    target = int(input()) # 새롭게 입력해주는 숫자를 target으로 지정
    data.append(target)

# 데이터를 오름차순으로 정렬하기
# python에서 sort()를 이용하면 바로 오름차순으로 정렬되지만 정렬 알고리즘 이용하기

# 선택정렬 알고리즘
# data의 모든 인덱스를 탐색하는데 O(N), 탐색을 N번 반복해야하므로 O(N^2)의 시간복잡도를 가짐

for cnt in range(N-1): 
    # 한 번의 cnt마다 data의 앞에서부터 작은 값이 배치되므로 i의 범위를 cnt부터 N-1까지 돌게 for문 설정
    # num을 이용해서 data[cnt+1:]의 리스트에서 최솟값 설정
    num = data[cnt]
    for i in range(cnt+1, N):
        if data[i] < num:
            num = data[i]
    # num과 data[cnt] 교환
    idx = data.index(num)
    data[cnt], data[idx] = data[idx], data[cnt]


# 출력
for number in data:
    print(number)
