import pandas as pd
import numpy as np


def prep_data(data, filename='air'):
    '''
    Prepare the sensor data. If a prepared version of the sensor does not exist,
    one is created for the user.
    
    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        Raw sensor data.
        
    filename : str, default 'air'
        The type of prepared sensor data
        
        filename options
        ----------------
        'air' : Returns air quality data for all zones. 
        'noise' : Returns ambient noise data for all zones.
        'water' : Returns water level data for all zones.
        'weather' : Returns weather data for all zones.

    Returns
    -------
    data : pandas.core.frame.DataFrame
        Prepared ensor data.
    '''
    filepath = f'./data/prepared/{filename}.csv'
    
    try:
        data = pd.read_csv(filepath, infer_datetime_format=True, parse_dates=True)
        data['date'] = pd.to_datetime(data['date'])
    except:
        data = normalize_common_cols(data)
        
        if filename == 'air':
            data = prep_air_data(data)
        elif filename == 'noise':
            data = prep_noise_data(data)
        elif filename == 'water':
            data = prep_water_data(data)
        elif filename == 'weather':
            data = prep_weather_data(data)
        else:
            return None
        
        data.to_csv(filepath, index=False)
    finally:
        return data


#################################################################################################################################


def prep_air_data(data):
    '''
    Prepare the air quality sensor data for exploration.
    '''
    data.rename(columns={'pm1_0': 'micron_1',
                         'pm2_5': 'micron_2',
                         'pm10': 'micron_10',
                         'so2': 'sulfur',
                         'o3': 'ozone',
                         'co' : 'carbon',
                         'no2': 'nitrogen'},
                inplace=True)
    
    data = update_sensor_coordinates(data)
    return data


def prep_noise_data(data):
    '''
    Prepare the ambient noise data for exploration.
    '''
    data.rename(columns={'noiselevel_db': 'noise_level'},
                inplace=True)
    data.zone = data.zone.replace(to_replace=" Market\s\d{2}", value='', regex=True)
    data = update_sensor_coordinates(data)
    return data
  
    
def prep_water_data(data):
    '''
    Prepare the water level sensor data for exploration.
    '''
    data.drop(columns=['disttowl_m', 'disttodf_m', 'temp_c'],
              inplace=True)
    
    data.rename(columns={'disttowl_ft': 'dist_to_water_ft',
                         'disttodf_ft': 'dist_to_floor_ft'},
                inplace=True)
    
    data['water_level'] = data['dist_to_floor_ft'] - data['dist_to_water_ft']
    return data


def prep_weather_data(data):
    '''
    Prepare the weather data for exploration.
    '''
    data.drop(columns=['temp_c', 'dewpoint_c'],
              inplace=True)
    
    data = update_sensor_coordinates(data)
    
    return data
    

#################################################################################################################################


def update_sensor_coordinates(data):
    '''
    Update all previous coordinates with the most recent position of the sensor.
    
    ONLY APPLICABLE TO THE NOISE SENSOR DATASET
    
    Refactor to update future lat and long artifacts.
    '''
    data.loc[data.sensor_id == '64d7e0e4cfeba0b6', ('latitude', 'longitude')] = \
        data.loc[(data.sensor_id == '64d7e0e4cfeba0b6')&(data.date == data.date.max()), ('latitude', 'longitude')].max().values
    data.loc[data.sensor_id == '64d7e4dbde37ccb5', ('latitude', 'longitude')] = \
        data.loc[(data.sensor_id == '64d7e4dbde37ccb5')&(data.date == data.date.max()), ('latitude', 'longitude')].max().values
    
    return data


def normalize_common_cols(data):
    '''
    Rename columns shared across all sensor types.
    '''
    data.columns = [col.lower() for col in data.columns]
    data.rename(columns={'datetime': 'date',
                         'sensormodel': 'sensor_model',
                         'lat': 'latitude',
                         'long': 'longitude',
                         'alerttriggered': 'alert_triggered',
                         'sensorstatus': 'sensor_status'},
                inplace=True)
    
    data['date'] = pd.to_datetime(data['date'], infer_datetime_format=True)
    data.alert_triggered = np.where(data.alert_triggered == np.NaN, 'Not Supported', data.alert_triggered)
    
    return data