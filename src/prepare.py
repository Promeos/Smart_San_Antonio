import pandas as pd
import numpy as np

import os


def prep_sensor_data(data):
    '''
    Prepare the noise sensor data.
    
    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The raw noise sensor data from the raw/ data file.
    
    Returns
    -------
    data : pandas.core.frame.DataFrame
        Prepared noise sensor data.
    '''
    filepath = './data/prepared/ambient_noise/sensors.csv'
    
    try:
        data = pd.read_csv(filepath)
    except FileNotFoundError:
        data.columns = [col.lower() for col in data.columns]

        data.rename(columns={'datetime': 'date',
                            'sensormodel': 'sensor_model',
                            'lat': 'latitude',
                            'long': 'longitude',
                            'noiselevel_db': 'noise_level',
                            'alerttriggered': 'alert_triggered',
                            'sensorstatus': 'sensor_status'},
                    inplace=True)

        data['date'] = pd.to_datetime(data['date'], infer_datetime_format=True)
        data.alert_triggered = np.where(data.alert_triggered == np.NaN, 'Not Supported', 'No')
        data.zone = data.zone.replace(to_replace=" Market\s\d{2}", value='', regex=True)

        # Replace duplicate latitude and longitude data with the most recent coordinates.
        data.loc[data.sensor_id == '64d7e0e4cfeba0b6', ('latitude', 'longitude')] = data.loc[(data.sensor_id == '64d7e0e4cfeba0b6')&(data.date == data.date.max()), ('latitude', 'longitude')].max().values

        data.loc[data.sensor_id == '64d7e4dbde37ccb5', ('latitude', 'longitude')] = data.loc[(data.sensor_id == '64d7e4dbde37ccb5')&(data.date == data.date.max()), ('latitude', 'longitude')].max().values
        
        data.to_csv(filepath, index=False)
    finally:
        return data