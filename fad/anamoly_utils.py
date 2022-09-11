from adtk.detector import SeasonalAD
from adtk.visualization import plot 
from adtk.detector import MinClusterDetector
from sklearn.cluster import KMeans
from adtk.detector import OutlierDetector
from sklearn.neighbors import LocalOutlierFactor
from adtk.detector import LevelShiftAD
from adtk.detector import VolatilityShiftAD
import pandas as pd 
from typing import Optional
from fad.constants import seasonal_c, side, n_clusters, contamination, level_shift_c, side_levelshift, window_levelshift , volatile_shift_c, side_volatile_shift, window_volatile_shift


def seasonal_ad_detector(data: pd.DataFrame, print_plot: bool = True) -> Optional[pd.DataFrame]:
    seasonal_ad = SeasonalAD(c=seasonal_c, side=side)
    anamolies = seasonal_ad.fit_detect(data)

    if print_plot == True:
        print(plot(data, anomaly=anamolies, anomaly_color="orange", anomaly_tag="marker"))
    
    return anamolies

def min_cluster_detector(data: pd.DataFrame, print_plot: bool =True) -> Optional[pd.DataFrame]:
    min_cluster_ad = MinClusterDetector(KMeans(n_clusters=3))
    anamolies = min_cluster_ad.fit_detect(data)

    if print_plot == True:
        plot(data, anomaly=anamolies, ts_linewidth=1, ts_markersize=3, anomaly_color='red', anomaly_alpha=0.3, curve_group='all')
    
    return anamolies

def outlier_detector(data: pd.DataFrame, print_plot: bool = True) -> Optional[pd.DataFrame]:
    outlier_ad = OutlierDetector(LocalOutlierFactor(contamination=contamination))
    anomalies = outlier_ad.fit_detect(data)
    if print_plot == True: 
        plot(data, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_color='red', anomaly_alpha=0.3, curve_group='all')
    
    return anomalies

def level_shift_detector(data: pd.DataFrame, print_plot: bool = True) -> Optional[pd.DataFrame]:
    level_shift_ad = LevelShiftAD(c= level_shift_c, side=side_levelshift, window=window_levelshift)
    anomalies = level_shift_ad.fit_detect(data)
    if print_plot == True:
        plot(data, anomaly=anomalies, anomaly_color='red');
    
    return anomalies

def volatile_shift_detector(data: pd.DataFrame, print_plot: bool = True) -> Optional[pd.DataFrame]:
    volatile_shift_ad = VolatilityShiftAD(c= volatile_shift_c, side=side_volatile_shift, window=window_volatile_shift)
    anomalies = volatile_shift_ad.fit_detect(data)
    if print_plot == True:
        plot(data, anomaly=anomalies, anomaly_color='red');
    
    return anomalies


