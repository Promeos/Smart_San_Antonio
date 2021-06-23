![header](./visuals/header.png)

![exec-summary](./visuals/executive_summary.png)

## Background

### San Antonio Smart Street Light Pilot Program

The SmartSA Smart Streetlight program pilots remote lighting controls, and five environmental sensor use-cases on up to 40 streetlights in each of the three Innovation Zones: Downtown, Brooks and the Medical Center for a total of up to 120 streetlights.

The goal of the program is to evaluate smart streetlights for their cost effectiveness, feasibility, and benefit to the public. If the streetlight pilot is successful, CPS-Energy and the City of San Antonio will determine the possibility of scaling the solutions city-wide. Smart streetlights incorporate energy saving LED lights, remote controls, and can optionally support sensor applications. SmartSA and City of San Antonio stakeholders identified five priority smart streetlight technologies to test during the pilot:
- Air quality sensing
- Temperature sensing
- Ambient noise detection
- Parking availability sensing
- Flood levels sensing

## Business Goals
- Determine which vendor (AT&T or ITRON) provides the most accurate and reliable data.
- Recommendations
  - Store vendor data separately: A folder for AT&T and ITRON for each Zone
  - Air Quality data provided by each sensor do not share the same unit of measurement. Each sensor measures a pollutant differently.
  - Use a new vendor for API or create one in house.
  - In each data dictionary, make it clear that -999 means that a sensor does not have a module to take measurement.
 
 - Create an Air Quality index using the sensor data and EPA standard formula for accurate reporting.
 - Define what AQI represents and how the AQI affects stakeholders (Hospitals, Citizens, First Responders).
 - Create a Noise Sensor Indicator to notify local law enforcement/first responders. Integrate with street cameras?
 - Integrate weather data with CPS energy usage to determine if weather has a significant impact on peak hour power useage.
 - Add street cameras or LED motion sensors to turn off or dim when activity is not detected. (Safety concern)
 - Explain why this data matters and how its insights can be use to improve quality of life for San Antonio in 4-5 sentences or $5 Dollar story.

https://www.sanantonio.gov/SmartSA/Projects

## Data Dictionary
**air.csv**
| Feature Name    | Description                                                                                              | Data Type    |
| :-------------- | :------------------------------------------------------------------------------------------------------- | :----------- |
| date            | Date and Time when the value was read by the sensor in local time. ISO6801 Format: YYYY:MM:DD hh:mm:ss   | DateTime     |
| sensor_id       | Sensor unique identifier.                                                                                | Alphanumeric |
| vendor          | Vendor that owns the sensor. Vendors are ITRON and ATT.                                                  | Text         |
| sensor_model    | The manufacturer model number of the sensor.                                                             | Alphanumeric |
| latitude        | Latitude of sensor.                                                                                      | Numeric      |
| longitude       | Longitude of sensor.                                                                                     | Numeric      |
| zone            | The zone where sensor is installed: Brooks, Downtown, Medical Center.                                    | Text         |
| micron_1        | Microgram per meter cube of inhalable particles with a diameter smaller than 1 Micron.                   | Numeric      |
| micron_2        | Microgram per meter cube of inhalable particles with a diameter smaller than 2.5 Microns.                | Numeric      |
| micron_10       | Microgram per meter cube of inhalable particles with a diameter smaller than 10 Microns.                 | Numeric      |
| sulfur          | Sulfur Dioxide concentration in PPM (parts per million)                                                  | Numeric      |
| ozone           | Ozone concentration in PPM (parts per million)                                                           | Numeric      |
| carbon          | Carbon Monoxide concentration in PPM (parts per million)                                                 | Numeric      |
| nitrogen        | Nitrogen Dioxide concentration in PPM (parts per million).                                               | Numeric      |
| alert_triggered | Yes, No, or Not Supported if sensor supports alert levels and alert was triggered.                       | Text         |
| sensor_status   | Status of the sensor: Normal, Malfunction                                                                | Text         |


