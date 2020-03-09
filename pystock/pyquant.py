import datetime as dt

import pandas as pd

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
