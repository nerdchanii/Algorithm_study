'''
baekjoon9012.py
'''
from sys import stdin 
# 첫번째 라인 (총 테스트 케이스 수) 읽기
line= int(input())

for _ in range(line):
    letter= stdin.readline().strip()
    # 예외처리 1: 문장의 길이가 짝수가 아닐 때
    # 예외처리 2: 문장의 시작이 "("가 아닐 때
    if len(letter)%2 == 1 or letter[0] != "(":
        print("NO")
        continue
    # 예외처리 3: "("의 수와 ")"의 개수가 일치하지 않을 때
    if letter.count("(") != letter.count(")"):
        print("NO")
        continue
   
    # 리스트와 인덱스를 위해 변수 선언, 
    # idx가 최종적으로 0일 때에만, YES출력해야함
    stack=list()
    idx= 0
    for i in letter:
        # letter가 "("일때만 리스트에 추가. idx로 인텍스 계산
        if i == "(":
            stack.append(i)
            idx +=1
        else:
            # ")"가 나온 상황에서 idx == 0 이면, NO를 출력해야함. 
            # idx가 0인 상황에서는 리스트가 비었으므로, pop()수행시
            # IndexError발생
            if idx == 0:
                # idx를 1로 만들고 break -> NO출력하도록 만듬
                idx =1
                break
            else:
                # pop은 idx 의 원소를 삭제, idx는 앞으로 들어가야할 공간을 가리키므로
                # 인데스를 축소시키고, pop 해야함
                idx -= 1
                stack.pop(idx)
    # 출력
    if idx == 0:
        print("YES")
    else:
        print("NO")        