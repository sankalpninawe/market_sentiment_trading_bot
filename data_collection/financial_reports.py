import pandas as pd

def load_financial_reports(file_path):
    data = pd.read_csv(file_path)
    return data

if __name__ == "__main__":
    financial_data = load_financial_reports('financial_reports.csv')
    print(financial_data.head())
