import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import os
for dirname,_,filenames in os.walk("input"):
    for filename in filenames:
        print(os.path.join(dirname,filename))

df=pd.read_csv("Musical_instruments_5.csv")
df.shape
df.head()
df=df[["reviewText","overall"]]
df.columns=["review","ratings"]
df.head()
df.isnull().sum()

df=df.dropna().reset_index(drop=True)
df.isnull().sum()

df["ratings"].unique()
df["ratings"].value_counts()

with plt.style.context(style="fivethirtyeight"):
    ax=df["ratings"].value_counts().plot.bar(figsize=(18,8),fontsize=15)
    plt.title(label="Analysing rating feature")
    plt.xlabel(xlabel="Rating labels")
    plt.ylabel(ylabel="Number of records")
    plt.show()

with plt.style.context(style="fivethirtyeight"):
    ax=df["ratings"].value_counts().plot.pie(figsize=(10,10),fontsize=10,autopct="%.2f%%",startangle=90)
    plt.title(label="Analysing rating feature")
    plt.show()
