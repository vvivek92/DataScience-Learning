#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
from sklearn.svm import SVC
clf = SVC(kernel="rbf",verbose=True,C=10000)
clf.fit(features_train,labels_train)
pred_test = clf.predict(features_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(labels_test, pred_test))
print(pred_test)


#########################################################


