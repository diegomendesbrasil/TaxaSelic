import requests
import pandas as pd

#Meta Selic - COPOM
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json&dataInicial=01/06/2022"
response = requests.get(url)
response.raise_for_status()  
data = response.json()

df = pd.DataFrame(data)

df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
df['valor'] = df['valor'].astype(float)

print(df)