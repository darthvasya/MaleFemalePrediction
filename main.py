from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import preprocessing

#genders
genders = ['male', 'female']

#[height, weight, shoe_size]
X = [[188, 80, 44],
     [188, 87, 45],
     [183, 79, 42],
     [177, 70, 43],
     [160, 60, 38],
     [154, 54, 37],
     [166, 65, 40],
     [190, 90, 47],
     [175, 64, 39],
     [177, 70, 40]]

Y = [genders[0],
     genders[0],
     genders[0],
     genders[1],
     genders[1],
     genders[1],
     genders[1],
     genders[0],
     genders[1],
     genders[1]]


scaler = preprocessing.StandardScaler().fit(X)
X_scalled = preprocessing.scale(X)

print(scaler.mean_)
## CHALLENGE - create 3 more classifiers...
#1
clf = tree.DecisionTreeClassifier()
#2
gnb = GaussianNB()
#3
svmClf = svm.SVC()

## CHALLENGE - train all of it
#1
clf = clf.fit(X_scalled, Y)
#2
gnb = gnb.fit(X_scalled, Y)
#3
svmClf.fit(X_scalled, Y)
#data for test
inputs = [[190, 84, 43], [201, 97, 46], [167, 51, 39]]

prediction = clf.predict(inputs)
print(prediction)

prediction = gnb.predict(inputs)
print(prediction)

prediction = svmClf.predict(inputs)
print(prediction)