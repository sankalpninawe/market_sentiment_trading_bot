from nlp_processing import initialize_nlp_pipeline

def score_sentiments(texts):
    sentiment_analyzer = initialize_nlp_pipeline()
    scores = [sentiment_analyzer(text) for text in texts]
    return scores

if __name__ == "__main__":
    sample_texts = ["The stock market is booming!", "There is a recession coming."]
    sentiment_scores = score_sentiments(sample_texts)
    print(sentiment_scores)
