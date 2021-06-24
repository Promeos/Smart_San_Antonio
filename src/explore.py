import pandas as pd
import math


# Create a function to truncate pollutant values
def truncate(number, n_decimals=0):
    """
    Truncate value to a specific number of decimal places.
    
    
    Parameters
    ----------
    number : float data type
        The average amount of a pollutant in the atmosphere.
    
    n_decimals : int, default 0
        The number of decimal places to keep.
    
    Returns
    -------
    The pollutant truncated to n_decimals.
    
    """
    # Shift the value by the number of decimal place to keep.
    factor = 10.0 ** n_decimals
    
    return math.trunc(number * factor) / factor


def aqi_table():
    '''
    Return a table of AQI values
    '''
    categories = ['Good',
              'Moderate',
              'Unhealthy for Sensitive Groups',
              'Unhealthy',
              'Very unhealthy',
              'Hazardous',
              'Extremely Hazardous']

    AQI_Lower_Limits = [0, 51, 101, 151, 201, 301, 401]
    AQI_Upper_Limits = [50, 100, 150, 200, 300, 400, 500]


    pm25_L = [0.0, 12.1, 35.5, 55.5, 150.5, 250.5, 350.5]
    pm25_U = [12.0, 35.4, 55.4, 150.4, 250.4, 350.4, 500.4]

    ozone_L = [0.000, 0.055, 0.071, 0.086, 0.106, np.nan, np.nan]
    ozone_U = [0.054, 0.070, 0.085, 0.105, 0.200, np.nan, np.nan]

    df_aqi = pd.DataFrame({'PM 2.5 Lower': pm25_L,
                           'PM 2.5 Upper': pm25_U,
                           'Ozone Lower': ozone_L,
                           'Ozone Upper': ozone_U,
                           'AQI_Lower': AQI_Lower_Limits,
                           'AQI_Upper': AQI_Upper_Limits,
                           'category': categories})

    return df_aqi


def aqi(pollutant='ozone', c=.050):
    '''
    Calculates the Air Quality Index for a given pollutant.
    
    Parameters
    ----------
    pollutant : str, default 'ozone'
    
        pollutant options
        -----------------
        'ozone': Calculate the AQI for Ozone AKA O3
        'pm2.5': Calculate the AQI for Particle Matter Smaller than 2.5 Microns
    
    c : numeric, default 10
        The calculated average of the pollutant
    
    Returns
    -------
    The Air Quality Index with Category
    '''
    table = aqi_table()
    
    if pollutant == 'ozone':
        decimals = 3
        upper_bound = 'Ozone Upper'
        lower_bound = 'Ozone Lower'
    elif pollutant == 'pm2.5':
        decimals = 1
        upper_bound = 'PM 2.5 Upper'
        lower_bound = 'PM 2.5 Lower'
    
    C_p = truncate(c, n_decimals = decimals)
    
    I = table.loc[(table[upper_bound] >= C_p)&(table[lower_bound] <= C_p)].reset_index(drop=True)

    BP_high = I[upper_bound]
    BP_low = I[lower_bound]
    I_high = I['AQI_Upper']
    I_low = I['AQI_Lower']
    category = I['category'][0]

    AQI = int(((I_high - I_low)/(BP_high - BP_low))*(C_p- BP_low) + I_low)

    print(f"The AQI is {AQI}. Category: {category}")