import IO
from IO import *
import matplotlib.ticker as mtick

import average as AVG
    
def main():
    data_MOEX = IO.get_data('MOEX')
    #IO.plot_price(data_MOEX, 'MOEX')


    length = 30
    AVG.calc_dif_average(data_MOEX, length)
    AVG.plot_dif_average(data_MOEX, length, 'MOEX - dif with 2 month avg')

    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0f%%'))
    leg = ax.legend();
    plt.show()



main()