# 세이커 정렬을 이용한 sort

def shaker_sort(a: list) -> list:
    """세이커 정렬"""
    # left right로 정렬해야하는 범위를 설정
    left = 0
    right = len(a) - 1
    # last는 정렬의 범위를 좁히기 위해 사용
    last = right

    while left < right:
        # 일반 버블과 동일
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                # last에 j를 저장(j는 마지막으로 교환이 일어난 자리)
                last = j
        # left에 last를 저장(정렬이 완료된 자리를 저장하는것, 이를통해서 비교범위를 줄임.)
        left = last
        # left에서 right로 비교해감(버블정렬의 역방향)
        for j in range(left, right):
            ''
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j+1],a[j]
                # 위와 동일
                last = j
        # 위와 동일
        right = j
    return a


if __name__ == '__main__':
    # 입력의 라인 수 입력받기
    lines = int(input())
    # 리스트컴프리헨션을 통한 인풋 받기
    numbers = [int(input()) for _ in range(lines)]
    # shaker_sort진행
    numbers = shaker_sort(numbers)
    # 출력
    for i in numbers:
        print(i)
