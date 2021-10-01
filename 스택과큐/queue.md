# 1. 큐(queue)

- 데이터를 임시 저장하는 자료구조

## 1.1. 특징

- FIFO(First In First Out), LILO(Last In Last Out)의 자료구조로 스택과 비교되어서 사용됨
- 큐에 데이터를 추가하는 작업: enqueue(인큐)
- 큐에서 데이터를 꺼내는 작업: dequeue(디큐)
- 데이터를 꺼내는 쪽: 프론트
- 데이터를 넣는 쪽: 리어

## 1.2. 배열을 통한 구현
> Enqueue Dequeue 시간 복잡도

- **Enqueue(인큐)**: 배열의 맨마지막에 데이터를 저장하면 되므로, 시간복잡도는 **O(1)**이다.
- **Dequeue(디큐)**: 배열의 맨 앞에 데이터를 삭제하고 다른 데이터 전부를 한칸씩 이동시켜야하므로 시간복잡도는 **O(n)**이다. 

**∴ Enqueue는 빠르지만 dequeue는 느린 방법** 


## 1.3. 링 버퍼로 큐 구현하기
> 링 버퍼란? : 배열의 맨 끝의 원소 뒤에 맨 앞의 원소가 연결되는 자료구조
- 원형 큐의 모습
- 인큐와 디큐를 수행하면, front와 rear의 위치를 변경시켜서 구현
- 원소를 옮기지 않고, front와 rear의 값을 업데이트 하는 것만으로도 인큐와 디큐를 수행할 수 있다. 
- 인큐와 디큐시 시간복잡도: **O(1)**

### 1.3.1. 고정길이 원형 큐 만들기

- 예외처리 클래스 : `Empty` , `Full`
- 초기화 함수 `__init()__` : 현재 큐의 데이터의 갯수를 0개로, front, rear의 커서를 0으로, 크기를 파라미터 capacity값으로, que의 본체로를 capacity 크기로 생성
- 데이터의 개수를 반환하는 `__len()__`: `self.no`에 **직접 접근하지 않고, 함수를 사용해서 접근**
- 큐가 가득찼는지, 혹은 완전 비었는지 확인하는 함수: `is_full`, `is_empty`
- 데이터를 넣는 `enque()`
  - 큐에 데이터를 인큐, 큐가 꽉찾을 경우, FixedQueue.Full 반환
  - 데이터의 수 증가 FixedQueue.no += 1 
  - rear를 가리키는 Fixed.rear += 1 
  - 만약에 rear == capacity이면, rear =0
  
- 데이터를 꺼내는 `deque()`
  - 큐에서 데이터를 디큐, 큐가 비었을 경우,FixedQueue.Empty 반환
  - 데이터 수 줄이기 FixedQueue.no -= 1
  - front를 가리키는 Fixed.front += 1
  - 만약에 front == capacity이면, front =0 

- 데이터를 들여다보는 `peek()`
  - 큐에서 데이터를 수정하지 않으므로, front, rear, no 는 바뀌지 않음
  - 다음으로 큐에서 나올 front의 값을 확인함
  - 만약 큐가 비어있다면, FixedQueue.Empty 반환
- 큐에서 탐색하기 `find()`
  - 큐에 value와 같은 데이터가 포함되어 있는 위치를 알아냅니다.
  - 이때 탐색은 인덱스 0 에서 시작하는 것이 아니라, FixedQueue의 front 에서부터 시작합니다. 
  - 그러므로 인덱스는 front~ rear 까지탐색해야하므로, `(i+front)% capacity` 
  - 성공시 해당 인덱스를 반환, 실패시 -1 반환
- 데이터의 개수를 세는 `count()`
    - count()는 큐에있는 value의 값의 개수를 반환
- 데이터가 포함되어 있는 지 판단하는 `__contains__()`
  - 큐에 value가 있는지 boolean형으로 반환
- 큐의 전체 원소를 삭제하는 `clear()`
  - 큐에 있는 모든 데이터를 삭제</br>
  *실제로 큐에 모든데이터를 삭제하지 않고, front와 rear, no를 변경함으로서 삭제
