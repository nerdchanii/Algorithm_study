# 별찍는 함수 만들기
def square(number):

    # 주어지는 number가 3일 때가 가장 기본 형태 
    if number == 3:
        star = ['***','* *','***']
        return star

    # number가 3이 아닌 3의 거듭제곱일 때 재귀함수 이용
    else:
        # 리스트 star의 길이는 number
        star = [''] * number
        
        # square(number//3)의 리스트로부터 number에 대한 star을 만들어줌
        for i, s in enumerate(square(number//3)):

            # 새로운 star는 square(number//3)의 3배 길이이므로 i, i+(number//3), i+(number//3)*2마다 규칙성 생김
            # star[i]와 star[i+(number//3)*2]는 s의 3배를 해준 값
            # star[i+(number//3)]은 s + (number//3)만큼의 공백 + s 의 값
            star[i] = s*3
            star[i+(number//3)] = s + ' ' * (number//3) + s
            star[i+(number//3)*2] = s*3

        return star


number = int(input())

# square(number)는 number길이 만큼의 리스트 형태이므로 요소별로 출력
for s in square(number):
    print(s)
