I believe that the stock trading behavior for companies that sell technologies to PV generation companies may adjust relative to information coming from the EIA surveys on energy generation and consumption produced monthly. To that end, I will attempt to generate two trading strategies based on two different models, and may further extend to a third that attempts to combine the two effectively.

For the datasets,  we will use the stock information from several companies by using the alpha-vantage web api, in conjunction with the eip report data for 2013 onwards (most solar information wasn't tracked until 2013).

I _intend_ to utilize the ARIMA and LSTM models for predicting future values and building the trading strategy around the efficacy of those predictions. however, I don't believe the closing values for the OHLC of the datasets will be stationary, and we may need to carry out stationarization transformations before applying the data model.
