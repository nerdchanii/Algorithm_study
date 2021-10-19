import sys    # sys 모듈의 입력 방식이 더 시간 절약에 용이

def move(no: int, x: int, y: int) -> None:
    if no > 1:
        move(no - 1, x, 6 - x - y)
    print(str(x) + ' ' + str(y))
    if no > 1:
        move(no - 1, 6 - x - y, y)
n = int(sys.stdin.readline())

print(2**n - 1)    # 탑의 층 수에 따라 2의 제곱수 씩 이동하기 때문에, 마지막에 모두 3기둥으로 갔을 때 끝나므로 -1
move(n, 1, 3)
