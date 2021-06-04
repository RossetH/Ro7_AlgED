import pandas as pd  # importação/exportação de dados
import numpy as np

dataset_path = "exercise-list-4/datasets/euro_players.txt"

dataset = pd.read_table(filepath_or_buffer = dataset_path,sep = "\t", comment = "#")

#Task 1
weight_median = dataset['kg'].median()

#Task 2
team_n_registered = dataset.groupby('team')['name'].size()

#Task 3
age_mean = dataset['age'].median()

#Task 4
dataset['cm'].quantile([.1,.9])

#Task 5
max_goal = (dataset['goal'].max())

#Task 6
max_goal = (dataset['cm'].max())

#Task 7
dataset.sort_values(by=['rt'])['name'].head(10)

#Task 8
dataset.sort_values(by=['cm'])['name'].head(10)

#Task 9
dataset.loc[dataset['apps'] > 0]

#Task 10
dataset[['yel','red','goal','ass']].fillna(0)

#Task 11
for i in range(0,100,5):
    dataset.loc[dataset['age'].between(i, i+5, inclusive=True), 'age_group'] = f'{i}-{i+5}'

#Task 12
age_group_size = dataset.groupby('age_group')['name'].size()

#Task 13
team_age_mean = dataset.groupby('team')['age'].mean()

#Task 14
country_weight_median = dataset.groupby('country')['kg'].median()

#Task 15
pos_height_mean = dataset.groupby('pos')['cm'].mean()

#Task 16
team_rt_mean = dataset.groupby('team')['rt'].mean()

#Task 17
max_goal_byteam = dataset.groupby('team')['goal'].nlargest(1)

#Task 18
dataset.groupby('team')['goal'].agg(Mean='mean', Std='std', Max='max', Min='min')
dataset.groupby('team')['goal'].max()-dataset.groupby('team')['goal'].min()

#Task 19
dataset['bmi'] = dataset['kg']/np.power(dataset['cm']/100,2)

#Task 20
dataset.groupby('team')['goal'].std()
dataset.groupby('team')['cm'].mean()
dataset.groupby('team')['bmi'].max()-dataset.groupby('team')['bmi'].min()

#Task 21
dataset.loc[dataset['bmi'].lt(18.5), 'bmi_group'] = 'Below normal weight'
dataset.loc[dataset['bmi'].between(18.5, 25, inclusive=True), 'bmi_group'] = 'Normal weight'
dataset.loc[dataset['bmi'].between(25, 30, inclusive=True), 'bmi_group'] = 'Overweight'
dataset.loc[dataset['bmi'].between(30, 35, inclusive=True), 'bmi_group'] = 'Class I Obesity'
dataset.loc[dataset['bmi'].between(35, 40, inclusive=True), 'bmi_group'] = 'Class II Obesity'
dataset.loc[dataset['bmi'].gt(40), 'bmi_group'] = 'Obesity'