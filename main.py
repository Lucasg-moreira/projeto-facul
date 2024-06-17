import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path = 'customers.csv';
try:
    dict = {}

    chunk_iterator = pd.read_csv(file_path, chunksize=1000, compression=None)

    for i, chunk in enumerate(chunk_iterator): 
        for row_index, row in chunk.iterrows():
            country = row['Country']

            if country in dict:
                dict[country] = dict[country] + 1
            else:
                dict[country] = 0
    

    labels = ["Brasil", "Argentina", "Chile"]
    values = [dict['Brazil'], dict['Argentina'], dict['Chile']]

    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.show()
    
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found. Please provide the correct file path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")