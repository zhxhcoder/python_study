import datetime as dt

daylinefilespath = '/Users/xhzh/fileDo/dayline'
stock_b_code = '000001'  # 平安银行
MA1 = 10
MA2 = 50
startdate = dt.date(2016, 6, 29)
enddate = dt.date(2017, 1, 30)


def readstkData(rootpath, stockcode, sday, eday):
    returndata = pd.DataFrame()
    for yearnum in range(0, int((eday - sday).days / 365.25) + 1):
        theyear = sday + dt.timedelta(days=yearnum * 365)
        # build file name
        filename = rootpath + theyear.strftime('%Y') + '\\' + str(stockcode).zfill(6) + '.csv'

        try:
            rawdata = pd.read_csv(filename, parse_dates=True, index_col=0, encoding='gbk')
        except IOError:
            raise Exception('IoError when reading dayline data file: ' + filename)

        returndata = pd.concat([rawdata, returndata])

    # Wash data
    returndata = returndata.sort_index()
    returndata.index.name = 'DateTime'
    returndata.drop('amount', axis=1, inplace=True)
    returndata.columns = ['Open', 'High', 'Close', 'Low', 'Volume']

    returndata = returndata[returndata.index < eday.strftime('%Y-%m-%d')]

    return returndata


import pandas as pd;
import matplotlib.pyplot as plt
from matplotlib import dates as mdates
from matplotlib import ticker as mticker
from matplotlib.finance import candlestick_ohlc
import datetime as dt

daylinefilespath = '/Users/xhzh/fileDo/dayline'
stock_b_code = '000001'  # 平安银行
MA1 = 10
MA2 = 50
startdate = dt.date(2016, 6, 29)
enddate = dt.date(2017, 1, 30)


def readstkData(rootpath, stockcode, sday, eday):
    returndata = pd.DataFrame()
    for yearnum in range(0, int((eday - sday).days / 365.25) + 1):
        theyear = sday + dt.timedelta(days=yearnum * 365)
        # build file name
        filename = rootpath + theyear.strftime('%Y') + '\\' + str(stockcode).zfill(6) + '.csv'

        try:
            rawdata = pd.read_csv(filename, parse_dates=True, index_col=0, encoding='gbk')
        except IOError:
            raise Exception('IoError when reading dayline data file: ' + filename)

        returndata = pd.concat([rawdata, returndata])

    # Wash data
    returndata = returndata.sort_index()
    returndata.index.name = 'DateTime'
    returndata.drop('amount', axis=1, inplace=True)
    returndata.columns = ['Open', 'High', 'Close', 'Low', 'Volume']

    returndata = returndata[returndata.index < eday.strftime('%Y-%m-%d')]

    return returndata


# 这里定义了几个全局变量：
#
# daylinefilespath
# 是下载的日k线数据
# stock_b_code
# 是要显示的股票代码，大家可以换成自己想要的股票
# MA1和MA2是移动平均线的日期间隔，例如10是10日移动平均线
# startdate和enddate是想要显示的日期范围
# 函数readstkData读入数据并做了必要的合并和清洗。注意这里年做了简化处理，并不完全准确。
#
# 绘出日K线
# Talk is cheap，我们直接上代码：

def main():
    days = readstkData(daylinefilespath, stock_b_code, startdate, enddate)

    # drop the date index from the dateframe & make a copy
    daysreshape = days.reset_index()
    # convert the datetime64 column in the dataframe to 'float days'
    daysreshape['DateTime'] = mdates.date2num(daysreshape['DateTime'].astype(dt.date))
    # clean day data for candle view
    daysreshape.drop('Volume', axis=1, inplace=True)
    daysreshape = daysreshape.reindex(columns=['DateTime', 'Open', 'High', 'Low', 'Close'])

    Av1 = movingaverage(daysreshape.Close.values, MA1)
    Av2 = movingaverage(daysreshape.Close.values, MA2)
    SP = len(daysreshape.DateTime.values[MA2 - 1:])
    fig = plt.figure(facecolor='#07000d', figsize=(15, 10))

    ax1 = plt.subplot2grid((6, 4), (1, 0), rowspan=4, colspan=4, axisbg='#07000d')
    candlestick_ohlc(ax1, daysreshape.values[-SP:], width=.6, colorup='#ff1717', colordown='#53c156')
    Label1 = str(MA1) + ' SMA'
    Label2 = str(MA2) + ' SMA'

    ax1.plot(daysreshape.DateTime.values[-SP:], Av1[-SP:], '#e1edf9', label=Label1, linewidth=1.5)
    ax1.plot(daysreshape.DateTime.values[-SP:], Av2[-SP:], '#4ee6fd', label=Label2, linewidth=1.5)
    ax1.grid(True, color='w')
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.yaxis.label.set_color("w")
    ax1.spines['bottom'].set_color("#5998ff")
    ax1.spines['top'].set_color("#5998ff")
    ax1.spines['left'].set_color("#5998ff")
    ax1.spines['right'].set_color("#5998ff")
    ax1.tick_params(axis='y', colors='w')
    plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))
    ax1.tick_params(axis='x', colors='w')
    plt.ylabel('Stock price and Volume')
    plt.show()


if __name__ == "__main__":
    main()
