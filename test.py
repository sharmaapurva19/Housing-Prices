import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

housing_df = pd.read_csv('housing_data.csv')
housing_df = housing_df.drop(['MSZoning', 'LotConfig', 'BldgType', 'Exterior1st'], axis=1)

housing_df = housing_df.dropna(subset=['BsmtFinSF2', 'TotalBsmtSF', 'SalePrice'])

X = housing_df.drop('SalePrice', axis=1)
y = housing_df['SalePrice']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(X_train, y_train)

change by apuva
