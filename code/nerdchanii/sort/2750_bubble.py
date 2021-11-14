# 버블 정렬을 이용한 sort

def bubble(a: list)-> list:
  # 리스트의 길이 length
  length= len(a)
  #  정렬이 완료된 수 k 
  k = 0

  while k< length - 1:
    # last를 마지막 인덱스로 설정
    last = length - 1
    # a의 마지막 원소부터 k 번째 원소까지 정렬 수행, 스텝은 -1
    for i in range(length - 1, k, -1):
      # ex) a[2]>a[1] => a[2],a[1] = a[1],a[2]
      if a[i-1]>a[i]:
        a[i], a[i - 1] = a[i - 1],a[i]
        # 마지막으로 정렬이 된 원소를 k값으로 정하기 위한 코드
        # 즉, 정렬이 된 원소의 갯수와 동일한 값이 됨. 
        last = i
    k = last
  return a

if __name__ == '__main__':
  # 읽어야하는 라인 수를 받음
  lines = int(input())
  # 받은 수를 저장하기 위한 배열 생성
  numbers = list()
  # 처음 입력 받은 라인 수 만큼 수를 입력받고, numbers에 저장함
  for i in range(lines):
    get = int(input())
    numbers.append(get)
  # 버블정렬 수행
  numbers = bubble(numbers)
  # 출력
  for i in numbers:
    print(i)
    
