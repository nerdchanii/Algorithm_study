import sys

n = int(sys.stdin.readline()) # 몇 개의 문장을 쓸 것인지 입력받기
d = [] # 빈 리스트에 입력받은 라인 정리하기 준비

for i in range(n):
    a = sys.stdin.readline()
    d.append(a.rstrip()) # 빈 리스트에 입력값 채우기

for i in d:
    if (i[0] == ')') or (i[-1] == '(') or (i.count('(') != i.count(')')): # 첫 인덱스 값이 ), 끝 인덱스 값이 ( 인 경우 거짓, "("와 ")"가 개수가 다르면 거짓
        print("NO")
        continue # 생략하고 다음 인덱스로
    h = list(i) # 문자열을 리스트로 받아서 계산하기(값 변경을 용이하게 하기 위해서
    for j in range(len(i)): # 리스트 길이만큼 반복해서 시행
        if h[0] == '(': # 만약 시작이 "("일 때
            del h[0]    # "("를 먼저 삭제하고
            del h[h.index(')')] # "("에 조응하는 ")" 를 삭제해나감
            if len(h) == 0: # 모두 삭제했을 때, YES를 출력할 수 있게 됨
                print("YES")
                break
            else:
                continue
        else: # 삭제하다가 ))이렇게 반복되는 경우에는 VPS가 불가능하기 떄문에 NO 출력 ★아 생각해보니 ))이렇게 반복되면 NO로 출력해도 될 듯 하다!!★
            print("NO")
            break
