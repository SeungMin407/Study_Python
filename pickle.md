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
```
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
```
import json

with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print(loaded_data)
```
