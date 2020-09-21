import pandas as pd
import numpy as np
import datetime as dt
import itertools
import FinanceDataReader as fdr
from pandas_datareader import data as pdr

class Portfoilo():
    def __init__(self):
        self.stock_codes=[]
        self.df_stock = pd.DataFrame()
    
    def load_price_data(self, start_date, end_date):
        tmp =[]
        for stock_code in self.stock_codes:
            if 'KS' in stock_code:
                tmp = pdr.DataReader(stock_code, 'yahoo', start_date, end_date)
            elif 'KQ' in stock_code:
                tmp = fdr.DataReader(stock_code[:-3], start_date, end_date)
            self.df_stock[stock_code] = tmp['Close']

    def add_stock(self, stock_codes):
        self.stock_codes.append(stock_codes)
        if(np.shape(self.stock_codes)[0] != 1): # flatten
            self.stock_codes = list(itertools.chain(*self.stock_codes))
    
    def corr(self):
        return self.df_stock.corr()


def test():
    pf = Portfoilo()
    pf.add_stock(['003670.KS', '069960.KS'])
    pf.add_stock(['099320.KQ', '030520.KQ'])
    print(pf.stock_codes)
    pf.load_price_data(start_date='2019-03-02', end_date='2020-03-21')
    print(pf.df_stock)
    print(pf.corr())
test()