**noise.csv**
| Feature Name    | Description                                                                                              | Data Type    |
| :-------------- | :------------------------------------------------------------------------------------------------------- | :----------- |
| date            | Date and Time when the value was read by the sensor in local time. ISO6801 Format: YYYY:MM:DD hh:mm:ss   | DateTime     |
| sensor_id       | Sensor unique identifier.                                                                                | Alphanumeric |
| vendor          | Vendor that owns the sensor. Vendors are ITRON and ATT.                                                  | Text         |
| sensor_model    | The manufacturer model number of the sensor.                                                             | Alphanumeric |
| latitude        | Latitude of sensor.                                                                                      | Numeric      |
| longitude       | Longitude of sensor.                                                                                     | Numeric      |
| zone            | The zone where sensor is installed: Brooks, Downtown, Medical Center.                                    | Text         |
| noise_level     | Noise level in decibels.                                                                                 | Numeric      |
| alert_triggered | Yes, No, or Not Supported if sensor supports alert levels and alert was triggered.                       | Text         |
| sensor_status   | Status of the sensor: Normal, Malfunction                                                                | Text         |

<br>

| Decibels (dB) | Type of Sound                                    |
| :------- | :---------------------------------------------------- |
| 130      | Artillery fire at close proximity                     |
| 120      | Amplified rock music; near jet engine                 |
| 110      | Loud orchestral music, in audience                    |
| 100      | Electric saw                                          |
| 90       | Bus or truck interior                                 |
| 80       | Automobile interior                                   |
| 70       | Average street noise; loud telephone bell             |
| 60       | Normal conversation; business office                  |
| 50       | Restaurant; private office                            |
| 40       | Quiet room in home                                    |
| 30       | Quiet lecture hall; bedroom                           |
| 20       | Radio, television, or recording studio                |
| 10       | Soundproof room                                       |
| 0        | Absolute silence (threshold of hearing)               |

[source](https://www.britannica.com/science/sound-physics/The-decibel-scale)

**water.csv**
| Feature Name     | Description                                                                                              | Data Type    |
| :--------------- | :------------------------------------------------------------------------------------------------------- | :----------- |
| date             | Date and Time when the value was read by the sensor in local time. ISO6801 Format: YYYY:MM:DD hh:mm:ss   | DateTime     |
| sensor_id        | Sensor unique identifier.                                                                                | Alphanumeric |
| vendor           | Vendor that owns the sensor. Vendors are ITRON and ATT.                                                  | Text         |
| sensor_model     | The manufacturer model number of the sensor.                                                             | Alphanumeric |
| latitude         | Latitude of sensor.                                                                                      | Numeric      |
| longitude        | Longitude of sensor.                                                                                     | Numeric      |
| zone             | The zone where sensor is installed: Brooks, Downtown, Medical Center.                                    | Text         |
| temp_f           | Temperature at sensor in degrees Fahrenheit. -999 if sensor does not read temperature.                   | Numeric      |
| dist_to_water_ft | Distance from sensor to water level in feet. -999 if sensor is not capable of taking measurement.        | Numeric      |
| dist_to_floor_ft | Distance from sensor to dry floor of river, creek in feet. -999 if sensor cannot take measurement.       | Numeric      |
| alert_triggered  | Yes, No, or Not Supported if sensor supports alert levels and alert was triggered.                       | Text         |
| sensor_status    | Status of the sensor: Normal, Malfunction, Low Battery                                                   | Text         |


**weather.csv**
| Feature Name     | Description                                                                                              | Data Type    |
| :--------------- | :------------------------------------------------------------------------------------------------------- | :----------- |
| date             | Date and Time when the value was read by the sensor in local time. ISO6801 Format: YYYY:MM:DD hh:mm:ss   | DateTime     |
| sensor_id        | Sensor unique identifier.                                                                                | Alphanumeric |
| vendor           | Vendor that owns the sensor. Vendors are ITRON and ATT.                                                  | Text         |
| sensor_model     | The manufacturer model number of the sensor.                                                             | Alphanumeric |
| latitude         | Latitude of sensor.                                                                                      | Numeric      |
| longitude        | Longitude of sensor.                                                                                     | Numeric      |
| zone             | The zone where sensor is installed: Brooks, Downtown, Medical Center.                                    | Text         |
| temp_f           | Temperature at sensor in degrees Fahrenheit. -999 if sensor does not read temperature.                   | Numeric      |
| humidity         | Relative Humidity.                                                                                       | Numeric      |
| dewpoint_f       | Dew point in degrees fahrenheit.                                                                         | Numeric      |
| pressure_pa      | Atmospheric pressure in Pascal (PA).                                                                     | Numeric      |
| alert_triggered  | Yes, No, or Not Supported if sensor supports alert levels and alert was triggered.                       | Text         |
| sensor_status    | Status of the sensor: Normal, Malfunction, Low Battery                                                   | Text         |
