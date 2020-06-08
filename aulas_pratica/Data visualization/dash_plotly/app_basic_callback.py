# dash components
import dash
import dash_core_components as dcc
import dash_html_components as html
# data
import pandas as pd
import numpy as np
# plotly
from dash.dependencies import Input, Output

# reading data
df = pd.read_csv('data/gapminderDataFiveYear.csv')

# instantiate server
app = dash.Dash()

# year options
year_options = []
for year in df['year'].unique():
    year_options.append({'label':str(year),'value':year})

# country options
country_options = []
for country in df['country'].unique():
    country_options.append({'label':country,'value':country})
    
# layout
app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id='id-year',
                     options=year_options,
                     value=year_options[0]['value'])
    ], style={'width': '50%', 'display': 'inline-block'}),
    html.Div([
        dcc.Dropdown(id='id-country',
                     options=country_options,
                     value=country_options[0]['value'])
    ],  style={'width': '50%', 'display': 'inline-block'}),
    html.Div(id='output-div')
])

@app.callback(Output(component_id='output-div', component_property='children'),
              [Input(component_id='id-year', component_property='value'),
               Input(component_id='id-country', component_property='value')])
def update_output(year, country):
    return '\n Population: {} milhões'.format(int(df.loc[np.logical_and(df['year']==year,
                                                                         df['country']==country), 'pop'].values[0]/1e6))

if __name__ == '__main__':
    # run server
    app.run_server()