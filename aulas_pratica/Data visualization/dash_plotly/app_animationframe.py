# dash components
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# plotly
import plotly.express as px

# data
import pandas as pd

# reading data
df = pd.read_csv('data/gapminderDataFiveYear.csv')
print(df.head())

# instantiate server
app = dash.Dash()

# build animation figure
fig1 = px.scatter_geo(df,
                     locations="country",
                     color='country',
                     locationmode='country names',
                     hover_name="country",
                     size="gdpPercap",
                     animation_frame='year',
                     projection="natural earth")

# configurando o layout do título
fig1.update_layout(title={'text': "Evolução do PIB per capita",
                         'y':0.95,
                         'x':0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'})

# animation frame layout
app.layout = html.Div(children=[
    html.H1(children='Dados mundiais',
            style={'textAlign': 'center'}),
    dcc.Graph(id='graph', figure=fig1)])

if __name__ == '__main__':
    app.run_server()