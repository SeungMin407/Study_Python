## Gradient Descent
Gradient Descent(경사하강법)는 머신러닝과 딥러닝에서 **모델의 손실함수를 최소화**하기 위해 가장 널리 사용되는 최적화 알고리즘입니다.  

### 1. 기본 아이디어
경사하강법의 핵심은 **손실함수(Loss function)의 기울기(gradient)를 이용하여 파라미터를 반복적으로 업데이트**하는 것입니다.  
즉, 현재 위치에서 손실이 가장 빠르게 감소하는 방향으로 조금씩 이동하는 방식이다.

대표적인 손실함수인 **MSE**를 미분하는 과정은 다음과 같다.
<img width="827" height="197" alt="image" src="https://github.com/user-attachments/assets/ee9e087b-9f38-4111-9c03-c93f1a55d9af" />
<img width="477" height="141" alt="image" src="https://github.com/user-attachments/assets/a29e25d2-8be4-495c-9cfd-bacd52251e21" />

- $\theta$ : 모델 파라미터  
- $\eta$ : 학습률(learning rate)  
- $J(\theta)$ : 손실함수  
- $\nabla_\theta J(\theta)$ : 파라미터 $\theta$에 대한 손실함수의 기울기

### 2. 학습률(learning rate)
- 학습률 $\eta$는 한 번 업데이트 시 파라미터가 이동하는 크기를 결정한다.
- 너무 크면 최소값을 지나치며 발산할 수 있고, 너무 작으면 수렴 속도가 느리다.

### 3. 경사하강법의 종류
1. **Batch Gradient Descent (배치 경사하강법)**  
   - 전체 데이터셋을 사용해 기울기를 계산하고 한 번 업데이트합니다.  
   - 장점: 안정적, 정확한 기울기  
   - 단점: 데이터가 많으면 느림

2. **Stochastic Gradient Descent (확률적 경사하강법, SGD)**  
   - 한 번에 하나의 샘플만 사용해 기울기를 계산하고 업데이트합니다.  
   - 장점: 빠르고 온라인 학습 가능, 지역 최솟값 탈출 용이  
   - 단점: 손실함수의 진동이 심할 수 있음

3. **Mini-batch Gradient Descent (미니배치 경사하강법)**  
   - 데이터 일부(mini-batch)로 기울기를 계산하고 업데이트합니다.  
   - 장점: 배치와 SGD의 장점을 절충  
   - 딥러닝에서 가장 많이 사용되는 방식

### 4. 경사하강법 시 주의점
- **지역 최소값(Local Minimum)**  
  경사하강법은 일반적으로 현재 위치의 기울기에 따라 움직이므로 전역 최소값(Global Minimum)에 도달하지 못할 수 있습니다.  
- **학습률 조정**  
  학습률을 점진적으로 줄이는 **learning rate decay**나 적응형 학습률(Adam, RMSprop 등)을 활용하면 수렴을 안정화할 수 있습니다.

### 5. 간단한 파이썬 예제
```python
import numpy as np

# 손실함수: J(theta) = theta^2
def J(theta):
    return theta**2

# 손실함수의 기울기
def gradient(theta):
    return 2*theta

theta = 10.0      # 초기값
eta = 0.1         # 학습률
epochs = 50       # 반복 횟수

for _ in range(epochs):
    theta -= eta * gradient(theta)
    print(theta)

