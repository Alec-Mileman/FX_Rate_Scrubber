import yfinance as yf
import pandas as pd


print("------------------")
s_dt = input("Input START date in this format 'YYYY-MM-DD' : ")
e_dt = input("Input END date in this format 'YYYY-MM-DD' : ")
print("------------------")

fx_rates = ["GBPAUD=X","GBPCHF=X","GBPCZK=X","GBPCZK=X","GBPDKK=X","GBPEUR=X","GBPNOK=X","GBPPLN=X","GBPSEK=X","GBPUSD=X","GBPZAR=X"]
date = yf.download(tickers = fx_rates, threads = True, group_by="ticker", start = str(s_dt), end = str(e_dt))

df = pd.DataFrame()

n=3

for i in range(len(fx_rates)):
    
    
    if n <= len(date.columns)-3:
        df = pd.concat((df, date.iloc[:,n]), axis = 1)        
        n+=6
    else:
        break



