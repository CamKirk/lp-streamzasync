import statsmodels.api as sm 
from statsmodels.tsa.arima_model import ARIMA
import pandas as pd

arima_result = sm.load("../analysis/notebooks/models/arima.pickle")
# garch_result= sm.load("../../analysis/notebooks/models/garch.pickle")

def forecast_future(date):
        """accepts date as string and returns int days difference"""
        # calc timedelta in days
        try:
            days = pd.Timedelta(pd.to_datetime(date) - pd.Timestamp.now()).days
            return arima_result.forecast(days)[0][-1]
        except:
            raise "forecast_future was passed an invalid date"

def predict_history(data):

    # need to correct below code
    # need to slice data at 95% and train
    if isinstance(pd.core.series.Series):
        model = ARIMA(data, order=(2,1,2)) # order from our prior calcs

