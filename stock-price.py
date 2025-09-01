import yfinance as yf

STK =  input("Enter Stock name : ")

data = yf.Ticker(STK).history(period="1d")

last_market_price = data['Close'].iloc[-1]

print("Last market price",last_market_price)