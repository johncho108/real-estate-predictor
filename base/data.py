import pandas as pd
import numpy as np

def clean(dataset):
    dataset.dropna(inplace=True)
    dataset.drop(columns=['id','date','sqft_above','sqft_basement','yr_renovated','zipcode','lat','long', 'sqft_living15', 'sqft_lot15', 'yr_built'], inplace=True)
    for col in dataset.columns: 
        if col == 'waterfront' or col == 'view':
            continue
        print("Feature:", col)
        outliers_list = outliers(dataset, col)
        remove_outliers(dataset, outliers_list)
        print('Outliers removed!')
        dataset.reset_index(drop=True, inplace=True)

def outliers(dataset, feature):
    col = dataset[feature]
    outliers_list = []
    for i, val in enumerate(col):
        z_score = (val - col.mean()) / col.std()
        if abs(z_score) > 4.5:
            outliers_list.append(i)
    return outliers_list

def remove_outliers(dataset, outliers):
    dataset.drop(outliers, inplace=True)

dataset = pd.read_csv('base/kc_house_data.csv')
clean(dataset)
dataset.to_csv('base/kc_house_data_cleaned.csv', index=False)