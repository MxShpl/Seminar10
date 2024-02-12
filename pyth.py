import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI':lst})

df = pd.DataFrame({})

for i in lst:
    if i == "human":
        df = pd.concat([df, pd.DataFrame({'human': [True], 'robot': [False]})], ignore_index=True)
    else:
        df = pd.concat([df, pd.DataFrame({'human': [False], 'robot': [True]})], ignore_index=True)

# print(data.head())
print("У тебя ВОТ ТАК:")
print(df)
print()
print("A НУЖНО ТАК:")
print(pd.get_dummies(data['whoAmI']))