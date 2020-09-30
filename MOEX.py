index_name = 'NLMK'
file_name = 'data/' + index_name + '.csv'

DATE = '\ufeff"Дата"'
PRICE = 'Цена'
OPEN = 'Откр.'
MIN = 'Мин.'
MAX = 'Макс.'
VOLUME = 'Объём'
DIF = 'Изм. %'

import csv
import matplotlib.pyplot as plt
from datetime import datetime

def csv_dict_list(variables_file):
    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
 
    reader = csv.DictReader(open(variables_file, 'r', encoding='utf-8'), delimiter=',')
    
    dict_list = []
    for line in reader:
        dict_list.append(line)


    return dict_list

def plot_price(data):
    date = []
    price = []

    for row in data:
        date.append(row[DATE])
        price.append(row[PRICE])
        
    print(len(date), len(price))

    plt.title(index_name)

    plt.plot(date, price)
    plt.gcf().autofmt_xdate()
    

def main():    
    data = csv_dict_list(file_name)

    for row in data:

        row[PRICE] = float(row[PRICE].replace(',','.'))
        row[OPEN] = float(row[OPEN].replace(',','.'))
        row[MIN] = float(row[MIN].replace(',','.'))
        row[MAX] = float(row[MAX].replace(',','.'))
        row[DATE] = datetime.strptime(row[DATE], "%d.%m.%Y")

    plot_price(data)

    plt.show()



main()