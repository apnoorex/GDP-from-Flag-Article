import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier


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
    
def categorize_aspect_ratio_gdp(entry):
    if entry < 25000:
        return 'A'
    elif entry < 50000:
        return 'B'
    elif entry < 75000:
        return 'C'
    else:
        return 'D'

# Dataset
countries = pd.read_csv('in_data/world_flags_2024.csv')

# Add columns (feature engineering)
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

# Target values
countries['GDPPerCapitaCat'] = countries['GDPPerCapita'].apply(categorize_aspect_ratio_gdp)
y = countries['GDPPerCapitaCat']

# Split the dataset into testing and training portions
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=71)

# Classification model
clf = GradientBoostingClassifier(n_estimators=120, max_depth=3)

# Fit the model with the training data
clf.fit(X_train, y_train)

# Make predictions
predictions = clf.predict(X_test)

# Accuracy of the model
acc = np.sum(predictions == y_test) / len(y_test)
print(acc)
