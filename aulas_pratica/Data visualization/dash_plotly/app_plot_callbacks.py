# dash components
import dash
import dash_core_components as dcc
import dash_html_components as html
# data
import pandas as pd
# plotly
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from plotly.graph_objs.layout import slider


def app_callbacks(slider=True):

    # reading data
    df = pd.read_csv('data/gapminderDataFiveYear.csv')

    # instantiate server
    app = dash.Dash()

    # check input type: slider or dropdown
    if slider:
        # slider options
        slider_min, slider_max = df['year'].min(), df['year'].max() 
        slider_step = 5

        # layout
        app.layout = html.Div([
            dcc.Graph(id='graph'),
            dcc.Slider(id='year-picker',
                       min=slider_min,
                       max=slider_max,
                       step=slider_step,
                       marks={int(year): str(year) for year in df['year'].unique()},
                       value=slider_min)
        ])
    
    # dropdown
    else:
        # we need to construct a dictionary of dropdown values for the years
        year_options = []
        for year in df['year'].unique():
            year_options.append({'label':str(year),'value':year})
        
        # layout
        app.layout = html.Div([
            html.Div([html.H3('Ano:'),
                      dcc.Dropdown(id='year-picker',
                                   options=year_options,
                                   value=df['year'].min())],
                                   style={'width': '10%',
                                          'display': 'inline-block',
                                          'vertical-align': 'top'}),
            html.Div([html.H3('Evolução do PIB no mundo:'),
                      dcc.Graph(id='graph')],
                                style={'width': '90%',
                                       'display': 'inline-block'})],
                                        style={'padding': '20px'})
   
    @app.callback(Output(component_id='graph', component_property='figure'),
                [Input(component_id='year-picker', component_property='value')])
    def update_figure(selected_year):
        filtered_df = df[df['year'] == selected_year]
        traces = []
        for country in filtered_df['country'].unique():
            df_by_country = filtered_df[filtered_df['country'] == country]
            traces.append(go.Scatter(
                x=df_by_country['gdpPercap'],
                y=df_by_country['lifeExp'],
                text=df_by_country['country'],
                mode='markers',
                opacity=0.7,
                marker={'size': 15},
                name=country
            ))

        return {
            'data': traces,
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                hovermode='closest'
            )
        }
    
    # run server
    app.run_server()

if __name__ == '__main__':
    app_callbacks(slider=True)
