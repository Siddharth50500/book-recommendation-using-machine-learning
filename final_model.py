# -*- coding: utf-8 -*-
"""final model

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t8ssSqPQ73xs9Jskpe8YrBLLQKgnB4P6
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from xgboost import XGBRegressor
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

gpa_data = pd.read_csv('/content/Contact-Information-_Responses_.csv')

pd.read_csv

gpa_data.head()

gpa_data.shape

gpa_data.describe()

gpa_data.info()

gpa_data.isnull().sum()

X = gpa_data.drop(['Timestamp','Name','Email','iq','gender'],axis=1)
Y = gpa_data['iq']

print(X)

print(gpa_data.gender.value_counts())

print(gpa_data['gender'].dtype)

gpa_data['gender'] = gpa_data['gender'].astype(str)

print(gpa_data['gender'].dtype)

print("Before:")
print(gpa_data['gender'].value_counts())

gpa_data['gender'] = gpa_data['gender'].str.lower()
gpa_data.replace({'gender': {'male': 0, 'female': 1}}, inplace=True)

print("After:")
print(gpa_data['gender'].value_counts())

gpa_data['gender'] = gpa_data['gender'].str.strip()  # Remove leading and trailing whitespaces
gpa_data['gender'] = gpa_data['gender'].str.lower()
gpa_data.replace({'gender': {'male': 0, 'female': 1}}, inplace=True)

gpa_data['gender'] = gpa_data['gender'].str.lower()  # Convert to lowercase
gpa_data.replace({'gender': {'male': 0, 'female': 1}}, inplace=True)

print(gpa_data['gender'].unique())

gender_mapping = {'male': 0, 'Male': 0, 'female': 1, 'Female': 1, 'other': -1}
gpa_data['gender'] = gpa_data['gender'].map(gender_mapping)

gpa_data['gender'] = gpa_data['gender'].astype(float)

print(X)

print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, random_state=2)

lin_reg_model = LinearRegression()
lin_reg_model.fit(X_train,Y_train)

training_data_prediction = lin_reg_model.predict(X_train)

error_score = metrics.r2_score(Y_train, training_data_prediction)
print("R squared Error : ", error_score)

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual gpa")
plt.ylabel("Predicted gpa")
plt.title(" Actual gpa vs Predicted gpa")
plt.show()

test_data_prediction = lin_reg_model.predict(X_test)

gpa_data.info()

error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared Error : ", error_score)

plt.scatter(Y_test, test_data_prediction)
plt.xlabel("Actual gpa")
plt.ylabel("Predicted gpa")
plt.title(" Actual gpa vs Predicted gpa")
plt.show()

lass_reg_model = Lasso()
lass_reg_model.fit(X_train,Y_train)

training_data_prediction = lass_reg_model.predict(X_train)

error_score = metrics.r2_score(Y_train, training_data_prediction)
print("R squared Error : ", error_score)

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual gpa")
plt.ylabel("Predicted gpa")
plt.title(" Actual gpa vs Predicted gpa")
plt.show()

test_data_prediction = lass_reg_model.predict(X_test)

error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared Error : ", error_score)

plt.scatter(Y_test, test_data_prediction)
plt.xlabel("Actual gpa")
plt.ylabel("Predicted gpa")
plt.title(" Actual gpa vs Predicted gpa")
plt.show()

regressor = XGBRegressor()

regressor.fit(X_train, Y_train)

training_data_prediction = regressor.predict(X_train)

r2_train = metrics.r2_score(Y_train, training_data_prediction)

print('R Squared value = ', r2_train)

test_data_prediction = regressor.predict(X_test)

r2_test = metrics.r2_score(Y_test, test_data_prediction)

print('R Squared value = ', r2_test)

g1 = pd.read_csv('/content/train.csv')

g1.head()

g1.describe()

g1.info()

g1.isnull().sum()

print(g1['Suggested Book'].value_counts())

g1.replace({'Suggested Book':{'Moderate visual content':0,'High text content (Theory)':1,'High visual content (more Images)':2}},inplace=True)

g1.head(
)

X = g1.drop(['Suggested Book'],axis=1)
Y = g1['Suggested Book']

print(X)

print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, random_state=2)

lin_reg_model = LinearRegression()
lin_reg_model.fit(X_train,Y_train)

training_data_prediction = lin_reg_model.predict(X_train)

error_score = metrics.r2_score(Y_train, training_data_prediction)
print("R squared Error : ", error_score)

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual gpa")
plt.ylabel("Predicted gpa")
plt.title(" Actual gpa vs Predicted gpa")
plt.show()

test_data_prediction = lin_reg_model.predict(X_test)

g1.info()

error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared Error : ", error_score)

plt.scatter(Y_test, test_data_prediction)
plt.xlabel("Actual gpa")
plt.ylabel("Predicted gpa")
plt.title(" Actual gpa vs Predicted gpa")
plt.show()

lass_reg_model = Lasso()
lass_reg_model.fit(X_train,Y_train)

training_data_prediction = lass_reg_model.predict(X_train)

error_score = metrics.r2_score(Y_train, training_data_prediction)
print("R squared Error : ", error_score)

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual gpa")
plt.ylabel("Predicted gpa")
plt.title(" Actual gpa vs Predicted gpa")
plt.show()

test_data_prediction = lass_reg_model.predict(X_test)

error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared Error : ", error_score)

plt.scatter(Y_test, test_data_prediction)
plt.xlabel("Actual gpa")
plt.ylabel("Predicted gpa")
plt.title(" Actual gpa vs Predicted gpa")
plt.show()

regressor = XGBRegressor()

regressor.fit(X_train, Y_train)

training_data_prediction = regressor.predict(X_train)

r2_train = metrics.r2_score(Y_train, training_data_prediction)

print('R Squared value = ', r2_train)

test_data_prediction = regressor.predict(X_test)

r2_test = metrics.r2_score(Y_test, test_data_prediction)

print('R Squared value = ', r2_test)