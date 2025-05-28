import yfinance as yf
import pandas as pd

consumer_tickers1 = [
    "PG", "KO", "PEP", "UL", "CL", "KMB", "NSRGY", "MDLZ", "JNJ", "WMT",
    "COST", "HD", "LRLCY", "NKE", "ADDYY", "SBUX", "MCD", "AMZN", "TGT", "EL",
    "DG", "DLTR", "BBY", "KR", "TSCDY", "WBA", "CVS", "HD", "LOW", "TJX",
    "RL", "VFC", "HSY", "GIS", "TSN", "CAG", "K", "CPB", "HRL", "BF-B", "TAP",
    "BUD", "DEO", "STZ", "CABGY", "HEINY", "PM", "MO", "BTI", "RBGLY", "CHD",
    "EPC", "NWL", "MAT", "HAS", "SONY",  "SSNLF", "AAPL", "FKRAF",
    "WHR", "ELUXY", "YETI", "SWK", "PTON", "UA", "PUMSY", "DECK", "COLM", "BURL",
    "ROST","JWN", "FL", "LULU", "URBN", "WSM", "W", "CHWY", "AZO",
    "ORLY", "AAP", "KMX", "LAD", "TSCO", "CWH", "DKS", "RH", "ETSY", "EBAY",
     "CHWY", "RVLV",  "WRBY", "BIRD",  "HNST"]

consumer_tickers= ["PG", "KO", "PEP", "UL", "CL", "KMB", "NSRGY", "MDLZ"]

Stat1=[]
GC=[]
ddt=[]
MX=[]
imx=[]
MN=[]
imn=[]
olma=[]
pososto=[]
st="2023-07-05"
en="2025-04-06"

for tick in consumer_tickers1:
    ts = yf.download(tick, start=st, end=en)
    ts1=ts.dropna()
    ts1d = ts1.index.tolist()
    ts1d = pd.DataFrame(ts1d)
    ts1=ts1.iloc[:, 0]
    tt50=ts1.rolling(window=50).mean()
    tt200=ts1.rolling(window=200).mean()
    tt10 = ts1.rolling(window=50).mean()

    mhkos = tt50.shape[0]-200
    ts1 = ts1.tail(mhkos)
    tt50 = tt50.tail(mhkos)
    tt200 = tt200.tail(mhkos)

    for i in range(1,mhkos-31):

        if (tt200.iloc[i] - tt50.iloc[i]) * (tt200.iloc[i + 1] - tt50.iloc[i + 1]) <= 0 and tt50.iloc[i]<tt200.iloc[i]:
            ddt=ts1d.iloc[i]
            GC=ts1.iloc[i]
            MX=0
            MN=5*ts1.iloc[i]
            imx=-1
            imn=-1
            olma=0
            for j in range(1,30):
                if ts1.iloc[i+j]>=MX:
                    MX=ts1.iloc[i+j]
                    imx=j
                if  ts1.iloc[i+j]<=MN:
                    MN=ts1.iloc[i+j]
                    imn=j
                olma += ts1.iloc[i+j]-GC
            pososto=(MX-GC)/GC
            Stat1.append([tick,ddt,GC,pososto,MX,imx,MN,imn,olma])

gcross=pd.DataFrame(Stat1)
gcross.to_csv('gc_stat.csv')