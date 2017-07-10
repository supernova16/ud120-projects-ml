#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pprint
import re

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

#print (len(enron_data))
#print(len(enron_data["SKILLING JEFFREY K"]))
#pprint.pprint(enron_data["SKILLING JEFFREY K"])


def count_poi():
    count = 0
    for person_name in enron_data:
        if enron_data[person_name]["poi"] == 1:
            count += 1
    return count

print(count_poi())


txtpath = '../final_project/poi_names.txt'

with open(txtpath) as file:
    poi_n=[name for name in file if "(n)" in name]

with open(txtpath) as file:
    poi_y=[name for name in file if "(y)" in name]

pprint.pprint(len(poi_y)+len(poi_n))



print(enron_data["PRENTICE JAMES"]["total_stock_value"])
print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

lay_total_payments = enron_data['LAY KENNETH L']['total_payments']
skilling_total_payments = enron_data['SKILLING JEFFREY K']['total_payments']
fastow_total_payments = enron_data['FASTOW ANDREW S']['total_payments']

print(lay_total_payments,skilling_total_payments,fastow_total_payments)


# NAN

print (sum(1 for x in enron_data.values() if x['salary'] != 'NaN'))
print (sum(1 for x in enron_data.values() if x['email_address'] != 'NaN'))

print (sum(1 for x in enron_data.values() if x['total_payments'] == 'NaN') * 100 / len(enron_data))

pois = [x for x in enron_data.values() if x['poi'] == True]

print (sum(1 for x in pois if x['total_payments'] == 'NaN') * 100 / len(pois))

print (len(enron_data) + 10)
print (sum(1 for x in enron_data.values() if x['total_payments'] == 'NaN') + 10)



