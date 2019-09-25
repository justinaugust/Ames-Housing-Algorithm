#set your database to snake case
def snake_df(dataframe):
    for column in dataframe.columns:
        try:
            dataframe[column] = dataframe[column].str.lower()
        except:
            pass
    dataframe.columns = dataframe.columns.str.lower().str.replace(" ","_")
