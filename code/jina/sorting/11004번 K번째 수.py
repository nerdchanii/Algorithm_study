import sys

# 입력값 N와 K
N, K = map(int,input().split())

# 숫자 데이터 data에 입력
data = list(map(int, sys.stdin.readline().split()))

# 퀵 정렬을 이용한 풀이도 작성했었으나 시간 초과로 통과하지 못함
# 병합 정렬 이용
def mergesort(data):
    # data에 값이 하나 이하라면 그대로 return
    if len(data) <= 1:
        return data
    
    # data에 값이 2개 이상이면 리스트를 절반으로 나눠서 저장
    i = len(data) //2
    left = data[:i]
    right = data[i:]
    
    # left와 right를 값이 한 개가 될 때까지 재귀적으로 mergesort
    l = mergesort(left)
    r = mergesort(right)
    
    # 오름차순 정렬을 하기 위한 mergelst 생성
    mergelst = []
    i, j = 0, 0
    
    while i < len(l) and j < len(r):
        # l[i]와 r[j] 비교해서 mergelst에 작은 수부터 추가
        if l[i] < r[j]:
            mergelst.append(l[i])
            i += 1
        else:
            mergelst.append(r[j])
            j += 1
    
    # l과 r중 하나 리스트가 먼저 mergelst에 다 채워지면 나머지 리스트를 순서대로 mergelst에 채워넣음
    if i == len(l):
        for j in range(j, len(r)):
            mergelst.append(r[j])
    
    if j == len(r):
        for i in range(i, len(l)):
            mergelst.append(l[i])

    return mergelst

print(mergesort(data)[K-1])
