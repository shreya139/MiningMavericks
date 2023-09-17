# MiningMaverick
# DATASET : [The Weather of 187 Countries in 2020](https://www.kaggle.com/datasets/amirhoseinsedaghati/the-weather-of-187-countries-in-2020/code?select=the+weather+of+187+countries+in+2020.csv)
## About Dataset
This dataset provides information about the weather obseravation of 187 countries/regions,spanning from January 22, 2020 to July 27, 2020.
There are six elements to this project:
1. Introduction
2. Data Preprocessing
3. Data visualization
4. Modeling
5. Inference
6. Conclusion

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

# 2. Data Preprocessing
1. Eliminating meaningless attributes
> **DAPR, MDPR, WESD, PRCP_ATTRIBUTES, TAVG_ATTRIBUTES, TMAX_ATTRIBUTES, TMIN_ATTRIBUTES, SNWD_ATTRIBUTES:** These columns have a high percentage of missing values (over 99%), and it's unlikely they will provide meaningful insights. It's advisable to remove them.
2. Changed Data type
> DATE attribute is change from object to datatime.
3. Handled Null Values and Duplicate Instances
> There are missing value of TAVG,TMAX,TMIN so by grouping by STATION attribute of Country we will fill those missing values with the mean of correspondin attribute. Even after that these attributes contains null values so by grouping by Country we handeled these values.
> There are *22456* duplicate instances so all these instances are dropped.
4. Latitude and Longitude
> Missing value of Latitude and Longitude is managed by using geopandas library but in this dataset we dont have exact address of station in country only station id is provided so those stations will have common geocodes of their corresponding country.
# 3. Data Visualization
We have tried to made inference from this data by using 
* Boxplot of Precipitation, Temperature Average, Maximum Temperature and Minimum Temperature to know the distribution of data
* scatter plot of **TAVG v/s PRCP**,**TMAX v/s TMIN** and **County/Region v/s PRCP**.
* Correlationn heatmap.
* Pie Chart for Country wise distribution.
* Histogram of TAVG,TMAX and TMIN.
* Time Series Plot of Average Temperature for Station CA004016699 of Canada.
* Box Plot of Average Temperaturen (TAVG) by month of Station CA004016699 of Canada.
# 4. Modeling
### 1. Country Wise Precipitation **(PRCP)** prediction
   - Linear Regression
   - Polynomial Regression
   - Stochastic Gradient Descent (SGD)
   - Lasso Regression
   - Ridge Regression
   - Autoregressive Integrated Moving Average (ARIMA)
### 2. Station Wise Average Temperature **(TAVG)** prediction
   - Forecasting next 7 days TAVG using Linear Regression
   - Autoregressive Integrated Moving Average (ARIMA)
   - Lasso Regression
   - Ridge Regression
# Contributors
* Dhruv Solanki (202218053)  - 
* Shreya Arora (202218032) -
* Zeel Gudhka (202218025) -
* Dhruvi Kotecha (202218009) - 
* Mayank Gour (202101072) - 
