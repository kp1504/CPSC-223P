#By Kshitij Pingle
#series.py
#This file is a part of numbers subpackage
#This file and the mathematics package are a part of Lab 4 for CPSC 223P


def sum(*, list):
    listsum = 0
    for x in list:
        listsum += x
    return listsum
#End of sum function


def average(*, list):
    listsum = sum(list = list)
    average = listsum / len(list)
    return average
#End of average function

#End of series.py
