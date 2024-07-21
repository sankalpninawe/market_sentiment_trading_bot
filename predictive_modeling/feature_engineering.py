import numpy as np

def create_features(sentiment_scores, market_data):
    sentiment_features = np.array([score['score'] for score in sentiment_scores])
    market_features = market_data.values
    features = np.concatenate([sentiment_features.reshape(-1, 1), market_features], axis=1)
    return features
