#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list,sort_keys = '../tools/python2_lesson13_keys.pkl')
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!


from sklearn.tree import DecisionTreeClassifier
clf1 = DecisionTreeClassifier()
clf1.fit(features, labels)
acc1  = clf1.score(features,labels)

print('acc1',acc1)

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(
    features, labels, test_size = 0.30, random_state = 42)

from sklearn.metrics import accuracy_score
clf2 = DecisionTreeClassifier()
clf2.fit(features_train, labels_train)
pred = clf2.predict(features_test)
#acc2 = clf2.score(features_test, labels_test)
acc2 = accuracy_score(labels_test,pred)

print('acc2',acc2)