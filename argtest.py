
# import argparse

# parser = argparse.ArgumentParser(description='Dataset analysis script')
# parser.add_argument('config', type=str, help='Path to the configuration file')
# args = parser.parse_args()


# import yaml


# config_paths = ['user_config.yml']
# paths = args.config(config_paths)

# print (config_paths)



'''Part one Load data and explore'''
import pandas as pd



import yaml


config_paths = ['user_config.yml']
# config_paths = args.config


#open config file
config = {}
for path in config_paths:
    with open (path, 'r') as f:
        this_config = yaml.safe_load(f)
        config.update(this_config)

# print(config)

# Load the data to a single DataFrame.
'''the path would be a userspecific configuration'''
Data = config['dataset']
# path = args.config
bus_data = pd.read_excel(Data)
# #^Job specific



'''### Grouping and aggregating
1. Use `groupby()` to split your data into groups based on one of the columns.
2. Use `agg()` to apply multiple functions on different columns and create a summary table. Calculating group sums or standardizing data are two examples of possible functions that you can use.
'''


Daily_bus_data = bus_data.groupby(['Day'])


Summary_table = Daily_bus_data.agg(Delay_counts = ('Min Delay', 'count'),Mean_Delay=('Min Delay','mean'),
                   Mean_Gap= ('Min Gap', 'mean'))



Summary_table



'''1. Plot two or more columns in your data using `matplotlib`, `seaborn`, or `plotly`. Make sure that your plot has labels, a title, a grid, and a legend.'''


import matplotlib.pyplot as plt

Summary_table.plot(y=config['columns'], kind='bar', ylabel= config['plot_config']['ylabel'], xlabel=config['plot_config']['xlabel'], title=config['plot_config']['title']).grid()


# plt.savefig('summary_table.png')
