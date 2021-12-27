# 하노이의 탑 이동순서
# baekjoon 11729
## 문제: https://www.acmicpc.net/problem/11729


##하노이의 탑을 이동 시키는 함수

# def move(no: int, x: int , y: int )->None:
def move(no: int, x: int, y: int):
    if no > 1:
        move(no-1, x, 6-x-y) 
    print_list.append([x,y]) 
    if no > 1: move(no-1, 6-x-y, y)

    
# 하노이의 탑 출력 함수 
def printout():
    print(len(print_list))
    for x, y in print_list:
        print(f"{x} {y}")


if __name__ == '__main__':
    n= int(input())
    print_list =list()
    move(n, 1, 3)
    printout()
    
# 메모리 120648kb	
# 시간 1472ms
