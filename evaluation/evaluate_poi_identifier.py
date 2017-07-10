#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list,sort_keys = '../tools/python2_lesson13_keys.pkl')
labels, features = targetFeatureSplit(data)



### your code goes here

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(
    features, labels, test_size = 0.30, random_state = 42)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
#acc2 = clf2.score(features_test, labels_test)
acc = accuracy_score(labels_test,pred)

print(acc)
print('POI numbers in test set is ',sum(pred))
print('The test set has %d people'%(pred.shape[0]))



import numpy as np
print ("all zero's accuracy is %0.3f"%(sum(pred == np.zeros(pred.shape[0])) * 1.0 /pred.shape[0]))

import numpy as np
zero_iden = np.zeros(pred.shape[0])
acc = accuracy_score(zero_iden,pred)
print ('testing accuracy(zero indentify note) is %0.3f'%acc)



from sklearn.metrics import precision_score
print ('precision score is %0.3f'%precision_score(labels_test,pred))
from sklearn.metrics import recall_score
print ('recall score is %0.3f'%recall_score(labels_test,pred))


