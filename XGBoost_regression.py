import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor


np.random.seed(0)

def categorize_aspect_ratio(entry):
    if entry == '2:3':
        return 4
    elif entry == '1:2':
        return 3
    elif entry == '3:5':
        return 2
    else:
        return 1

# Dataset
countries = pd.read_csv('in_data/world_flags_2024.csv')

color_columns = ['White', 'Red', 'Blue', 'Black', 'Yellow', 'Green', 'Orange', 'OtherColor']
objects_columns = ['White', 'Red', 'Blue', 'Black', 'Yellow', 'Green', 'Orange', 'OtherColor',
                   'LeftTriangle', 'Canton', 'Cross', 'Crescent', 'Stars', 'Sun', 'Bird', 'Circle', 'BlazonOrOther']

# Add columns (feature engineering)
countries['TotalColors'] = countries[color_columns].sum(axis=1)
countries['TotalMarks'] = countries[objects_columns].sum(axis=1)
countries['Ratio'] = countries['AspectRatio'].apply(categorize_aspect_ratio)

# Remove possible outliers
countries = countries[countries['Population'] > 100000]
countries = countries[countries['GDPPerCapita'] > 1000]

cols = ['White', 'Red', 'Blue', 'Black', 'Yellow', 'Green', 'Orange', 'OtherColor',
        'StripesEqual', 'StripesVertical', 'StripesHorizontal', 'StripesDiagonal', 'StripesOther', 'SingleColor',
        'LeftTriangle', 'Canton', 'Cross', 'Sun', 'Bird', 'Circle', 'BlazonOrOther',
        'Ratio']

# Features
X = countries[cols]
# Target valules
y = countries['GDPPerCapita']

# Split the dataset into testing and training portions
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=71)

# Classification model
reg = GradientBoostingRegressor(n_estimators=120, max_depth=3)

# Fit the model with the training data
reg.fit(X_train, y_train)

# Make predictions
predictions = reg.predict(X_test)

df = pd.DataFrame(y_test).reset_index()
df['Preds'] = predictions
print(df.head(100))

# Accuracy of the model
mae = np.absolute(np.subtract(df['GDPPerCapita'].to_numpy(), df['Preds'].to_numpy())).mean()
print(mae)
