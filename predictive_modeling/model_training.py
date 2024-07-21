from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    joblib.dump(model, 'trading_model.pkl')

if __name__ == "__main__":
    X_train = pd.read_csv('features_train.csv')
    y_train = pd.read_csv('labels_train.csv')
    train_model(X_train, y_train)
