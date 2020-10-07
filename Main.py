import IO
from IO import *
import matplotlib.ticker as mtick

import average as AVG
import difference as DIF
    
def main():
    data_MOEX = IO.get_data('MOEX')
    #IO.plot_price(data_MOEX, 'MOEX')


    length = 15
    AVG.calc_average(data_MOEX, length)
    AVG.calc_dif_average(data_MOEX, length)

    DIF.calc_dif(data_MOEX)
    DIF.calc_average(data_MOEX, length)
    
    DIF_AVG_expected = AVG.calc_expected(data_MOEX, AVG._DIF_AVG(length))
    DIF_AVG_variance = AVG.calc_variance(data_MOEX, DIF_AVG_expected, AVG._DIF_AVG(length))
    print('DIF_AVG E = ' + str(DIF_AVG_expected))
    print('DIF_AVG sigma = ' + str(DIF_AVG_variance ** 0.5))

    DIF_expected = AVG.calc_expected(data_MOEX, DIF._DIF())
    DIF_variance = AVG.calc_variance(data_MOEX, DIF_expected, DIF._DIF())
    print('DIF E = ' + str(DIF_expected))
    print('DIF sigma = ' + str(DIF_variance ** 0.5))

    #AVG.plot_average(data_MOEX, length, 'MOEX - dif with 2 month avg')
    #AVG.plot_hist_average(data_MOEX, length, DIF_AVG_expected, DIF_AVG_variance, 'MOEX - dif with 2 month avg')
    
    #DIF.plot_dif(data_MOEX, 'MOEX daily dif')
    #DIF.plot_average(data_MOEX, length, 'MOEX daily dif average')
    
    DIF.hist_dif(data_MOEX, DIF_expected, DIF_variance, 'MOEX daily dif average')


    #ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0f%%'))
    
    leg = ax.legend();
    plt.show()



main()