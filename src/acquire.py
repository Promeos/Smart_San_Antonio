import pandas as pd
import os


def get_zone_data(sensor='ambient_noise', zone='all'):
    '''
    Sensor data from a zone(s) in San Antonio.
    
    Parameters
    ----------
    sensor : str optional, default 'ambient_noise'
        The type of raw sensor data to return.
        
        sensor options
        --------------
        'air_quality'   : Air Quality sensor data
        'ambient_noise' : Ambient Noise sensor data
        'flood_level'   : Flood level sensor data
        'weather'       : Weather sensor data
        
    
    zone : str optional, default 'all' 
        Zone where the sensors are located.
        
        zone options
        ------------
        'brooks'   : Brooks City Base
        'downtown' : Downtown San Antonio
        'medical'  : Medical Center
        'all'      : All zones. Brooks, Downtown, and Medical
    
    Returns
    -------
    data : pandas.core.frame.DataFrame
        Raw sensor dataset.
    '''
    
    filepath = f'./data/raw/{sensor}/{zone}.csv'
    
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        return combine_data(sensor_type=sensor)

 
def combine_data(sensor_type='ambient_noise'):
    '''
    For a specific sensor, combine the zones together into a file named 'all'
    Parameters
    ----------
    sensor : str optional, default 'ambient_noise'
        The type of raw sensor data to return.
        
        sensor options
        --------------
        'air_quality'   : Air Quality sensor data
        'ambient_noise' : Ambient Noise sensor data
        'flood_level'   : Flood level sensor data
        'weather'       : Weather sensor data
    '''
    
    a = pd.read_csv(f'./data/raw/{sensor_type}/brooks.csv')
    b = pd.read_csv(f'./data/raw/{sensor_type}/downtown.csv')
    c = pd.read_csv(f'./data/raw/{sensor_type}/medical.csv')
    
    merge_1 = pd.concat([a, b])
    merge_2 = pd.concat([merge_1, c])
    
    merge_2.to_csv(f'./data/raw/{sensor_type}/all.csv', index=False)
    
    return merge_2