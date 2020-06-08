# main imports
import dash
import dash_core_components as dcc
import dash_html_components as html

# layouts
def run_layout(option=1):
    """Run simple dash server.
    
    Args:
        option (int, optional): Layout type. Defaults to 1.
    """

    # dash app
    app = dash.Dash()    
    app.layout = dcc.Graph()
    # basic layout
    if option==0:

        # dash layout
        app.layout = html.Div(children=[
            html.H1(children='Hello Dash'),
            html.Div(children='Dash: A web application framework for Python.'),

            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Class 1'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Class 2'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
        ])

    # colored layout
    elif option==1:

        colors = {
            'background': '#282b38',
            'text': '#a5b1cd'
        }

        app.layout = html.Div(children=[
            html.H1(
                children='Hello Dash',
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            ),

            html.Div(
                children='Dash: A web application framework for Python.',
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            ),

            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font': {
                            'color': colors['text']
                        },
                        'title': 'Dash Data Visualization'
                    }
                }
            )],
            style={'backgroundColor': colors['background']}
        )
    
    # run server
    app.run_server()

if __name__ == '__main__':
    run_layout(option=1)
