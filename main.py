
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def stock_data():
    import yfinance as yahooFinance
    
    # Here We are getting Facebook financial information
    # We need to pass FB as argument for that
    GetFacebookInformation = yahooFinance.Ticker("MCX.NS")

    # whole python dictionary is printed here
    return ((GetFacebookInformation.info))
