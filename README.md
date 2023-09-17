# MiningMaverick
# DATASET : [The Weather of 187 Countries in 2020](https://www.kaggle.com/datasets/amirhoseinsedaghati/the-weather-of-187-countries-in-2020/code?select=the+weather+of+187+countries+in+2020.csv)
## About Dataset
This dataset provides information about the weather obseravation of 187 countries/regions,spanning from January 22, 2020 to July 27, 2020.
There are six elements to this project:
1. Introduction
2. Data Cleaning
3. Data visualization
4. Data Preprocessing
5. Modeling
6. Inference
7. Conclusion

# 1. Introduction

The dataset contains 1,392,575 instances and 23 columns.
The Feature Explanations:
* **STATION:** The station identifier
* **Country/Region:** The country or region where the station is located
* **DATE:** The date of the weather observation in YYYY-MM-DD format
* **Year:** The year of the weather observation
* **Month:** The month of the weather observation
* **Day:** The day of the weather observation
* **PRCP:** The amount of precipitation (rain or snow)
* **SNWD:** The depth of snow on the ground
* **TAVG:** The average temperature
* **TMAX:** The maximum temperature
* **TMIN:** The minimum temperature
* **SNOW:** The amount of snowfall
* **LATITUDE:** The latitude of the station's location
* **LONGITUDE:** The longitude of the station's location
* **ELEVATION:** The elevation of the station's location
* **PRCP_ATTRIBUTES:** Additional attributes for the precipitation data
* **TAVG_ATTRIBUTES:** Additional attributes for the average temperature data
* **TMAX_ATTRIBUTES:** Additional attributes for the maximum temperature data
* **TMIN_ATTRIBUTES:** Additional attributes for the minimum temperature data
* **DAPR:** The number of days since the last precipitation of any amount
* **MDPR:** The multiday precipitation total
* **WESD:** The water equivalent of the snow depth on the ground
* **SNWD_ATTRIBUTES:** Additional attributes for the snow depth data

# 2. Data Cleaning

**DAPR, MDPR, WESD, PRCP_ATTRIBUTES, TAVG_ATTRIBUTES, TMAX_ATTRIBUTES, TMIN_ATTRIBUTES, SNWD_ATTRIBUTES:** These columns have a high percentage of missing values (over 99%), and it's unlikely they will provide meaningful insights. It's advisable to remove them.There are *22456* duplicate instances so all these instances are dropped.

# Contributors
* Dhruv Solanki (202218053)  - 
* Shreya Arora (202218032) -
* Zeel Gudhka (202218025) -
* Dhruvi Kotecha (202218009) - 
* Mayank Gour (202101072) - 
