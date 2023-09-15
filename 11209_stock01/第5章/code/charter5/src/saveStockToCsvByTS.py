import tushare as ts
def saveStockByTS(code):    # 定義取得並儲存指定股票交易資料的方法
    start='2019-01-01'
    end='2019-01-31'
    ts.get_hist_data(code=code,start=start,end=end).to_csv('d:\\stockData\\ch5\\'+code+'.csv',columns=['open','high','close','low','volume'])
# 開始呼叫
code='600895'       # 股票“張江高科”
saveStockByTS(code)
# 也可以去掉下面的注解，在取得股票程式碼的同時取得該股票的訊息
# stockList=ts.get_stock_basics()
# for code in stockList.index:
    # saveStockByTS(code)