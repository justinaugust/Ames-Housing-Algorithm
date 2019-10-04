import pandas as pd
#set your database to snake case
def snake_df(dataframe):
    for column in dataframe.columns:
        try:
            dataframe[column] = dataframe[column].str.lower()
        except:
            pass
    dataframe.columns = dataframe.columns.str.lower().str.replace(" ","_")

def read_it(test):
    if test == True:
        df = pd.read_csv('datasets/test.csv')
    else:
        df = pd.read_csv('datasets/train.csv')
    print(df.shape)
    return(df)

def save_it(df, test):
    if test == True:
        file_name = 'datasets/test_cleaned.csv'
    else:
        file_name = 'datasets/train_cleaned.csv'
    df.to_csv(file_name, index=False)
    print(f'CSV saved to {file_name}')
