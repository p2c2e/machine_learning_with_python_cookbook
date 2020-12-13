# Import library
import sklearn

# Get scikit-learn version
scikit_version = joblib.__version__

# Save model as pickle file
joblib.dump(model, "model_{version}.pkl".format(version=scikit_version))