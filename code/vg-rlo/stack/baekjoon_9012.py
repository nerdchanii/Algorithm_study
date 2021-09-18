# Stack 구현
# 백준 괄호 - https://www.acmicpc.net/problem/9012
# memory: 29200
# time: 72ms
import sys

# 올바른 괄호 여부에 대한 판단하는 함수
def solution(pare : str):
    stack = []
    Iswrong = False

    # 각 하나의 문자열로 split 
    pare_lst = [p for p in pare]
    for p in pare_lst:
        # pop이 문제가 발생하는 경우가 있음
        try:
            if p == '(':
                stack.append(p) # 여는 괄호는 push(append in python)
            elif p == ')':
                stack.pop(-1) # 닫는 괄호는 pop(First In Last Out)
        # IndexError: pop from empty list
        except IndexError as error:
            Iswrong = True
            break

    # 여는 괄호 개수만큼 닫는 괄호가 push가 안됐을 때 return NO
    if len(stack) != 0 or Iswrong:
        answer = "NO"
    else:
        answer = "YES"
    return answer

# 입력 데이터 개수 지정 
nums = int(input())

# 입력 데이터 개수만큼 숫자 입력 받기
parenthesis = []
for n in range(nums):
    parenthesis.append(str(sys.stdin.readline()))

for pare in parenthesis:
    print(solution(pare)) 