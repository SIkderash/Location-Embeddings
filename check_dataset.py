import pandas as pd
import os

dataset_names = ['pek', 'jkt', 'nyc', 'tky', 'ist']

for dataset_name in dataset_names:
    print(dataset_name.capitalize())
    raw_df = pd.read_hdf(os.path.join('data', '{}.h5'.format(dataset_name)), key='data')
    coor_df = pd.read_hdf(os.path.join('data', '{}.h5'.format(dataset_name)), key='poi')
    print("Dataset days:", raw_df['datetime'].dt.day.unique(), end = "\n\n")