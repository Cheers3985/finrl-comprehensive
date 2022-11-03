import yfinance as yf
import pytz
# from tzlocal import get_localzone
# local = pytz.timezone('utc')
# print(local)
from datetime import datetime as datetime
tic = ['AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'GS', 'HD', 'HON', 'IBM', 'INTC']
start_date  = datetime (2008,1,1)
end_date   = datetime (2008,10,30)
# start_date = '2008-01-01'
# end_date = '2008-10-31'
time_interval='1D'
temp_df = yf.download(tic, start=start_date, end=end_date, interval=time_interval,proxy='127.0.0.1:10809')  
print(temp_df)