import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gas_df = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gas_df, x='dia', y='venda')
  grafico.set(title='Gas Price São Paulo Jul/2021', xlabel='Day', ylabel='Price')
  plt.savefig('gasolina.png', format='png')