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


## Data Dictionary
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
| sensor_status   | Status of the sensor: Normal, Malfunction, Low Battery, etc.                                             | Text         |

