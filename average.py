from IO import *

def _AVG(length):
    return 'AVG'+str(length)

def _DIF_AVG(length):
    return 'DIF_AVG'+str(length)

def calc_average(data, length) :
    print('calc dif_average, tag is [' + _AVG(length) + ']')

    if(length *2 > len(data)):
        print('length(' + str(length) + ') is too long')
        return

    sum = 0
    for i in range(0, length*2):
        sum += data[i][PRICE]

    for i in range(length, len(data)-length):
        data[i][_AVG(length)] = sum / length / 2

        sum -= data[i-length][PRICE]
        sum += data[i+length][PRICE]

def calc_dif_average(data, length) :
    print('calc dif_average, tag is [' + _DIF_AVG(length) + ']')

    if(length *2 > len(data)):
        print('length(' + str(length) + ') is too long')
        return

    sum = 0
    for i in range(0, length*2):
        sum += data[i][PRICE]

    for i in range(length, len(data)-length):
        avg = sum / length / 2

        data[i][_DIF_AVG(length)] = (data[i][PRICE]-avg)/avg*100

        sum -= data[i-length][PRICE]
        sum += data[i+length][PRICE]

def plot_average(data, length, title):
    date = []
    price = []

    for row in data:
        if('AVG'+str(length) in row):
            date.append(row[DATE])
            price.append(row[_AVG(length)])
        
    ax.plot(date, price, label=title)

def plot_hist_average(data, length, expected, variance, title):
    date = []
    price = []

    for row in data:
        if(_DIF_AVG(length) in row):
            date.append(row[DATE])
            price.append(row[_DIF_AVG(length)])
        
    ax.hist(price, label=title, bins=200, density=True)

    x_axis = np.arange(-20, 20, 0.001)
    ax.plot(x_axis, norm.pdf(x_axis,expected, variance ** 0.5))



def calc_expected(data, tag):
    result = 0.0
    num = 0
    for row in data:
        if(tag in row):
            result += row[tag]
            num += 1
    
    return result / num

def calc_variance(data, expected, tag):
    result = 0.0
    num = 0

    for row in data:
        if(tag in row):
            result += (row[tag] - expected) * (row[tag] - expected)

            num += 1
            
    return result / num