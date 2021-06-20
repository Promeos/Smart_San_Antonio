import pandas as pd
import numpy as np

import os


def get_zone_data(sensor='ambient_noise', zone='all'):
    '''
    Noise sensor data from a zone(s) in San Antonio.
    
    Parameters
    ----------
    zone : str optional, default 'all' 
        Zone where the sensors are located.
        
        Brooks City Base = 'brooks'
        Downtown San Antonio = 'downtown'
        Medical Center = 'medical'
        All zones = 'all'
    
    Returns
    -------
    data : pandas.core.frame.DataFrame
        Noise sensors dataset.
    '''
    
    filepath = f'./data/raw/{sensor}/{zone}.csv'
    
    try:
        if os.path.isfile(filepath):
            return pd.read_csv(filepath)
    except:
        raise FileNotFoundError(f"You're missing the {zone}.csv file.")