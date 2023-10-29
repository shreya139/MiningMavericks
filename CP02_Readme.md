# Course Project 02
# DATASET : [New York State Hospital Inpatient Discharge]([https://www.kaggle.com/datasets/amirhoseinsedaghati/the-weather-of-187-countries-in-2020/code?select=the+weather+of+187+countries+in+2020.csv](https://www.kaggle.com/datasets/thedevastator/2010-new-york-state-hospital-inpatient-discharge))
## About Dataset
The SPARCS(Statewide Planning and Research Cooperative System) Inpatient De-identified dataset for the year 2010 in New York State is a valuable resource containing comprehensive information about hospital inpatient discharges. 
It covers patient details like age, gender, race, and ethnicity, as well as diagnoses, treatments, services, and charges.
There are six elements to this project:
1. Introduction
2. Data Preprocessing
3. Data visualisation
4. Modeling
5. Conclusion

# 1. Introduction

Here are brief descriptions for each column in our New York State hospital inpatient discharge dataset:

1. **Health Service Area:** The geographic region of the hospital where the patient received care.

2. **Hospital Country:** The country in which the hospital is located.

3. **Operating Certificate Number:** A unique identifier for hospitals, typically in integer format.

4. **Facility ID:** The name of the hospital where the patient was admitted.

5. **Facility Name:** The name of the hospital where the patient was admitted.

6. **Age Group:** The age group to which the patient belongs.

7. **Zip Code -3 digit:** The first three digits of the patient's zip code.

8. **Gender:** The gender of the patient.

9. **Race:** The race of the patient.

10. **Ethnicity:** The ethnicity of the patient.

11. **Length of Stay:** The duration of the patient's inpatient stay, typically in days.

12. **Type of Admission:** The type of admission for the patient, such as elective, urgent, or emergency.

13. **Patient Disposition:** The disposition of the patient after discharge, e.g., home, other facility, or expired.

14. **Discharge Year:** The year in which the patient was discharged.

15. **CCS Diagnosis Code:** Clinical Classification Software (CCS) diagnosis code assigned to the patient.

16. **CCS Diagnosis Description:** Description of the CCS diagnosis code.

17. **CCS Procedure Code:** Clinical Classification Software (CCS) procedure code assigned to the patient.

18. **CCS Procedure Description:** Description of the CCS procedure code.

19. **APR DRG Code:** All Patient Refined Diagnosis Related Group (APR DRG) code assigned to the patient.

20. **APR DRG Description:** Description of the APR DRG code.

21. **APR MDC Code:** All Patient Refined Major Diagnostic Category (APR MDC) code assigned to the patient.

22. **APR MDC Description:** Description of the APR MDC code.

23. **APR Severity of Illness Code:** Severity of illness code assigned to the patient within APR.

24. **APR Severity of Illness Description:** Description of the severity of illness.

25. **APR Risk of Mortality:** APR's assessment of the patient's risk of mortality.

26. **APR Medical Surgical Description:** Description of whether the patient's case was medical or surgical.

27. **Source of Payment 1:** The primary source of payment for the patient's medical expenses.

28. **Source of Payment 2:** A secondary source of payment for the patient's medical expenses if applicable.

29. **Attending Provider License Number**: The license number of the attending healthcare provider responsible for the patient's care.

30. **Operating Provider License Number:** The license number of the healthcare provider who performed any surgeries or procedures on the patient.

31. **Other Provider License Number:** The license number of any other healthcare provider involved in the patient's care.

32. **Birth Weight:** The weight of the newborn at birth if applicable.

33. **Abortion Edit Indicator:** An indicator that may denote whether the admission was related to an abortion.

34. **Emergency Department Indicator:** An indicator to specify if the patient's admission originated from the emergency department.

35. **Total Charges:** The total charges for the patient's medical care, typically in monetary units.

36. **Total Costs:** The total costs incurred by the hospital for providing medical care to the patient, typically in monetary units.

# 2. Data Preprocessing
1. Eliminating meaningless attributes
> **DAPR, MDPR, WESD, PRCP_ATTRIBUTES, TAVG_ATTRIBUTES, TMAX_ATTRIBUTES, TMIN_ATTRIBUTES, SNWD_ATTRIBUTES:** These columns have a high percentage of missing values (over 99%), and it's unlikely they will provide meaningful insights. It's advisable to remove them.
2. Changed Data type
> DATE attribute is change from object to datatime.
3. Handeling Null Values and Duplicate Instances
> There are missing value of TAVG,TMAX,TMIN so by grouping by STATION attribute of Country we will fill those missing values with the mean of correspondin attribute. Even after that these attributes contains null values so by grouping by Country we handeled these values.
> There are *22456* duplicate instances so all these instances are dropped.
4. Latitude and Longitude
> Missing value of Latitude and Longitude is managed by using geopandas library but in this dataset we dont have exact address of station in country only station id is provided so those stations will have common geocodes of their corresponding country.
# 3. Data Visualisation
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
# 5. Conclusion
After a thorough examination of multiple machine learning models on our dataset, we concluded that Simple Linear Regression regularly beats the other models in terms of predicted accuracy. This claim is based on a thorough examination of numerous key performance indicators, such as Root Mean Squared Error (RMSE) and R-squared (R2) values.

Simple Linear Regression consistently had the lowest RMSE throughout our experiment, suggesting its superior capacity to minimize the difference between predicted and actual values. A lower RMSE indicates that this model makes the most accurate predictions when compared to other approaches.

Furthermore, when using Simple Linear Regression, the R-squared (R2) value, which represents the proportion of the variation in the dependent variable that is predictable from the independent variable(s), consistently produced the highest results. A higher R2 implies a better fit of the model to the data, indicating that this model captures a greater amount of the variability in the dataset, making it a reliable choice for our predicting tasks.

In conclusion, our comprehensive testing and careful examination have led us to the unequivocal conclusion that Simple Linear Regression is the best choice among the models studied, consistently demonstrating the lowest RMSE and greatest R-squared values. This finding emphasizes Simple Linear Regression's usefulness in modeling the relationship between our variables and indicates its potential for higher predictive performance in our unique application.
# Contributors
* Dhruv Solanki (202218053)
* Shreya Arora (202218032)
* Zeel Gudhka (202218025)
* Dhruvi Kotecha (202218009)
* Mayank Gour (202101072)
