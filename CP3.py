import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import warnings
warnings.filterwarnings('ignore')

"""#Loading the dataset"""

#data = pd.read_csv('/content/deliveries.csv')
data = pd.read_csv('C:\\Users\\Zeel\\Desktop\\DAIICT\\MScDS_Sem_3\\Data Mining\\CP3\\FastAPI\\deliveries.csv')

data.head()

data.shape

data.info()

"""#Preprocessing and Feature Engineering"""

data.duplicated().sum()

data.drop_duplicates(inplace=True)

missing_value_percentage = (data.isnull().sum() / len(data)) * 100
print(round(missing_value_percentage, 4))

def unique_values_count(data):
  for column in data.columns:
    unique_values = data[column].unique()
    unique_values_without_nan = [value for value in unique_values if pd.notna(value)]
    unique_count = len(unique_values_without_nan)
    print(f"Unique values in '{column}': {unique_count}")

    if unique_count > 0 and unique_count <= 10:
      print(unique_values_without_nan)

unique_values_count(data)

"""Dropping the columns with either only 1 unique value or no value at all"""

columns_to_drop = ['season', 'other_wicket_type', 'other_player_dismissed']
data.drop(columns_to_drop, axis=1, inplace=True)

"""Renaming player_dismissed column as wicket and assigning 1 if there exist any value else 0"""

data.rename(columns={"player_dismissed": "wicket"}, inplace=True)
data["wicket"] = np.where(data["wicket"].notna(), 1, 0)

"""Replacing the null values with 0"""

data[["wides", "noballs", "byes", "legbyes", "penalty"]] = data[["wides", "noballs", "byes", "legbyes", "penalty"]].fillna(0)

"""Replacing the null values with 'no wicket'"""

data.wicket_type.fillna("no wicket", inplace=True)
data.wicket.fillna("no wicket", inplace=True)

data.isna().sum()

"""converting the values in ball column to over and balls_left columns"""

data["ball"] = data["ball"].astype(str)
data[["over", "ball_num"]] = data["ball"].str.split(".", expand=True).astype(int)
data["ball"] = data["ball"].astype(float)
data["over"] = data["over"] + 1
data["balls_left"] = 306 - (data["over"]*6 + data["ball_num"])

"""Calculating total runs"""

data["total_runs"] = data["runs_off_bat"] + data["extras"]

"""Calculating cumulative runs in one inning"""

data["cumulative_runs"] = data.groupby(["match_id", "innings"])["total_runs"].cumsum()

"""calculating run rate"""

data['run_rate'] = data.groupby(["match_id", "innings"]).apply(lambda x: (x['cumulative_runs'] * 6) / (300 - x['balls_left'])).sort_index(level=[0, 1]).values

data.head(3)

"""Creating a result column having values as 0 and 1 depending if the value in wicket_type is nan or notna"""

specific_values = ['caught', 'bowled', 'caught and bowled', 'lbw', 'run out', 'stumped', 'retired hurt']
specific_values_lower = [value.lower() for value in specific_values]

data['wicket_new'] = data['wicket_type'].astype(str).fillna('').str.strip()
data["result"] = data['wicket_new'].str.lower().isin(specific_values_lower).astype(int)

result_counts = data['result'].value_counts()
print(result_counts)

"""Calculating target runs for the team in 2nd innings"""

target_runs = data[data["innings"] == 1].groupby("match_id")["cumulative_runs"].max().reset_index()
target_runs.rename(columns={"cumulative_runs": "target_runs"}, inplace=True)

data = data.merge(target_runs, on="match_id", how="left")

data.loc[data['innings'] == 1, 'target_runs'] = 0
data.loc[data['innings'] == 2, 'target_runs'] += 1

print(data['target_runs'].unique())

data.loc[data['target_runs'] > 0, ['target_runs', 'cumulative_runs', 'balls_left']]

"""Calculating required runs and required run rate"""

mask = data['target_runs'] > 0
print(mask.sum())

data.loc[mask, 'req_runs'] = data.loc[mask, 'target_runs'] - data.loc[mask, 'cumulative_runs']
data.loc[mask, 'req_rr'] = (data.loc[mask, 'req_runs'] * 6) / data.loc[mask, 'balls_left']

print(data.isna().sum())

data.fillna(0, inplace=True)

data

data.columns

"""Creating the final dataframe"""

final_data = data[['batting_team', 'bowling_team', 'wides', 'noballs', 'byes', 'legbyes', 'penalty', 'balls_left', 'cumulative_runs', 'run_rate',
                   'result', 'target_runs', 'req_runs', 'req_rr']]

final_data

final_data.info()

final_data.describe().T

"""Removing inf value in required run rate"""

print("Maximum req_rr value:", final_data['req_rr'].max())
print("Minimum req_rr value:", final_data['req_rr'].min())

final_data = final_data[~(final_data.req_rr > 500)]

final_data.describe().T

final_data.shape

final_data.columns

"""#FastAPI"""

X = final_data.drop('result', axis=1)
y = final_data['result']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

one_hot_cols = ['bowling_team', 'batting_team']
std_scale_cols = ['balls_left', 'cumulative_runs', 'run_rate', 'target_runs', 'req_runs', 'req_rr']

ct = ColumnTransformer(transformers=[
    ('one_hot', OneHotEncoder(sparse=False, drop="first"), one_hot_cols),
    ('scaler', StandardScaler(), std_scale_cols)
])

pipeline = Pipeline([
    ('transformer', ct)
])

X_train_transformed = pipeline.fit_transform(X_train)
X_test_transformed = pipeline.transform(X_test)

classifier = RandomForestClassifier()
classifier.fit(X_train_transformed, y_train)

y_pred = classifier.predict(X_test_transformed)

score = accuracy_score(y_test, y_pred)
score

import pickle
pickle_out = open("classifier.pkl", "wb")
pickle.dump(classifier, pickle_out)

pickle_out.close()

print(X_train_transformed[0])

classifier.predict([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1.308855, -1.3, -0.6, 0.48429005, 0.84556242, 0.35]])