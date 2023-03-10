import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as npl
from sklearn import linear_model, preprocessing

data = pd.read_csv("car.data")

print(data.head())

#transform data into lists containing integer values instead of words. i.e. yes -> 1 low - med - high -> 0 - 1 - 2 etc.
le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls_ = le.fit_transform(list(data["class"]))


#transforms labels into lists to more easily traverse
X = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls_)


#select training and test sizes
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

model = KNeighborsClassifier(n_neighbors = 9)

model.fit(x_train,y_train)

acc = model.score(x_test, y_test)

print(acc)