- 큐의 전체 데이터를 출력하는 `dump()`
    - 큐에 있는 모든 데이터를 맨 앞부터 맨 끝 쪽으로 순서대로 출력


> queue.py

```python 
 from typing import Any

class FixedQueue:
    class Empty(Exception):
        """비어있는 FixedQueue에서 디큐 또는 피크할 떄 내보내는 예외 처리"""
        pass
    
    class Full(Exception):
        """가득 찬 FixedQueue에서 인큐할 떄 내보내는 예외처리"""
        pass
    
    def __init__(self, capacity: int)-> None:
        """큐 초기화"""
        self.no= 0                       # 현재 데이터의 개수
        self.front= 0                    # 맨 앞 원소 커서              
        self.rear = 0                    # 맨 뒤 원소 커서
        self.capacity = capacity         # 큐의 크기
        self.que = [None]* capacity      # 큐의 본체 

    def __len__(self) -> int:
        """큐에 있는 모든 데이터의 개수를 반환 """
        return self.no

    def is_empty(self)-> bool:
        """큐가 비어있는지 판단"""
        return self.no <= 0
    
    def is_full(self)-> bool:
        """큐가 가득찼는지 판단"""
        return self.no >= self.capacity
    
    def enque(self, x: Any)-> None:
        """데이터를 인큐"""
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] =x
        self.rear +=1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0
    
    def deque(self)-> Any:
        """데이터를 디큐"""
        if self.is_empty():
            raise FixedQueue.Empty
        x= self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self)-> Any:
        """데이터를 피크"""
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que(self.front)
    
    def find(self, value: Any)->int:
        """큐에서 value를 찾아서 인데스를 반환 없으면(-1)"""
        for i in range(self.no):
            idx= (i + self.front)%capacity
            if self.que[idx] === value:
                return idx
        return -1
    
    def count(self, value:Any)-> Any
        """큐에 있는 value의 개수를 반환"""
        cnt = 0
        for i in range(self.no):
            idx= (i+self.front)%capacity
            if self.que[idx] ==value:
                cnt += 1
        return cnt
    
    def __contains__(self, value: Any)->bool:
        """큐에 value가 있는지 판단"""
        return self.count(value)
    
    def clear(self) -> None:
        """큐의 모든 데이터를 비움"""
        self.front = self.rear = self.no = 0
    
    def dump(self)->None:
        """모든 데이터를 맨 앞부터 맨 끝 순으로 출력"""
        if self.is_empty():
            print("큐가 비었습니다")
        else:
            for i in range(self.no):
                print(self.que[(i+self.front) % capacity], end ='')
            print()
    
```

## 1.4. 보충수업

### 1.4.1. 우선순위 큐
- 우선순위 큐: 인큐시 데이터의 우선순위를 부여하여 추가하고, 디큐할 때, 우선순위가 가장 높은 데이터를 꺼내는 방식
- Python 에서는 `heapq`모듈에서 제공함. 

### 1.4.2. 양방형 대기열 덱(deque)의 구조
*주의! 위의 deque()는 큐의 dequeue를 축약해서 쓴것이고 덱(deeque)은 double-ended queue의 약자*
- 맨 끝 양쪽에서 데이터를 모두 삽입-삭제할 수 있는 자료구조
- 2개의 포인터를 사용하여 양쪽에서 삭제-삽입할 수 있으며, 큐와 스택을 합친 형태라고 생각하면 됩니다. 

### 1.4.3. 링버퍼 활용( 오래된 데이터 삭제하기)
 이렇게 하면, 오랜된 데이터에 새로운 데이터를 덮어씌움으로서, 오래된 데이터를 삭제시킬 수 있다. 
```python
capacity= 5
queue= [None]* capacity

cnt =0
while True:
    a[cnt % n] = int(input(f`{cnt+1}번째 정수를 입력하세요`))
    cnt +=1
    if cnt == capacity:
        retry = input(f`이미 {capacity}개의 데이터가 있습니다. 계속할까요?`)

        if retry in ['n', 'N']:
            break

i = cnt -n
if i<0: i=0

while i< cnt:
    print(f`{i+1}번째 = {a[i%n]}`)
    i+=1
```