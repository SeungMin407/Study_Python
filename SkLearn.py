import pandas as pd
from sklearn.datasets import load_iris
iris=load_iris()
df=pd.DataFrame(data=iris.data,columns=iris.feature_names)
df['target'] = iris.target
target_name={0:iris.target_names[0],
        1:iris.target_names[1],
        2:iris.target_names[2]}
df['target']=df['target'].map(target_name)
print(df.head())
from sklearn.model_selection import train_test_split
iris_data=df[["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]]
iris_label=df["target"]
train_data,test_data,train_label,test_label=train_test_split(iris_data,iris_label)
from sklearn import svm, metrics
clf=svm.SVC()
clf.fit(train_data,train_label)
pre=clf.predict(test_data)
s=metrics.accuracy_score(test_label,pre)
print("정답 ",s)