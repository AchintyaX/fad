import pandas as pd
import yfinance as yf 
import numpy as np 
from anamoly_utils import seasonal_ad_detector, min_cluster_detector, outlier_detector, level_shift_detector, volatile_shift_detector
from adtk.data import validate_series 


class FinancialAnomalyDetector:

    def __init__(self) -> None:
        self.detector_map = {
            'seasonal_ad':seasonal_ad_detector,
            'min_cluster_ad':min_cluster_detector, 
            'outlier_ad': outlier_detector, 
            'level_shift_ad': level_shift_detector,
            'volatile_shift_ad': volatile_shift_detector
        }

    def fetch_data(self, company_name: str, start_date: str, end_date: str) -> pd.DataFrame:
        data = yf.download(company_name, start=start_date, end=end_date)

        idx = pd.date_range(start_date, end_date)
        data = data.reindex(idx)
        data = data.fillna(method="ffill", inplace = True)

        data = validate_series(data)

        return data
    
    def anamoly_detect(self, data: pd.DataFrame, method: str = 'min_cluster_ad', print_plot: bool = True) -> pd.DataFrame:
        detection_method = self.detector_map[method]

        anomalies = detection_method(data=data, print_plot=print_plot)

        return anomalies