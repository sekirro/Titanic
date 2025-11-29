import pandas as pd

def read_data(file_path):
    return pd.read_csv(file_path)

def main():
    df = read_data('train.csv')
    print(df.head())
    print(df.describe())

if __name__ == '__main__':
    main()