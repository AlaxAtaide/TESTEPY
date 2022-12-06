import pandas as pd
import plotly.express as px

df = pd.read_excel("dados.xlsx", sheet_name="TESTE")


# Remove a linha dos "Totais" localizado na linha 10 do dataframe
df.drop(10, axis=0, inplace=True)

fig = px.pie(df, values='Total Geral', names='Data', hole=.3,
             color_discrete_sequence=px.colors.sequential.ice,
             title='GEPEF - EMAILS RECEBIDOS')
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide', title_x=0.5)


fig.show()
