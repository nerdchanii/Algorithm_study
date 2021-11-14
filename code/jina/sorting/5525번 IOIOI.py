# 입력값 N
N = int(input())

# S의 길이 M
M = int(input())

# 문자열 S
S = input()

# Pn은  'I' + 'OI' * N, 'IOI'가 N개 반복되는 패턴으로 이루어짐
Pn = 'IO' * N + 'I'

# S에 Pn이 몇 개 존재하는지 확인
# cnt로 조건을 만족하는 경우의 수(ans) 구하기
ans = 0
cnt = 0
i = 0
while i < M-2:
    # S[i:i+3]이 'IOI'인 경우 cnt += 1
    if S[i] == 'I' and S[i+1] == 'O' and S[i+2] == 'I':
        cnt += 1
        # cnt가 N을 만족하면 ans+=1, cnt-=1
        if cnt == N:
            ans += 1
            cnt -= 1
        # IOI가 있을 때는 다음 I를 확인해주면 되므로 i += 2
        i += 2

    # S[i:i+3]이 'IOI'가 아닌 경우 cnt = 0
    else:
        cnt = 0
        # S[i+1]을 확인하기 위해 i += 1
        i += 1

# ans 출력
print(ans)
