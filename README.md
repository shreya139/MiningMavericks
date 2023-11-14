# MiningMaverick: Course Project 3
# DATASET: [ICC Cricket World Cup 2023 ML Challenge](https://www.kaggle.com/datasets/pardeep19singh/icc-mens-world-cup-2023)
The latest data has also been scrapped from https://cricsheet.org/

# 1. Introduction
## Dataset Description
The 2023 ICC Men's Cricket World Cup is the 13th edition of the Cricket World Cup, a quadrennial One Day International (ODI) cricket tournament contested by men's national teams and organized by the International Cricket Council (ICC). The source of this dataset is Cricsheet. Cricsheet provides ball and ball data for most cricket tournaments. It contains 22579 instances for 22 attributes.

Here are brief descriptions for each attribute in the New York State hospital inpatient discharge dataset:
1. match_id: unique identifier of each match
2. season: ICC Cricket World season during which the match took place
3. start_date: The date when the match started
4. venue: The location or stadium where the match was played
5. innings: The inning number (1st inning, 2nd inning, etc.) in the match.
6. ball: The ball number in the current over including the over
7. batting_team: The team that is currently batting.
8. bowling_team: The team that is currently bowling.
9. striker: The batsman facing the current delivery.
10. non_striker: The batsman at the non-striker's end.
11. bowler: The bowler delivering the current ball.
12. runs_off_bat: The number of runs scored off the bat (excluding extras).
13. extras: Extra runs scored, including wides, no-balls, byes, leg byes, and penalties.
14. wides: The number of wide deliveries bowled for the current ball
15. noballs: The number of no-ball deliveries bowled for the current ball
16. byes: The number of runs scored as byes.
17. legbyes: The number of runs scored as leg byes.
18. penalty: The number of runs scored as penalties.
19. wicket_type: The type of wicket if a wicket fell (e.g., caught, bowled, lbw).
20. player_dismissed: The player who got dismissed, if any.
21. other_wicket_type: The type of dismissal for a wicket, other than the primary batsman's dismissal
22. other_player_dismissed: The player who got dismissed in addition to the primary batsman.

# 2. Data Preprocessing and Feature Engineering:
1. Handeling Null Values and Duplicate Instances
> 'wides', 'noballs', 'byes', 'legbyes', and 'penalty' previously had null values, indicating no runs were scored in these categories. These null values have been replaced with 0, signifying that no additional runs were added.
> For 'wicket_type' and 'other_wicket_type', which denoted the type of dismissal, null values have been replaced with a new category 'no wicket,' reflecting that no wicket fell during those deliveries.
> Similarly, null values in 'player_dismissed' and 'other_player_dismissed,' representing the dismissed player's name, have been substituted with 'no dismissal,' indicating that no player was dismissed during those instances.

3. Feature Engineering:
The following features have been derived to create the necessary dataset for modelling:
> 1. wicket: Binary indicator (1 or 0) for whether a wicket fell in the current delivery.
> 2. over: The current over number.
> 3. ball_num: The current ball number of the over.
> 4. ball_left: The number of balls remaining in the match.
> 5. total_runs: The total runs scored by the batting team in the current delivery.
> 6. score: The current score of the batting team.
> 7. wickets_remaining: The number of wickets yet to fall for the batting team.
> 8. run_rate: The run rate calculated as the ratio of total runs to the number of overs bowled.
> 9. target: The target score set for the second inning in limited-overs matches.
> 10. winner: The team that won the match.
> 11. req_runs: The required runs for the chasing team to win, in case of second innings.
> 12. req_rr: The required run rate for the chasing team to win, in case of second innings.
> 13. result: The result of the match if the batting team won (1) or lost (0).

# 3. [EDA](https://github.com/shreya139/MiningMavericks/blob/Dhruvi-Kotecha/202218009_Data_Mining_Project3.ipynb)
We have performed univariate analysis for categorical attributes to understand the distribution of data for each category. Bar graphs with percentage have been plotted for the same.

