from IO import *

def _DIF():
    return 'DailyDIF'

def _DIF_AVG(length):
    return 'DailyDIF_AVG'+str(length)


def calc_dif(data) :
    print('calc dif, tag is [' + _DIF() + ']')

    for i in range(1, len(data)):
        data[i][_DIF()] = data[i][PRICE] / data[i-1][PRICE]


def calc_average(data, length) :
    print('calc dif_average, tag is [' + _DIF_AVG(length) + ']')

    if(length *2 > len(data)):
        print('length(' + str(length) + ') is too long')
        return

    sum = 0
    for i in range(1, length*2+1):
        sum += data[i][_DIF()]

    for i in range(length+1, len(data)-length):
        data[i][_DIF_AVG(length)] = sum / length / 2

        sum -= data[i-length][_DIF()]
        sum += data[i+length][_DIF()]

def plot_average(data, length, title):
    date = []
    price = []

    for row in data:
        if(_DIF_AVG(length) in row):
            date.append(row[DATE])
            price.append(row[_DIF_AVG(length)])
        
    ax.plot(date, price, label=title)

def hist_dif(data, expected, variance, title):
    date = []
    price = []

    for row in data:
        if(_DIF() in row):
            date.append(row[DATE])
            price.append(row[_DIF()])
        
    ax.hist(price, label=title, bins=200, density=True)

    x_axis = np.arange(.9,1.1, 0.001)
    ax.plot(x_axis, norm.pdf(x_axis,expected, variance ** 0.5))

def plot_dif(data, title):
    date = []
    price = []

    for row in data:
        if(_DIF() in row):
            date.append(row[DATE])
            price.append(row[_DIF()])
        
    ax.plot(date, price, '.' , label=title)
