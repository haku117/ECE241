"""
UMass ECE 241 - Advanced Programming
Homework #2     Fall 2018
question3.py - Manipulating stock data

"""
import datetime as dt
import pandas_datareader.data as web
import sys

TICKER = 'AMZN'  # You can experiment with other stocks (AAPL, F, FB, GOOG, TSLA)
DATE = dt.datetime(2018, 9, 15)  # DO NOT CHANGE THIS PARAMETER


class QuestionThree(object):

    def highest_price(self, alist):
        """
        This function receives an array of OHLC data from the past year
        and returns the highest price (highest H) on that period and the index on the array
        where that price happened.
        :param alist: list with OHLC data
        :return: highest price and the index
        """
        current_max = 0
        for i in alist[1::4]:
            if float(i) > float(current_max):
                current_max = i
        return float(current_max), alist.index(current_max)

    def lowest_closing_price(self, alist):
        """
        Similar to the previous method, this function receives an array with OHLC data
        from the past year and return the lowest closing price (lowest C) and the index
        where it happened.
        :param alist: list with OHLC data
        :return: lowest closing price and the index
        """
        current_min = sys.maxsize
        for i in alist[3::4]:
            if float(i) < float(current_min):
                current_min = i
        return float(current_min), alist.index(current_min)

    def average_opening(self, alist):
        """
        This function calculates the average opening price (O) in the past six months (you can
        use half of the array for this purpose).
        :param alist: list with OHLC data
        :return: average opening price from the past six months
        """
        sublist = alist[int(len(alist) / 2)::4]
        res = list(map(float, sublist))
        return sum(res) / len(res)


# DO NOT CHANGE THIS FUNCTION
def df_to_list(data_frame):
    close = data_frame["close_price"].tolist()
    high = data_frame["high_price"].tolist()
    low = data_frame["low_price"].tolist()
    open = data_frame["open_price"].tolist()
    big_list = []
    for o, h, l, c in zip(open, high, low, close):
        big_list.extend((o, h, l, c))

    q3 = QuestionThree()
    print("{}".format(q3.highest_price(big_list)))
    print("{}".format(q3.lowest_closing_price(big_list)))
    print("{}".format(q3.average_opening(big_list)))

    return big_list


# DO NOT CHANGE THIS FUNCTION
def get_stock_prices(ticker):
    start = DATE - dt.timedelta(days=1 * 365)
    end = DATE
    df = web.DataReader(ticker, 'robinhood', start, end)
    df.reset_index(inplace=True)
    df.set_index("begins_at", inplace=True)
    df = df.drop({"symbol", "interpolated", "session", "volume"}, axis=1)
    # df_to_list(df)

    return df


# DO NOT CHANGE THIS FUNCTION
def main():
    data_frame=get_stock_prices(TICKER)
    df_to_list(data_frame)


if __name__ == '__main__':
    main()
