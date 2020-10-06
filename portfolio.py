import pandas as pd
import numpy as np
import datetime as dt
import itertools
import FinanceDataReader as fdr
from pandas_datareader import data as pdr

class Portfoilo():
    def __init__(self):
        self.stocks = pd.DataFrame(columns=['stock_name','stock_code','VaR', 'Corr'])

    def add_stock_to_pf(self, stock_name, stock_code):
        self.stocks.append({'stock_name': stock_name,\
                            'stock_code': stock_code,\
                            'VaR':-1,\
                            'Corr':-1},\
                            ignore_index=True)

    def del_stock_from_pf(self, stock_code):
        pf =self.stocks
        pf.drop(pf[pf['stock_code']==stock_code].index, inplace=True)
        
    def view_pf(self):
        print("--information details in this portfolio.")
        print(self.stocks)
        


class Analysis(Portfoilo):
    def __init__(self):
        return

    def load_price_data(self, stock_code):
        return

    def cal_corr(self, pf_name):
        return

    def cal_var(self, pf_name):
        return