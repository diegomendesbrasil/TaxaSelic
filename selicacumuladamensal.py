import requests
import pandas as pd

#selic acumulada mensal
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4390/dados?formato=json"
response = requests.get(url)
response.raise_for_status()  
data = response.json()

df = pd.DataFrame(data)

df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
df['valor'] = df['valor'].astype(float)

print(df)

