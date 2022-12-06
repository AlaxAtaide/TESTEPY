import pandas as pd
import plotly.express as px


df = pd.read_excel("dados.xlsx", sheet_name="TESTE")

# Exclui colunas sem valores

df = df.dropna(how="any", axis=1)

# Exclui colunas indesejadas do dataframe
df.drop('Total Geral', axis=1, inplace=True)
df.drop('Percentual', axis=1, inplace=True)


# Remove a linha dos "Totais" localizado na linha 10 do dataframe
#df.drop(10, axis=0, inplace=True)


# Exclui colunas indesejadas, que não quero que puxe pro elemento gráfico

# Renomeando a coluna "Data", pois o nome não representa os dados da coluna
df = df.rename(columns={"Data": "Demandas"})

# "Melting" o dataframe, ou seja, fazendo o que foi descrito acima
df_new = df.melt(id_vars=["Demandas"], value_vars=[
                 c for c in df.columns if c != "Demandas"])


# Fazendo o gráfico
fig = px.bar(df_new, x='variable', y='value', color='Demandas', text_auto=True,
             title='Evolução // Gepef - Negocial')

fig.update_xaxes(range=[-0.5, 6.5])
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide', title_x=0.5)

fig.show()
