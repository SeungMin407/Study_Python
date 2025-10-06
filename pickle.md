### 파일 입출력
---------------
# 개요
 파이썬 수업에서 배운 기본 파일 입출력 방식(open, read, write)은 주로 문자열 데이터를 읽고 쓰는 데 사용된다.  
하지만 이 방식은 리스트, 딕셔너리 같은 복합 자료형을 직접 저장하거나 불러오는 데 제약이 있다.  
즉, 자료형을 문자열로 변환하여 저장해야 하고, 다시 읽을 때는 원래 자료형으로 복원하는 과정이 필요하다.  
이 과정에서 데이터 손상이나 오류가 발생할 위험이 있으며, 대규모 데이터나 객체를 다룰 때는 효율성이 떨어진다.  
복합 자료형과 객체를 안전하고 효율적으로 저장하기 위해, 파이썬에서는 직렬화(serialization) 기법을 사용한다. 대표적으로 pickle과 json이 있다.

 ------------
 # 1. json
 1️⃣ 파일에 저장하기(json.dump)
```ruby
import json

data = {
    "name": "abc",
    "age": 25,
    "hobbies": ["a", "b", "c"]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
```
2️⃣ 파일에서 불러오기 (json.load)
```ruby
import json

with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print(loaded_data)
```
3️⃣ 특징

텍스트 기반: 사람이 읽고 편집 가능

언어 간 호환성: 다른 언어에서도 JSON 데이터 사용 가능

기본 자료형 지원: 숫자, 문자열, 리스트, 딕셔너리, True/False/None

직렬화/역직렬화 용이: json.dump로 저장, json.load로 복원

4️⃣ 장점

안전하고 범용적 → 외부 파일 불러오기에도 안전

사람이 읽을 수 있는 형태 → 디버깅 용이

다른 언어와 데이터 공유 가능

5️⃣ 단점

파이썬 고유 객체(클래스, 튜플, set 등)는 직접 저장 불가

바이너리 저장보다 파일 크기 조금 큼

속도는 pickle보다 느림 (문자열 변환 과정 있음)

----------
# 2. pickle

1️⃣ 파일에 저장하기 (pickle.dump)
```ruby
import pickle

# 저장할 객체 (클래스, 리스트, 딕셔너리 등)
data = {
    "name": "abc",
    "age": 25,
    "hobbies": ["a", "b", "c"]
}

# pickle 파일로 저장 (바이너리 모드)
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

print("객체 저장 완료 ✅")
```
2️⃣ 파일에서 불러오기 (pickle.load)
```ruby
import pickle

with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)
```

3️⃣ 특징

바이너리 기반: 파이썬 객체를 그대로 저장하고 복원 가능

파이썬 전용: 다른 언어와 호환되지 않음

거의 모든 객체 저장 가능: 리스트, 딕셔너리, 클래스, 함수 등

4️⃣ 장점

객체 구조 그대로 저장 가능 → 복원 시 데이터 손실 없음

클래스 객체, 튜플, set 등 파이썬 고유 자료형까지 저장 가능

저장/복원 속도가 빠름

5️⃣ 단점

다른 언어에서 사용 불가 → 파이썬 전용

보안 문제: 신뢰할 수 없는 파일을 pickle.load()하면 악성 코드 실행 위험

사람이 읽을 수 없는 바이너리 파일 → 디버깅 어려움
