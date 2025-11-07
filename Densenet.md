## DenseNet (Densely Connected Convolutional Network)
---
#1. 개요
DenseNet은 2017년 CVPR에서 발표된 CNN 구조로, 이름처럼 모든 층이 서로 ‘조밀하게(Dense)’ 연결된 네트워크이다.
기존의 ResNet은 skip-connection 방식을 통해 활성화 함수로 인한 비선형 변환을 우회한다. 비선형 변환은 모델이 복잡한 형태의 비선형 데이터들을 학습 할 수 있게 하지만, 네트워크가 깊어질수록 기울기 소실 문제가 발생한다.
<img width="526" height="275" alt="image" src="https://github.com/user-attachments/assets/650e66b7-0802-47a1-8434-5a7877d3d87d" />
이러한 skip-connection을 통해 identity(원천 정보)가 직접적으로 뒤로 더해져 전달된다. 이러한 덧셈연산은 정보의 흐름을 방해할 여지가 있다.

---
#2. 해결 아이디어
<img width="583" height="506" alt="image" src="https://github.com/user-attachments/assets/7ca0d15f-4483-4299-a7ee-f224856f1b65" />
DenseNet에서는 레이어간 정보 흐름을 향상시키기 위해 단순 덧셈이 아닌 concatnate를 사용한다. concatnate는 특정 방향(차원)으로 feature을 쌓아 단순 덧셈에 비해 정보의 흐름을 방해할 여지가 적다.

<img width="692" height="290" alt="image" src="https://github.com/user-attachments/assets/609e41d7-2641-4c76-b980-0f3ae8ea14f4" />
ResNet과 중요한 차이점은 DenseNet이 더 narrow한 레이어를 가질 수 있다는 것이다.
DenseNet에서는 각 층이 새로운 채널을 growth rate(k) 만큼만 추가한다.
DenseNet의 한 층이 상대적으로 폭이 좁지만, 모든 이전 층의 출력을 연결(concatenate) 하기 때문에 결과적으로는 정보량이 많은 넓은 입력을 받게 된다.

<img width="752" height="302" alt="image" src="https://github.com/user-attachments/assets/9e48e4e7-131d-4a3c-9d71-a685a5e393a6" />
ResNet은 bottleneck layer를 제안하며 input의 수를 줄이고 효율성을 증가시켰다.
저자들은 DenseNet에 적합한 bottleneck으로 기존의 레이어를 총 2개의 레이어로 변형했다.
1번 레이어 : batch normalization -> ReLU -> (1x1 Conv, 4*k)
2번 레이어 : batch normalization -> ReLU -> (3x3 Conv, k)

ResNet은 덧셈을 하므로 입력과 출력의 shape가 같아야 한다.
반면 DenseNet은 Concat을 하므로 shape 중 가로 세로만 같으면 되고 채널은 달라도 된다. 따라서 그에 따라 변형한 것이라 볼 수 있다.

<img width="802" height="217" alt="image" src="https://github.com/user-attachments/assets/d5ff3314-ebac-4268-86cc-e2d404e18b13" />
해당 논문에서는 feature을 작은 사이즈로 바꾸는 pooling layer를 Dense Block 사이마다 배치하여 transition layer로 사용하였다.
transition layer의 구조는 다음과 같다. (batch normalization) -> (1x1 Conv) -> (2x2 average pooling)

---
#3. 구조
<img width="826" height="396" alt="image" src="https://github.com/user-attachments/assets/8a65aae1-f7e0-482e-b32f-4747b777d4da" />

---
#4 성능
<img width="615" height="300" alt="image" src="https://github.com/user-attachments/assets/863115ef-355b-4a0f-a4a0-6a9d2ada5ce2" />
DenseNet은 각 레이어가 이전의 모든 feature map을 입력으로 concat한다. 즉, 이미 계산된 특징들을 다시 계산하지 않고 그대로 사용하기 때문에 ResNet에 비해 적은 수의 파라미터를 가지고 연산량도 적다. 그러나 그래프에서 알 수 있듯, 에러는 비슷하다. 


