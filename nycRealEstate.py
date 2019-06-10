import string
import math
import random

def getData(filename):
    linelist=[]
    f=open(filename,'r')
    for item in f:
        linelist.append(item)
    return linelist

def convertStrNumToNum(string):
    try:
        answer = float(string)
    except ValueError:
        answer = string
    return answer

def stringsSeperatedByCommasToList(string):

    listOfStrings = []
    substring = ""
    for letter in string:
        if letter == ",":
            listOfStrings.append(convertStrNumToNum(substring))
            substring = ""
        else:
            substring += letter
    return listOfStrings

def putTogetherDataSet():

    listOfRowsAsStrs = getData("nyc-rolling-sales.csv")
    dataSet = [stringsSeperatedByCommasToList(string) for string in listOfRowsAsStrs]
    for row in dataSet:
        row.pop(0)
    return dataSet[1:]

dataSet = putTogetherDataSet()
print(dataSet[0])
