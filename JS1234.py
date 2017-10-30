import LennyStocksAPI
import time

from datetime import datetime, time
now = datetime.now()

UID = "JS1234"

while True: 
    n_time = datetime.datetime.now()
    ''' print the hour '''
    print (n_time.hour)
    ''' print the min ''' 
    print (n_time.minute)
    
    if n_time.hour >= 9 and n_time.minute >= 30:
        if n_time.hour >=9 and n_time.minute <35:
            LennyStocksAPI.buyStocks(UID, "ZOO", 2)
            time.sleep(600)
     
    if n_time.hour >= 15 and n_time.minute >= 30:
        if n_time.hour >=15 and n_time.minute <35:
            LennyStocksAPI.buyStocks(UID, "ZOO", 2)
            time.sleep(600)
     



#while 1 > 0:
#	now_time = now.time()
#	if now_time >= time(9,30) and now_time <=(9,35):				
#		LennyStocksAPI.buyStocks(UID, "AAPL", 2)
#		time.sleep(600)
#	if now_time >= time(15,30) and now_time <=(15,35):
#		LennyStocksAPI.sellStocks(UID, "AAPL", 2)
#		time.sleep(600)
	
	

	
