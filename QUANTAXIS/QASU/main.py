#
# The MIT License (MIT)
#
# Copyright (c) 2016-2018 yutiansut/QUANTAXIS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from QUANTAXIS.QASU import save_tdx as stdx
from QUANTAXIS.QASU import save_tdx_file as tdx_file
from QUANTAXIS.QASU import save_tushare as sts
from QUANTAXIS.QAUtil import DATABASE

from QUANTAXIS.QASU import crawl_eastmoney as crawl_eastmoney_file
from QUANTAXIS.QAFetch.QAQuery import QA_fetch_stock_list



def QA_SU_save_stock_info(engine, client=DATABASE):
    """save stock info
    
    Arguments:
        engine {[type]} -- [description]
    
    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_info(client=client)


def QA_SU_save_stock_info_tushare(engine="tushare", client=DATABASE):
    '''

    :param engine: tushare
    :param client:
    :return: None
    '''

    # only support the tushare
    engine = select_save_engine("tushare")
    engine.QA_SU_save_stock_info_tushare()

    pass


def QA_SU_save_stock_list(engine, client=DATABASE):
    """save stock_list
    
    Arguments:
        engine {[type]} -- [description]
    
    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_list(client=client)


def QA_SU_save_stock_day(engine, client=DATABASE):
    """save stock_day
    
    Arguments:
        engine {[type]} -- [description]
    
    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_day(client=client)


def QA_SU_save_stock_min(engine, client=DATABASE):
    """save stock_min
    
    Arguments:
        engine {[type]} -- [description]
    
    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_min(client=client)


def QA_SU_save_index_day(engine, client=DATABASE):
    """save index_day
    
    Arguments:
        engine {[type]} -- [description]
    
    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_index_day(client=client)


def QA_SU_save_index_min(engine, client=DATABASE):
    """save index_min
    
    Arguments:
        engine {[type]} -- [description]
    
    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_index_min(client=client)


def QA_SU_save_etf_day(engine, client=DATABASE):
    """save etf_day
    
    Arguments:
        engine {[type]} -- [description]
    
    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_etf_day(client=client)


def QA_SU_save_etf_min(engine, client=DATABASE):
    """save etf_min
    
    Arguments:
        engine {[type]} -- [description]
    
    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_etf_min(client=client)


def QA_SU_save_stock_xdxr(engine, client=DATABASE):
    """save stock_xdxr
    
    Arguments:
        engine {[type]} -- [description]
    
    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_xdxr(client=client)

def QA_SU_save_stock_block(engine, client=DATABASE):
    """save stock_block
    
    Arguments:
        engine {[type]} -- [description]
    
    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_block(client=client)



def select_save_engine(engine):
    '''
    select save_engine , tushare ts Tushare 使用 Tushare 免费数据接口， tdx 使用通达信数据接口
    :param engine: 字符串Str
    :return: sts means save_tushare_py  or stdx means save_tdx_py
    '''
    if engine in ['tushare', 'ts', 'Tushare']:
        return sts
    elif engine in ['tdx']:
        return stdx
    else:
        print('💢 Error QASU.main.py call select_save_engine with parameter %s is None of  thshare, ts, Thshare, or tdx',engine)

def QA_SU_save_stock_min_5(file_dir, client=DATABASE):
    """save stock_min5
    
    Arguments:
        file_dir {[type]} -- [description]
    
    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    
    Returns:
        [type] -- [description]
    """

    return tdx_file.QA_save_tdx_to_mongo(file_dir, client)


def QA_SU_crawl_eastmoney(action="zjlx",stockCode=None):
    '''

    :param action: zjlx 后期支持其他的操作类型
    :param stockCode: 股票代码
    :return:
    '''
    stockItems = QA_fetch_stock_list()

    if stockCode=="all":
        #读取tushare股票列表代码
        print(" 一共需要获取 %d 个股票的 资金流向 , 需要大概 %d 小时" % (len(stockItems), (len(stockItems)*30)/60/60 ))
        for stock in stockItems:
            #print(stock['code'])
            crawl_eastmoney_file.QA_read_eastmoney_zjlx_web_page_to_sqllite(stockCode=stock['code'])
            #print(stock)

        return
    else:
        #todo 检查股票代码是否合法
        return crawl_eastmoney_file.QA_read_eastmoney_zjlx_web_page_to_sqllite(stockCode=stockCode)
