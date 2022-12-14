import plotly.graph_objects as go
import numpy as np
import pandas as pd


"""N = 100
x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

fig = go.Figure()

fig.add_traces(go.Scatter(x=x, y=random_y0, mode="markers", name="markers"))

fig.add_traces(go.Scatter(x=x, y=random_y1,
               mode="lines+markers", name="lines+markers"))

fig.add_traces(go.Scatter(x=x, y=random_y2, mode="lines", name="lines"))

fig.show()"""


"""fig = go.Figure(data=go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3]),
    hovertemplate="R$ %{y} - %{marker.size}"
))

fig.show()"""

df = pd.read_excel("dados.xlsx", sheet_name="TESTE")

fig = go.Figure(
    data=(
        go.Bar(df, x="Data" y=[3, 120, 6]), name"Demandas"
    )
)
