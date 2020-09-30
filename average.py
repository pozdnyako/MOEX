from IO import *

def calc_average(data, length) :
    if(length *2 > len(data)):
        print('length(' + str(length) + ') is too long')
        return

    sum = 0
    for i in range(0, length*2):
        sum += data[i][PRICE]

    for i in range(length, len(data)-length):
        data[i]['AVG'+str(length)] = sum / length / 2

        sum -= data[i-length][PRICE]
        sum += data[i+length][PRICE]

def calc_dif_average(data, length) :
    if(length *2 > len(data)):
        print('length(' + str(length) + ') is too long')
        return

    sum = 0
    for i in range(0, length*2):
        sum += data[i][PRICE]

    for i in range(length, len(data)-length):
        avg = sum / length / 2

        data[i]['DIF_AVG'+str(length)] = (data[i][PRICE]-avg)/avg*100

        sum -= data[i-length][PRICE]
        sum += data[i+length][PRICE]

def plot_average(data, length, title):
    date = []
    price = []

    for row in data:
        if('AVG'+str(length) in row):
            date.append(row[DATE])
            price.append(row['AVG'+str(length)])
        
    ax.plot(date, price, label=title)

def plot_dif_average(data, length, title):
    date = []
    price = []

    for row in data:
        if('DIF_AVG'+str(length) in row):
            date.append(row[DATE])
            price.append(row['DIF_AVG'+str(length)])
        
    ax.plot(date, price, label=title)

