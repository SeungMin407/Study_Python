## Exemplar-CNN(Discriminative unsupervised feature learning with exemplar convolutional neural networks)
---
# 1. 개요

기존 CNN은 라벨(정답) 이 있어야 학습이 가능했다. 하지만 대규모 라벨링된 데이터셋(예: ImageNet)을 만드는 데는 막대한 시간과 비용이 든다. 
Exemplar-CNN은 2014년 Dosovitskiy 등이 제안한 Self-Supervised Learning (자기지도학습) 기법이다.  
라벨이 없는(unlabeled) 이미지에서도 CNN이 스스로 유용한 특징 표현(feature representation) 을 학습하도록 하는 것이 목표이다.

---
# 2. 핵심 개념

<img width="673" height="363" alt="image" src="https://github.com/user-attachments/assets/eb3da461-23da-4a5c-adbc-6d27820237dd" />

기존의 CNN은 라벨이 필요했지만, Exemplar-CNN은 라벨이 없어도 스스로 학습 데이터를 구성한다.

- 이미지마다 **고유한 가짜 클래스(label)** 를 부여한다.  
- 한 이미지에 대해 patch를 추출하고 다양한 transform을 하여 여러 **변형된 버전(augmented samples)** 을 만들어 모두 같은 클래스에 속하도록 학습한다.

즉, 같은 이미지의 변형된 버전은 **같은 class** 로, 서로 다른 이미지는 **다른 class** 로 인식하도록 훈련된다.

---
# 3. 구체적인 방법

1. **Patch 추출**
   - 원본 이미지에서 작은 영역(패치)을 여러 개 뽑는다.

2. **Transformation 적용**
   - 각 패치에 다양한 변형을 가한다.  
     (예: 회전, 이동, 밝기 조절, 색상 변화, 블러 등)
     
3. **가짜 라벨 부여**
- 동일한 원본 패치에서 나온 모든 변형 이미지는 **같은 클래스 i** 로 취급한다.
- 서로 다른 패치는 각각 다른 클래스 번호를 가진다.

4. **CNN 학습**
- CNN은 “이 이미지가 어떤 Exemplar(class i)에 속하는가?”를 예측하도록 학습한다.
- 일반적인 **cross-entropy loss** 를 사용한다.

 동일한 exemplar에서 transform이 적용된 patches들은 하나의 class i를 부여한다. 즉, unlabeled dataset으로부터 8000개의 exemplar를 추출했다면, 8000개의 클래스가 존재하고 신경망의 끝에서 8000차원의 softmax 연산을 수행한다. 이렇게 CNN을 학습함으로써 동일한 class내에 존재하는 상호정보량을 최대화 할 수 있다.

---
# 4. Expriments

<img width="717" height="504" alt="image" src="https://github.com/user-attachments/assets/0268bd24-f6d3-4685-acc7-e020da9c5e30" />

exeplars(대표 샘플)의 수는 8000개가 적당하다는 실험 결과이다.

<img width="630" height="429" alt="image" src="https://github.com/user-attachments/assets/8b1a0de4-c6d8-4b92-9e5c-2d1dd120d25a" />

클래스 당 샘플 수에 따른 실 결과이다.

---
# 5. reference

https://www.inference.vc/exemplar-cnns-and-information-maximization/
