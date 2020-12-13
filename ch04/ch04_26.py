# Load library
from sklearn.preprocessing import Imputer

# Create imputer
mean_imputer = Imputer(strategy="mean", axis=0)

# Impute values
features_mean_imputed = mean_imputer.fit_transform(features)

# Compare true and imputed values
print("True Value:", true_value)
print("Imputed Value:", features_mean_imputed[0,0])