# 4. Modelling
### Task 1:
#### 1. [Predicting the player who will hit the most sixes in the tournament](https://github.com/shreya139/MiningMavericks/blob/main/CP03_T28_Task1_most_sixes.ipynb)
Additional attributes such as strike rate, balls played, and the number of sixes have been engineered to enhance the dataset for the specific prediction task. This involved creating new features that provide insights into a batsman's performance, including their scoring rate, the number of deliveries faced, and the frequency of hitting sixes. Similarly, the [player who will hit the most fours](https://github.com/shreya139/MiningMavericks/blob/Dhruv-Solanki/CP03_Prediction_Max_Fours.ipynb) has also been predicted.

Furthermore, to facilitate model training, label encoding has been applied to categorical variables such as venue, batsmen, and team.

LSTM has been used for predicting the number of sixes. The choice of LSTM for this task is apt due to the inherent sequential nature of cricket match data. Ball-by-ball events influence a batsman's performance over time, and LSTMs excel at capturing patterns in sequential data with long-term dependencies. This makes them well-suited for analyzing and predicting outcomes in cricket matches, where the order of events is crucial in understanding player performance.
      
#### 2. [Training the model to predict Wicket Fall](https://github.com/shreya139/MiningMavericks/blob/main/CP3.py)
Our model training endeavors focused on predicting the likelihood of a wicket falling based on the current delivery statistics. Given the substantial class imbalance, we explored both Oversampling and Undersampling techniques to evaluate the model's performance. We employed Random Forest and Logistic Regression for training, and further experimented with Sequential Deep Learning and Functional API Deep Learning methods to enhance predictive capabilities.
   
### Task 2: [Predicting the Finalist Teams](https://github.com/shreya139/MiningMavericks/blob/main/CP03_T28_Task2_%26_Task3.ipynb)
In our attempt to predict the outcome of cricket matches, specifically whether the batting team will win or not, we employed various machine learning ensemble techniques and deep learning methods. The features used for prediction include 'venue', 'batting_team', 'bowling_team', 'ball', 'score', 'run_rate', 'req_rr', 'ball_left', 'req_runs', 'wickets_remaining', and 'target.'

Here is a summary of the models implemented and their respective accuracies:

1. **Logistic Regression:**
         - Test Set Accuracy: 93.22%

2. **Gradient Boosting:**
         - Test Set Accuracy: 100.00%

3. **XGBoost:**
         - Test Set Accuracy: 100.00%

4. **CatBoost:**
         - Test Set Accuracy: 100.00%

5. **LGBMClassifier:**
         - Test Set Accuracy: 100.00%

