import pandas as pd
import pickle
import xgboost
from sklearn import preprocessing

def decision_tree_predict():
    datas = pd.read_csv("Datas/S15.csv").drop('Subject', axis=1)
    model = pickle.load(open("Datas/decision_tree_model.sav", 'rb'))
    X = datas.iloc[:,0:25]
    cat_cols = ['Gender']
    for col in cat_cols:
        lbl = preprocessing.LabelEncoder()
        lbl.fit(list(X[col].values.astype('str')))
        X[col] = lbl.transform(list(X[col].values.astype('str')))

    prediction = model.predict(X)
    return prediction

def random_forest_predict():
    datas = pd.read_csv("Datas/S15.csv").drop('Subject', axis=1)
    model = pickle.load(open("Datas/random_forest_model.sav", 'rb'))
    X = datas.iloc[:,0:25]
    cat_cols = ['Gender']
    for col in cat_cols:
        lbl = preprocessing.LabelEncoder()
        lbl.fit(list(X[col].values.astype('str')))
        X[col] = lbl.transform(list(X[col].values.astype('str')))

    prediction = model.predict(X)
    return prediction

def xgboost_predict():
    datas = pd.read_csv("Datas/S15.csv").drop('Subject', axis=1)
    model = pickle.load(open("Datas/xgb_model.sav", 'rb'))
    X = datas.iloc[:,0:25]
    cat_cols = ['Gender']
    for col in cat_cols:
        lbl = preprocessing.LabelEncoder()
        lbl.fit(list(X[col].values.astype('str')))
        X[col] = lbl.transform(list(X[col].values.astype('str')))

    prediction = model.predict(X)
    return prediction