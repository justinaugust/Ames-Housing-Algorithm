import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



#code adapted from our visualization lecture

def subplot_scatterz(dataframe, predict_variables, target_variable):
    nrows = int(np.ceil(len(predict_variables)/2)) # Makes sure you have enough rows
    fig, ax = plt.subplots(nrows = nrows,
                           ncols = 2,
                           figsize = (15,6*nrows)
                          ) # You'll want to specify your figsize
    ax = ax.ravel() # Ravel turns a matrix into a vector, which is easier to iterate
    for i, column in enumerate(predict_variables): # Gives us an index value to get into all our lists

        ax[i].scatter(x = dataframe[column],
                      y = dataframe[target_variable],
                      s = 5,
                      alpha = .9,

                     )
        ax[i].set_title(f'{target_variable} by {column}',
                       fontsize = 20)
        ax[i].set_xlabel(column,
                        fontsize = 14)
        ax[i].set_ylabel(target_variable,
                         fontsize = 14

                        )

        plt.tight_layout()

def subplot_boxez(dataframe, predict_variables):
    nrows = int(np.ceil(len(predict_variables)/2)) # Makes sure you have enough rows
    fig, ax = plt.subplots(nrows = nrows,
                           ncols = 2,
                           figsize = (15,6*nrows)
                          ) # You'll want to specify your figsize
    ax = ax.ravel() # Ravel turns a matrix into a vector, which is easier to iterate
    for i, column in enumerate(predict_variables): # Gives us an index value to get into all our lists

        ax[i].boxplot(x = dataframe[column])
        ax[i].set_title(f'{column}',
                       fontsize = 20)

        plt.tight_layout()

def subplot_dists(dataframe, columns):
    nrows = int(np.ceil(len(columns)/3)) # Makes sure you have enough rows
    fig, ax = plt.subplots(nrows = nrows,
                           ncols = 3,
                           figsize = (15,6*nrows)
                          )
    ax = ax.ravel() # Ravel turns a matrix into a vector, which is easier to iterate
    for i, column in enumerate(columns): # Gives us an index value to get into all our lists
        ax[i].hist(x = dataframe[column])
        ax[i].set_title(column,
        fontsize = 20)

        plt.tight_layout()

def graph_greater_than_mean(columns,
                            data,
                            mean_price,
                            target):
    colors = []

    nrows = int(np.ceil(len(columns)/2))
    fig, ax = plt.subplots(nrows = nrows,
                           ncols = 2,
                           figsize = (15,6*nrows)
                          )
    ax = ax.ravel()
    for i, column in enumerate(columns):
        colors = []
        to_graph = data.groupby(by = column).mean()[target].sort_values(ascending=True)
        for col, val in enumerate(to_graph.values):
            if to_graph.values[col] >= mean_price:
                colors.append('g')
            else:
                colors.append('r')
        ax[i].barh(
            y = to_graph.index,
            width = to_graph.values,
            color = colors

        )


        ax[i].set_title(f'{target} by {column}',
                       fontsize = 20)
        ax[i].set_ylabel(column,
                        fontsize = 18)
        ax[i].set_xlabel(target,
                         fontsize = 18
                        )


    plt.tight_layout();