6. **MLP (Multi-Layer Perceptron):**
         - Test Set Accuracy: 100.00%

      For the prediction of semi-final winners and final winners, we opted for the Categorical Boost Classifier. The prediction was based on the match state after the first ball of the first innings, assuming no runs were scored initially. The average run rate of the respective teams was utilized for these predictions.

      While all the ensemble models and deep learning techniques achieved 100% accuracy on the test data, the Categorical Boost Classifier was chosen for its superior speed, efficiency, memory usage, and deployment considerations compared to other models. This decision factors in not only accuracy but also practical aspects that make the chosen model more suitable for real-world applications.

      The two finalist teams have also been predicted using features ['venue', 'innings', 'total_runs', 'run_rate', 'batting_team', 'bowling_team'] using Sequential Deep Learning Technique. The accuracy of [this model](https://github.com/shreya139/MiningMavericks/blob/main/202218009_Data_Mining_Project3.ipynb) is 99.97%.
      
### Task 3: [Predict the Winner of ICC Cricket World Cup 2023](https://github.com/shreya139/MiningMavericks/blob/main/CP03_T28_Task2_%26_Task3.ipynb)
The same methodology used in Task 2, involving various machine learning ensemble techniques and deep learning methods, has been applied to predict the winner of the ICC Cricket World Cup 2023. The features considered for this prediction likely include relevant cricket match data, and the chosen models were likely trained on historical data to make predictions for the World Cup matches.

# 5. Conclusion
In Task 1, our model predicts that Glenn Maxwell (GJ Maxwell) will hit the most sixes, followed by Mitchell Marsh (MR Marsh). This prediction is based on the features and methodology used in Task 1, which involves historical player performance data during the series. Rohit Sharma and Glenn Maxwell are predicted to hit the most fours.

The introduction of oversampling to predict wicket fall has significantly enhanced the model's performance, leading to high accuracy levels on both the validation and test sets. This improvement is particularly noteworthy for Random Forest models, as they tend to benefit from a balanced class distribution. Contrastingly, undersampling appears to have had a detrimental effect on the Random Forest model's performance. This outcome is likely attributed to the loss of information from the majority class, potentially posing challenges for the model to generalize effectively with a reduced representation of the majority class. In the realm of deep learning, the Sequential API, coupled with early stopping, achieved moderate accuracy. However, further fine-tuning or exploration of alternative architectures may be necessary to optimize its performance. On the other hand, the model constructed using the Functional API, incorporating features like batch normalization and skip connections, demonstrated improvements over the Sequential model. This observation suggests that a more intricate architecture, particularly one with skip connections, has the capacity to capture more nuanced patterns within the data.

As per our model's predictions for the semi-final winners, India is anticipated to emerge victorious in the first semi-final, securing a spot in the finals. Nevertheless, when both South Africa and Australia are granted the opportunity to bat first, their probabilities of winning are notably high. Specifically, if South Africa assumes the batting position first, the model assigns a 99% chance of victory for the team.

Our predictive analysis focused on forecasting the ultimate winners, considering the potential finalists, South Africa and Australia. Notably, South Africa emerges as the frontrunner. In the scenario where India faces Australia in the finals, our model indicates a 95% probability of India winning if Australia bowls first, while the probability increases to 98% if India assumes the bowling position first.

Should the finals feature India against South Africa, the likelihood of India winning is estimated at 83% if South Africa bowls first. Conversely, if India takes the bowling initiative, their chances decrease to 42% for securing victory and clinching the ICC World Cup trophy.

# Contributors
* Dhruv Solanki (202218053)
* Shreya Arora (202218032)
* Zeel Gudhka (202218025)
* Dhruvi Kotecha (202218009)
* Mayank Gour (202101072)

---

---


# MiningMaverick: Course Project 2
# DATASET: [New York State Hospital Inpatient Discharge](https://www.kaggle.com/datasets/thedevastator/2010-new-york-state-hospital-inpatient-discharge/)
# 1. Introduction
## Dataset Description
The Statewide Planning and Research Cooperative System (SPARCS) Inpatient De-identified dataset is a wealth of information, containing discharge level detail on various aspects of hospital inpatient discharges in New York State during the year 2010. It contains 2622133 instances for 37 attributes.

Here are brief descriptions for each attribute in the New York State hospital inpatient discharge dataset:
1. Health Service Area: The geographic region of the hospital where the patient received care.
2. Hospital County: The county in which the hospital is located.
3. Operating Certificate Number: A unique identifier for hospitals, typically in integer format.
4. Facility ID: The name of the hospital where the patient was admitted.
5. Facility Name: The name of the hospital where the patient was admitted.
6. Age Group: The age group to which the patient belongs.
7. Zip Code -3 digit: The first three digits of the patient's zip code.
8. Gender: The gender of the patient.
9. Race: The race of the patient.
10. Ethnicity: The ethnicity of the patient.
11. Length of Stay: The duration of the patient's inpatient stay, typically in days.
12. Type of Admission: The type of admission for the patient, such as elective, urgent, or emergency.
13. Patient Disposition: The disposition of the patient after discharge, e.g., home, other facility, or expired.
14. Discharge Year: The year in which the patient was discharged.
15. CCS Diagnosis Code: Clinical Classification Software (CCS) diagnosis code assigned to the patient.
16. CCS Diagnosis Description: Description of the CCS diagnosis code.
17. CCS Procedure Code: Clinical Classification Software (CCS) procedure code assigned to the patient.
18. CCS Procedure Description: Description of the CCS procedure code.
19. APR DRG Code: All Patient Refined Diagnosis Related Group (APR DRG) code assigned to the patient.
20. APR DRG Description: Description of the APR DRG code.
21. APR MDC Code: All Patient Refined Major Diagnostic Category (APR MDC) code assigned to the patient.
22. APR MDC Description: Description of the APR MDC code.
23. APR Severity of Illness Code: Severity of illness code assigned to the patient within APR.
24. APR Severity of Illness Description: Description of the severity of illness.
25. APR Risk of Mortality: APR's assessment of the patient's risk of mortality.
26. APR Medical Surgical Description: Description of whether the patient's case was medical or surgical.
27. Source of Payment 1: The primary source of payment for the patient's medical expenses.
28. Source of Payment 2: A secondary source of payment for the patient's medical expenses if applicable.
29. Source of Payment 3: A tertiary source of payment for the patient's medical expenses if applicable.
30. Attending Provider License Number: The license number of the attending healthcare provider responsible for the patient's care.
31. Operating Provider License Number: The license number of the healthcare provider who performed any surgeries or procedures on the patient.
32. Other Provider License Number: The license number of any other healthcare provider involved in the patient's care.
33. Birth Weight: The weight of the newborn at birth if applicable.
34. Abortion Edit Indicator: An indicator that may denote whether the admission was related to an abortion.
35. Emergency Department Indicator: An indicator to specify if the patient's admission originated from the emergency department.
36. Total Charges: The total charges for the patient's medical care, typically in monetary units.
37. Total Costs: The total costs incurred by the hospital for providing medical care to the patient, typically in monetary units.

# 2. Data Preprocessing
1. Eliminating meaningless attributes
> **index, Discharge Year, Abortion Edit Indicator:** index attribute is repetitive and Discharge Year & Abortion Edit Indicator has the same value for all instances, hence they do not provide any meaningful conclusion.
2. Handeling Null Values and Duplicate Instances
> There are a few missing values for some of the attributes. Since there percentage was less than 0.2%, we have dropped these instances. 'Other Provider License Number','Operating Provider License Number' have been dropped due to large number of missing values. The null values in 'Source of Payment 2' and 'Source of Payment 3' have been replaced by a category called 'Unused'.
3. Feature Selection
> There are multiple attributes which provide description for already existing attributes, hence these columns have been dropped. Columns with datatype 'Object' have been encoded using LabelEncoder. 'Length of Stay' and 'Zip Code - 3 digits' attributes have been changed from Object to Float.

# 3. EDA
We have performed univariate analysis for categorical attributes to understand the distribution of data for each category. Bar graphs with percentage have been plotted for the same.

# 4. Modelling
### 1. Prediction of Risk of Mortality has been performed using the following Machine Learning Models
      - Logistic Regression
      - Decision Tree
      - Random Forest
      - Naive Bayes
      - K-Nearest Neighbours
      - One vs Rest
### 2. Prediction of Source of Payment 1
   This has been done in two ways:
      - Prediction of all 10 classes using Decision Tree and Logistic Regression
      - Prediction of only 2 (most popular) classes using Decision Tree and Logistic Regression
### 3. Prediction of APR Severity of Illness
      - Logistic Regression
      - Decision Tree
      - Random Forest
      - Gradient Boosting Classifier
      - Naive Bayes
      - Sequential Method (Deep Learning)
      - Functional API Method (Deep Learning)
### 4. Prediction of Medical Surgical Description
      - Logistic Regression
      - Bagging and Boosting

# 5. Conclusion
After experimenting with several models to predict the Risk of Mortality, we have determined that the Decision Tree model performs the best in this scenario, possibly due to addressing the class imbalance.

When predicting Source of Payment 1, we observed that Decision Tree overfits the data, whereas Logistic Regression, while achieving lower accuracy, does not suffer from overfitting in either case.

Random Forest and Deep Learning models demonstrate superior performance when predicting the severity of illness. XGBoost (XGB) performs exceptionally well in predicting medical surgical descriptions.

# Contributors
* Dhruv Solanki (202218053)
* Shreya Arora (202218032)
* Zeel Gudhka (202218025)
* Dhruvi Kotecha (202218009)
* Mayank Gour (202101072)

---

---

      

# Course Project 1
# DATASET : [The Weather of 187 Countries in 2020](https://www.kaggle.com/datasets/amirhoseinsedaghati/the-weather-of-187-countries-in-2020/code?select=the+weather+of+187+countries+in+2020.csv)
## About Dataset
This dataset provides information about the weather obseravation of 187 countries/regions,spanning from January 22, 2020 to July 27, 2020.
There are six elements to this project:
1. Introduction
2. Data Preprocessing
3. Data visualisation
4. Modeling
5. Conclusion

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
