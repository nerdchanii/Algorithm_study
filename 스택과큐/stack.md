# 스택
## 스택이란? 
- 데이털르 임시 저장할 떄 사용하는 자료구조, 입출력이 LIFO방식인 자료구조
  LIFO란, Last In First Out 의 약자 !

## 스택과 관련한 용어들
### 푸시와 팝
- 푸시(push): 스택에 데이터를 넣는 작업 
- 팝(pop): 스택에서 데이터를 꺼내는 작업

### 탑과 바텀
- top : 스택의 꼭대기
- bottom : 스택의 아랫부분

### 스택의 길이와 스택 포인터

- capacity : 스택의 길이를 의미, 스택이 담을 수 있는 양
- ptr: 스택에 쌓여 있는 데이터의 개수를 나타냄
- 스택포인터의 범위(?)는 0 =< ptr =< capacity

## 스택 구현하기

### 고정길이스택 구현하기

필요한것들: 예외처리, 초기화, 데이터 개수 확인을 위한 함수, 스택이 비었는지 확인하는 함수, 스택이 꽉찼는지 확인하는 함수,
        push, pop, peek, clear 메소드= 삽입, 삭제, 마지막원소확인
        find, count, __contains__메소드 = 원소찾기, 원소 수세기, 원소가 있는지 확인하기

```python
class FixedStack:

    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256)-> None:
        """스택 생성, 초기화"""
        self.capacity = capacity
        self.stk = [None] * capacity
    
    def is_full(self)->bool:
        """스택이 꽉 찾는지 판단"""
        return self.ptr>= self.capacity

    def is_empty(self)->bool:
        """스택이 비었는지 판단"""
        return self.ptr<=0

    def push(self, value: Any)-> None:
        """스택에 원소 집어넣기"""
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] =value
        self.ptr += 1
        
    def pop(self)-> Any:
        """스택에서 원소 꺼내기"""
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def clear(self)->None:
        """스택의 모든원소 제거하기"""
        self.ptr = 0

    def find(self, value: Any)-> int:
        """스택에 원소를 찾아 인덱스를 반환(없으면 -1) """ 
        # 두개면 어떻게 되는거지? 더 높은 쪽의 인덱스를 반환할것 같다.
        for idx in range(self.ptr -1, -1, -1): # self.ptr -1 : 현재 제일 꼭대기의 인덱스
            if self.stk[idx] == value:
                return idx
        return -1

        # 이렇게도 만들 수 있지 않을까? 
        # try:
        #     return self.stk.index(value)
        # except: 
        #     return -1
    

    def count(self, value: Any)-> int:
        """스택에 있는 value의 개수를 반환"""
        
        c= 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c


    def __contains__(self, value: Any)-> bool:    
        """value가 스택에 있는지 확인"""
        return self.count(value) > 0
        

    def dump(self) -> None:
        """스택의 모든 원소 출력"""
        if self.is_empty():
            print('스택이 비어 있습니다')
        else:
            print(self.str[:self.ptr])
```


### deque사용해서 구현하기

**deque**는파이썬에서 지원하는 내장 모듈 collection에서는 여러 컨테이너를 추가적으로 지원한다.<br> 
주요한 컨테이너는 namedtuple(), deque, chainMap, Counter, OrederedDict, defaultdict, UserDict, UserList, UserString 같은 콜렉션이다.<br> 
deque를 사용하면 리스트를 사용할 때보다 좋은 성능의 스택을 구현할 수 있다. 

<table>
<th>deque의 메소드들 </th>
<tr>
<td>

|속성과 함수|설명|
|:-------|:--|
|maxlen|deque의 최대 크기, 읽기 전용, 크기 제한이 없으면 None|
|append(x)|deque의 맨 끝(오른쪽)에 x 추가|
|appendleft(x)|deque의 맨 앞(왼쪽)에 x 추가|
|clear()| deque의 모든 원소를 삭제하고 크기를 0으로 만듬|
|copy()|deque의 얕은 복사|
|count(x)|deque안에 있는 x의 갯수를 계산|
|extend(iterable)|순차 반복 인수 iterable에서 가져온 원소를 deque의 맨 끝에 추가하여 확장합니다.|
|extendleft(iterable)|순차 반복 인수 iterable에서 가져온 원소를 deque의 맨 왼쪽에 추가하여 확장합니다.|
|이외 |index(x[,start[,stop]])<br> insert(i,x)<br> pop(), popleft()<br> remove(value), reverse(), rotate(n=1)<br> 등등

</td>
</tr>
</table>



