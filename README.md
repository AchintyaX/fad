# Financial Anomaly Detection 

A Toolkit to perform anomaly detection on time-series data of any stock that can be download via yahoo finance API.
You can download the stock data and perform anomaly detection using a range of algorithms

## Installation
For installing the pre-release version use -
` pip install https://github.com/AchintyaX/fad/releases/download/v0.1.0/fad-0.1.0-py3-none-any.whl`

## Usage
1. fetch_data - Used for fetching stock data using yahoo finance API and transforming it for anamoly detection : 
```
In [1]: from fad import FinancialAnomalyDetector

In [2]: fad = FinancialAnomalyDetector()

In [3]: start = '2020-01-10'

In [4]: end = '2022-09-10'

In [5]: data = fad.fetch_data('SBIN.NS', start, end)

In [6]: data
Out[6]:
                  Open        High  ...   Adj Close      Volume
2020-01-10  331.000000  337.950012  ...  324.151825  42377838.0
2020-01-11  331.000000  337.950012  ...  324.151825  42377838.0
2020-01-12  331.000000  337.950012  ...  324.151825  42377838.0
2020-01-13  334.000000  335.450012  ...  322.688354  23615129.0
2020-01-14  329.799988  331.700012  ...  320.005402  26296117.0
...                ...         ...  ...         ...         ...
2022-09-06  538.000000  542.700012  ...  537.799988   8657868.0
2022-09-07  534.400024  537.450012  ...  532.849976   8445359.0
2022-09-08  536.000000  546.299988  ...  544.650024  12240707.0
2022-09-09  549.650024  557.000000  ...  553.349976  18585432.0
2022-09-10  549.650024  557.000000  ...  553.349976  18585432.0

[975 rows x 6 columns]

```

2. anamly_detection - Used to find anomalies in the data returning the dataframe along with plotting them in the time series

The package has 2 primary methods - 
1. 

## For Development 

1. Clone the project
2. `pip install --upgrade pip`
3. `pip install poetry`
4. `poetry install`

project setup is complete for contributions 

