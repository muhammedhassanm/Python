# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:33:16 2020

@author: Muhammed Hassan M
"""
import pandas as pd  
import numpy as np  
import seaborn as sns
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn import metrics

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score


#Training
train_df = pd.read_csv('C:/Users/Muhammed Hassan M/Desktop/Dataset/Train.csv', na_values="?")

train_df = train_df.drop(columns=['Employee_ID'])
train_df.shape
train_df.describe()
train_df.info()
#train_df[train_df.isnull().any(axis=1)]
train_df.isnull().sum()

train_df["Age"].value_counts()
train_df["Time_of_service"].value_counts()
train_df["Work_Life_balance"].value_counts()
train_df["VAR2"].value_counts()
train_df["VAR4"].value_counts()
train_df["Pay_Scale"].value_counts()

train_df["Age"] = train_df["Age"].fillna(22)
train_df["Time_of_service"] = train_df["Time_of_service"].fillna(6)
train_df["Work_Life_balance"] = train_df["Work_Life_balance"].fillna(1)
train_df["VAR2"] = train_df["VAR2"].fillna(0.7516)
train_df["VAR4"] = train_df["VAR4"].fillna(2)
train_df["Pay_Scale"] = train_df["Pay_Scale"].fillna(8)

train_df.isnull().sum()

train_obj_df = train_df.select_dtypes(include=['object']).copy()
train_obj_df.head()
train_obj_df[train_obj_df.isnull().any(axis=1)]


train_obj_df["Gender"].value_counts()
train_obj_df["Relationship_Status"].value_counts()
train_obj_df["Hometown"].value_counts()
train_obj_df["Unit"].value_counts()
train_obj_df["Decision_skill_possess"].value_counts()
train_obj_df["Compensation_and_Benefits"].value_counts()

cleanup_nums = {"Gender":     {"M": 1, "F": 0},
                "Relationship_Status": {"Married": 1, "Single": 0},
                "Hometown":{"Lebanon":0,"Springfield":1,"Franklin":2,"Washington":3,"Clinton":4},
                "Unit": {"IT":0 ,"Logistics":1,"Sales":2,"Operarions":3,"R&D":4,"Purchasing":5,
                         "Accounting and Finance":6,"Human Resource Management":7,"Marketing":8,
                         "Production":9,"Quality":10,"Security":11},
                "Decision_skill_possess": {"Conceptual":0,"Analytical":1,"Directive":2,"Behavioral":3},
                "Compensation_and_Benefits":{"type0":0,"type1":1,"type2":2,"type3":3,"type4":4}}
train_obj_df.replace(cleanup_nums, inplace=True)
train_obj_df.head()
train_obj_df.dtypes

train_df = train_df.select_dtypes(exclude=['object'])
train_df = pd.concat([train_df, train_obj_df], axis=1, sort=False)
cols = list(train_df.columns)
cols = cols[:16] + cols[17:] +[cols[16]]
train_df = train_df[cols]


corr = train_df.corr()
sns.heatmap(corr)

X = train_df.iloc[:,train_df.columns != 'Attrition_rate']
Y = train_df.iloc[:,22]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state= 0)

model = linear_model.LinearRegression()
model.fit(X_train, Y_train)

coeff_df = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coeff_df)

y_pred = model.predict(X_test)
df = pd.DataFrame({'Actual': Y_test, 'Predicted': y_pred})
print(df.head(10))

df.plot(kind='bar',figsize=(10,8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

# Root Mean Squared Deviation
rmsd = np.sqrt(mean_squared_error(Y_test, y_pred))      
r2_value = r2_score(Y_test, y_pred)                     

print("Intercept: \n", model.intercept_)
print("Root Mean Square Error \n", rmsd)
print("R^2 Value: \n", r2_value)


#TESTING
test_df = pd.read_csv('C:/Users/Muhammed Hassan M/Desktop/Dataset/Test.csv')
test_df_copy = test_df.copy()

test_df.isnull().sum()
test_df = test_df.drop(columns=['Employee_ID'])
test_df.shape
test_df.describe()
test_df.info()

test_df["Age"].value_counts()
test_df["Time_of_service"].value_counts()
test_df["Work_Life_balance"].value_counts()
test_df["VAR2"].value_counts()
test_df["VAR4"].value_counts()
test_df["Pay_Scale"].value_counts()

test_df["Age"] = test_df["Age"].fillna(22)
test_df["Time_of_service"] = test_df["Time_of_service"].fillna(6)
test_df["Work_Life_balance"] = test_df["Work_Life_balance"].fillna(1)
test_df["VAR2"] = test_df["VAR2"].fillna(0.7516)
test_df["VAR4"] = test_df["VAR4"].fillna(2)
test_df["Pay_Scale"] = test_df["Pay_Scale"].fillna(8)

test_df.isnull().sum()

test_obj_df = test_df.select_dtypes(include=['object']).copy()
test_obj_df.head()
test_obj_df[test_obj_df.isnull().any(axis=1)]


test_obj_df["Gender"].value_counts()
test_obj_df["Relationship_Status"].value_counts()
test_obj_df["Hometown"].value_counts()
test_obj_df["Unit"].value_counts()
test_obj_df["Decision_skill_possess"].value_counts()
test_obj_df["Compensation_and_Benefits"].value_counts()

cleanup_nums = {"Gender":     {"M": 1, "F": 0},
                "Relationship_Status": {"Married": 1, "Single": 0},
                "Hometown":{"Lebanon":0,"Springfield":1,"Franklin":2,"Washington":3,"Clinton":4},
                "Unit": {"IT":0 ,"Logistics":1,"Sales":2,"Operarions":3,"R&D":4,"Purchasing":5,
                         "Accounting and Finance":6,"Human Resource Management":7,"Marketing":8,
                         "Production":9,"Quality":10,"Security":11},
                "Decision_skill_possess": {"Conceptual":0,"Analytical":1,"Directive":2,"Behavioral":3},
                "Compensation_and_Benefits":{"type0":0,"type1":1,"type2":2,"type3":3,"type4":4}}
test_obj_df.replace(cleanup_nums, inplace=True)
test_obj_df.head()
test_obj_df.dtypes

test_df = test_df.select_dtypes(exclude=['object'])
test_df = pd.concat([test_df, test_obj_df], axis=1, sort=False)
cols = list(test_df.columns)
cols = cols[:16] + cols[17:] +[cols[16]]
test_df = test_df[cols]

X = test_df.iloc[:,test_df.columns != 'Attrition_rate']
X["Attrition_rate"] = model.predict(X)


result_df = test_df_copy[["Employee_ID"]].copy()
result_df["Attrition_rate"] = X["Attrition_rate"]
result_df.to_csv('C:/Users/Muhammed Hassan M/Desktop/Dataset/submission.csv',index=False)
