import sys

# 입력값 N
N = int(input())

# data에 수 입력하기
data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))

# 병합 정렬 이용 오름차순 정렬
## 정렬되지 않은 리스트를 절반으로 잘라 나누고 그 리스트들의 요소가 1개가 될 떄까지 재귀적으로 conquer
## 두 개의 리스트들을 하나의 리스트로 하나의 리스트가 될 때까지 merge

def mergesort(data):
    # data에 값이 하나 이하 라면 그대로 return
    if len(data) <= 1:
        return data

    # data에 값이 2개 이상이면 리스트를 절반으로 나눠서 저장
    idx = len(data)//2
    left = data[:idx]
    right = data[idx:]
    
    # left와 right를 값이 한 개가 될 때까지 재귀적으로 mergesort
    l = mergesort(left)
    r = mergesort(right)

    # 오름차순 정렬을 하기 위한 mergelst 생성
    mergelst = [0 for _ in range(len(l) + len(r))]
    i, j, k = 0, 0, 0

    while i < len(l) and j < len(r):
        # l[i]와 r[j] 비교해서 mergelst에 작은 수부터 추가
        if l[i] < r[j] :
            mergelst[k] = l[i]
            i += 1
        else:
            mergelst[k] = r[j]
            j += 1
        k += 1  
        
    # l과 r중 하나 리스트가 먼저 mergelst에 다 채워지면 나머지 리스트를 순서대로 mergelst에 채워넣음
    if i == len(l):
        while j < len(r):
            mergelst[k] = r[j]
            j += 1
            k += 1
        
    elif j == len(r):
        while i < len(l):
            mergelst[k] = l[i]
            i += 1
            k += 1
        
    # mergelst return
    return mergelst



# 구하고자 하는 최종 리스트를 answer로 설정하고 하나씩 출력
answer = mergesort(data)
for num in answer:
    print(num)
