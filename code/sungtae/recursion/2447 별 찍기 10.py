# 재귀적으로 들어가야 함
# 먼저 별을 찍는 과정 나타내기
# 상대적인 좌표가 필요
a = int(input())
arr = [[' ' for _ in range(a)] for _ in range(a)] # 배열을 사전 설정하여, 그 자리에 별 문자로 replace하는 방법

def star(n: int, x: int, y: int) -> str:
    """n: 변의 길이, x: 중간 좌표(x와 y는 동일)"""
    if n == 3: # 최소한의 수준일 때
        arr[y - 1][x - 1] = "*"        # 좌상단
        arr[y - 1][x] = "*"            # 상단
        arr[y - 1][x + 1] = "*"        # 우상단
        arr[y][x - 1] = "*"            # 좌단
        arr[y][x + 1] = "*"            # 우단
        arr[y + 1][x - 1] = "*"        # 좌하단
        arr[y + 1][x] = "*"            # 하단
        arr[y + 1][x + 1] = "*"        # 우하단
    else:
        # 첫 번째 줄
        star(int(n / 3), x - int(n / 3), y - int(n / 3))       # 좌상단
        star(int(n / 3), x, y - int(n / 3))                    # 상단
        star(int(n / 3), x + int(n / 3), y - int(n / 3))       # 우상단
        # 두 번째 줄
        star(int(n / 3), x - int(n / 3), y)                    # 좌단
        star(int(n / 3), x + int(n / 3), y)                    # 우단
        # 세 번째 줄
        star(int(n / 3), x - int(n / 3), y + int(n / 3))       # 좌하단
        star(int(n / 3), x, y + int(n / 3))                    # 하단
        star(int(n / 3), x + int(n / 3), y + int(n / 3))       # 우하단

star(a, int(a / 2), int(a / 2))

for i in range(a):
    for j in range(a):
        print(arr[i][j], end=' ')
    print()
