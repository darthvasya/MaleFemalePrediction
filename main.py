from sklearn import tree

genders = ['male', 'female']
X = [[188, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
     [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40]]

Y = [genders[0], genders[1], genders[1], genders[1],
     genders[0], genders[0], genders[0], genders[1]]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

prediction = clf.predict([[190, 70, 43]])

print(prediction)