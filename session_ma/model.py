# import pandas as pd 
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# df = pd.read_csv(r'C:\Abdelouaheb\perso\Data_science_2024_projects\Deployement\streamlit_flask_app_basics\session_ma\diabetes.csv')

# y = df['Outcome']
# x= df.drop(columns='Outcome')

# pipline = Pipeline([
#     ("scaler" , MinMaxScaler()),
#     ("model" ,  RandomForestClassifier(random_state=42))
# ])

# x_t,x_te,y_t,y_te = train_test_split(x,y,test_size=.25,random_state=20,stratify=y)

# model = pipline.fit(x_t,y_t)

# y_pred_train = model.predict(x_t)
# y_pred_test = model.predict(x_te)

# train_acc= accuracy_score(y_pred_train,y_t)
# test_acc= accuracy_score(y_pred_test,y_te)


# print("train_acc:",train_acc)


# print("test_acc:",test_acc)

# import joblib
# joblib.dump(model,"random_fores.pkl")

import joblib
import numpy as np


model= joblib.load("random_fores.pkl")

x_test= np.array([[1,148,72,35,0,33.6,0.555,50]])

y= model.predict(x_test)

print(y)