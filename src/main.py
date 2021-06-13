
import pandas as pd

import networkx as nx
import matplotlib.pyplot as plt

def eval(df):
    from ast import literal_eval
    for col in df.columns:
        df[col] = df[col].apply(lambda x: int(x))
    return df

if __name__ == '__main__':
    data_df = pd.read_csv('../data/startup.com.csv', index_col=['Item'])

    matrix = data_df[data_df.columns[6:]]
    matrix = matrix.fillna(0)

    matrix = eval(matrix)
    G = nx.from_pandas_adjacency(matrix, create_using=nx.DiGraph)

    nx.draw_networkx(G, with_labels=True)
    labels = nx.draw_networkx_labels(G, pos=nx.spring_layout(G))
    plt.show()
    print("Done")