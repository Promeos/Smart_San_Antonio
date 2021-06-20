import pandas as pd
import numpy as np


def prep_data(data, folder='ambient_noise', filename='all'):
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
    filepath = f'./data/prepared/{folder}/{filename}.csv'
    
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

   
# def prep_noise_data(data):
#     '''
    
#     '''
#     data.columns = [col.lower() for col in data.columns]
#     data = rename_common_cols(data)
#     data.rename(columns={'noiselevel_db': 'noise_level'},
#                 inplace=True)
#     return data
  
   
    
# def prep_water_data():
#     '''
    
#     '''
    
    
# def rename_common_cols(data):
#     '''
#     Rename columns shared across all sensor types.
#     '''
#     data.columns = [col.lower() for col in data.columns]
#     data.rename(columns={'datetime': 'date',
#                          'sensormodel': 'sensor_model',
#                          'lat': 'latitude',
#                          'long': 'longitude',
#                          'alerttriggered': 'alert_triggered',
#                          'sensorstatus': 'sensor_status'},
#                 inplace=True)
#     return data

    
#     data['date'] = pd.to_datetime(data['date'], infer_datetime_format=True)
#     data.alert_triggered = np.where(data.alert_triggered == np.NaN, 'Not Supported', 'No')
#     data.zone = data.zone.replace(to_replace=" Market\s\d{2}", value='', regex=True)
    
