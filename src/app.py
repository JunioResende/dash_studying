import pandas as pd
from dash import Dash, html, dash_table, dcc, callback, Input, Output
import plotly.express as px

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# Create a Dash app
app = Dash(__name__)

# exibe o dataframe
app.layout = html.Div([
    # exibe o grafico em forma de histograma
    html.H1('Histograma'),
    html.Hr(),
    dcc.RadioItems(
        options=[
            'pop',
            'lifeExp',
            'gdpPercap'
        ],
        value='lifeExp',
        id='radio-controler',
    ),
    dcc.Graph(
        figure={},
        id='histogram-controller',
    ),
    html.H1('Exibicao do dataframe'),
    dash_table.DataTable(
        data=df.to_dict('records'),
        page_size=5,
    ),
])


@callback(
    Output(
        component_id='histogram-controller',
        component_property='figure',
    ),
    Input(
        component_id='radio-controler',
        component_property='value',
    ),
)
def update_graph(col_chosen):
    fig = px.histogram(
        df,
        x='continent',
        y=col_chosen,
        histfunc='avg',
    )
    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(
        debug=True,
        host='192.168.0.194',
        port=3000,
        dev_tools_hot_reload=True,
    )
