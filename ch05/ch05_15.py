from sklearn.preprocessing import Imputer

# Join the two feature matrices
X_complete = np.vstack((X_with_nan, X))

imputer = Imputer(strategy='most_frequent', axis=0)

imputer.fit_transform(X_complete)