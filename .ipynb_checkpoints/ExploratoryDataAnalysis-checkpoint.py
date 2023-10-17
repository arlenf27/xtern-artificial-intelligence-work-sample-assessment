## Author: Arlen Feng
# For more information on this quick exploratory data analysis, see the README.md file
# This program uses matplotlib, an open-source plotting library for Python. To learn more about matplotlib, 
# go to https://matplotlib.org/
from matplotlib import pyplot
import csv

# Adds one piece of data to dictionary
def addData(category, dict):
    if category not in dict:
        dict.update({category:1})
    else: 
        dict.update({category:dict.get(category)+1})

# Opens the csv dataset and reads the data into dictionaries, returns the dictionaries
def loadData():
    yearDict = {}
    majorDict = {}
    universityDict = {}
    timeDict = {}
    orderDict = {}
    numOrders = 0
    with open('XTern 2024 Artificial Intelegence Data Set - Xtern_TrainData.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            numOrders+=1
            addData(row['Year'], yearDict)
            addData(row['Major'], majorDict)
            addData(row['University'], universityDict)
            addData(row['Time'], timeDict)
            addData(row['Order'], orderDict)
    return numOrders, yearDict, majorDict, universityDict, timeDict, orderDict

# Prints one distribution and plots a histogram using matplotlib
def printGeneralDistribution(str, dict, i):
    print(str, end='')
    print(dict)
    pyplot.figure(i)
    pyplot.title(str)
    pyplot.bar(list(dict.keys()), dict.values(), 1.0, color='g')
    pyplot.xticks(rotation=45, horizontalalignment='right', fontweight='light', fontsize='x-small')
    print('\n')

# Print and plot all distributions
def printAllGeneralDistributions():
    numOrders, yearDict, majorDict, universityDict, timeDict, orderDict = loadData()
    print('Exploratory Data Analysis: \n\n')
    print('Number of Orders: ' + str(numOrders) + '\n\n')
    printGeneralDistribution('General Year Distribution: ', yearDict, 1)
    printGeneralDistribution('General Major Distribution: ', majorDict, 2)
    printGeneralDistribution('General University Distribution: ', universityDict, 3)
    printGeneralDistribution('General Time Distribution: ', timeDict, 4)
    printGeneralDistribution('General Order Distribution: ', orderDict, 5)
    print('Below are general bar chart plots for each category of data. ')
    