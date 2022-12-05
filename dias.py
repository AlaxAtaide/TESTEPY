import pandas as pd
import plotly.express as px

df = pd.read_excel("dados.xlsx", sheet_name="TESTE")

# Esclui colunas sem valores

df = df.dropna(how="any", axis=1)

# Exclui colunas indesejadas, que não quero que puxe pro elemento gráfico

df.drop('Total Geral', axis=1, inplace=True)
df.drop('Percentual', axis=1, inplace=True)
fig = px.bar(df, x=df.columns, y='Data', color='variable', text_auto=True,
             title='Evolução // Gepef - Negocial')

fig.update_traces(textposition='inside')
fig.update_yaxes(autorange='reversed')
fig.show()
