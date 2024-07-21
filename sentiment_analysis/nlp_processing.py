from transformers import pipeline

def initialize_nlp_pipeline():
    sentiment_analyzer = pipeline('sentiment-analysis')
    return sentiment_analyzer

if __name__ == "__main__":
    nlp_pipeline = initialize_nlp_pipeline()
    print(nlp_pipeline("The stock market is doing great!"))
