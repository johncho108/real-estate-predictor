import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

def fit_regression(*features, visualize=False):
    features_to_drop = ['price','condition','bathrooms','sqft_lot','floors','waterfront','view']
    for feature in features:
        features_to_drop.remove(feature)
    dataset = pd.read_csv('base/kc_house_data_cleaned.csv')
    x = dataset.drop(columns=features_to_drop).to_numpy()
    y = dataset['price'].to_numpy()
    x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=0)
    regression = LinearRegression()
    regression.fit(x_train, y_train)

    if visualize == True:
        y_pred = regression.predict(x_test)
        r2 = r2_score(y_test, y_pred)
        print(r2)
        plt.figure(figsize=(15,10))
        plt.scatter(y_test, y_pred,alpha=0.5)
        plt.title('Actual vs. Predicted House Prices in Millions of Dollars')
        plt.xlabel('Actual')
        plt.ylabel('Predicted')
        plt.show()
    return regression

def predict(regression, *feature_vals):
    vals = [val for val in feature_vals]
    print("feature values:", vals)
    prediction = regression.predict([vals])
    print("Prediction", prediction)
    return prediction

def display(prediction):
    prediction_int = round(prediction.item())
    prediction_str = str(prediction_int)
    prediction_with_commas = ""
    i = len(prediction_str) - 1
    place_keeper = 1
    while i > -1:
        if place_keeper < len(prediction_str) and place_keeper % 3 == 0:
            prediction_with_commas = "," + prediction_str[i] + prediction_with_commas
        else: 
            prediction_with_commas = prediction_str[i] + prediction_with_commas
        place_keeper += 1
        i -= 1
    return "$" + prediction_with_commas




