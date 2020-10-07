from constants import *

import csv
from datetime import datetime
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

fig, ax = plt.subplots(figsize=(15, 7))


def get_data(index_name):
    filename = 'data/' + index_name + '.csv'
    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
 
    reader = csv.DictReader(open(filename, 'r', encoding='utf-8'), delimiter=',')
    
    dict_list = []
    for line in reader:
        dict_list.append(line)

    for row in dict_list:
        row[PRICE] = float(row[PRICE].replace(',','.'))
        row[OPEN] = float(row[OPEN].replace(',','.'))
        row[MIN] = float(row[MIN].replace(',','.'))
        row[MAX] = float(row[MAX].replace(',','.'))
        row[DATE] = datetime.strptime(row[DATE], "%d.%m.%Y")
        
    return dict_list

def plot_price(data, title):
    date = []
    price = []

    for row in data:
        date.append(row[DATE])
        price.append(row[PRICE])
        
    ax.plot(date, price, label=title)

