import yfinance as yf

ticker = "AAPL"

# Dates , this is for dayly prices. Data1 is for training the model and Data2 is for testing and ploting.

start_date = "2020-01-01"
end_date = "2025-01-01"
st="2024-9-01"
ed="2025-02-17"

Data = yf.download(ticker, start=start_date, end=end_date)
Data2 = yf.download(ticker, start=st, end=ed)

Data.to_csv(f'{ticker}_D1.csv')
Data2.to_csv(f'{ticker}_D2.csv')
