import requests
import pandas as pd

#url = 'https://www.tiobe.com/tiobe-index/'
url = 'https://dimayor.com.co/estadisticas/'

html = requests.get(url).content
df_list = pd.read_html(html)

df = df_list[-1]
print(df)
df.to_csv('output1.csv')