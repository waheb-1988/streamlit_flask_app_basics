from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler,RobustScaler
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split,RandomizedSearchCV,GridSearchCV
from pathlib import Path
import os

file_name = "diabetes.csv"
df= pd.read_csv(os.path.join(file_name))
x= df.drop(columns='Outcome')
print(x.shape)
y= df['Outcome']   
ordinal_categories = {}    
encoding_dict = {}    
pipeline = Pipeline([
    
    ("scaling", MinMaxScaler()),
    ("model", RandomForestClassifier(random_state=42))
])
#


x_t,x_te,y_t,y_te= train_test_split(x,y,test_size=.25,random_state=20, stratify=y)

model = pipeline.fit(x_t,y_t)

# Make Predictions
y_pred_train = model.predict(x_t)
y_pred_test = model.predict(x_te)


# Calculate Accuracy 
train_accuracy  = accuracy_score(y_pred_train,y_t)
test_accuracy  = accuracy_score(y_pred_test,y_te)


print(f"Training Accuracy: {train_accuracy:.2f}")
print(f"Test Accuracy: {test_accuracy:.2f}")


params = {
    'model__n_estimators': [100, 200],
    'model__max_depth': [None, 10, 20, 30],
    'model__min_samples_split': [2, 5],
    'model__min_samples_leaf': [1, 2, 4],
    'model__bootstrap': [True, False]
}
nreg=GridSearchCV(pipeline,param_grid=params,cv=5, verbose=2, n_jobs=-1, scoring='accuracy')

model1 = nreg.fit(x_t,y_t)



print(model1.best_params_)
print(model1.best_score_)
# Make Predictions
model2=model1.best_estimator_

y_pred_train1 = model2.predict(x_t)
y_pred_test1 = model2.predict(x_te)

# Calculate Accuracy 
train_accuracy1  = accuracy_score(y_pred_train1,y_t)
test_accuracy1  = accuracy_score(y_pred_test1,y_te)


print(f"Training Accuracy1: {train_accuracy1:.2f}")
print(f"Test Accuracy1: {test_accuracy1:.2f}")

import joblib
joblib.dump(model2, "random_forest.pkl")