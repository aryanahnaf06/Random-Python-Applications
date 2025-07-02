# importing necessary libraries
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from pandas import DataFrame
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# loading the wine dataset
wine = datasets.load_wine()

# X -> features, Y -> label
X = wine.data
Y = wine.target
# print(X)
# print(Y)

# dividing X, Y into train and test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

# training a Gaussian Naive Bayes classifier
model = GaussianNB()
model.fit(X_train, Y_train)

# testing
model_predictions = model.predict(X_test)

# accuracy of prediction
accuracyScore = accuracy_score(Y_test, model_predictions)
print(accuracyScore)

