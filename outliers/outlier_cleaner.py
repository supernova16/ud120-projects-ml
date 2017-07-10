#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    error = list((net_worths - predictions) ** 2)  ## use square，net_worths 和 predictions 均是 np.array 可以直接运算
    data = zip(ages, net_worths, error) # data是一个用zip打包成元组的列表
    sorted_data = sorted(data, key=lambda tup: tup[2])  ## tup[2] is error ，用error大小来排序data
    cleaned_data = sorted_data[:81]  # get the first 81 with least square errors

    return cleaned_data
