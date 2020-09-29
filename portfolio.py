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
        self.stocks
        return
    def del_stock_from_pf(self, stock_code):
        return


class Analysis(Portfoilo):
    def __init__(self):
        return

    def load_price_data(self, stock_code):
        return

    def cal_corr(self, pf_name):
        return

    def cal_var(self, pf_name):
        return