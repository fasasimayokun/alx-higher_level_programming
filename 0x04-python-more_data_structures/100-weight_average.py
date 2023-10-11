#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return 0

    num_ab = 0
    num_bl = 0

    for num in my_list:
        num_ab += num[0] * num[1]
        num_bl += num[1]

    return (num_ab / num_bl)
