from sklearn import tree
from sklearn.naive_bayes import GaussianNB

#genders
genders = ['male', 'female']

#[height, weight, shoe_size]
X = [[188, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
     [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40]]

Y = [genders[0], genders[1], genders[1], genders[1],
     genders[1], genders[0], genders[1], genders[1]]

## CHALLENGE - create 3 more classifiers...
#1
clf = tree.DecisionTreeClassifier()
#2
gnb = GaussianNB()

## CHALLENGE - train all of it
#1
clf = clf.fit(X, Y)
#2
gnb = gnb.fit(X, Y)

inputs = [[190, 70, 43], [201, 97, 46], [167, 51, 39]]

prediction = clf.predict(inputs)
print(prediction)

prediction = gnb.predict(inputs)
print(prediction)