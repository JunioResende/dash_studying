import pandas as pd
from dash import Dash, html, dash_table

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# Create a Dash app
app = Dash(__name__)

# exibe o dataframe
app.layout = html.Div([
    html.H1('Exibicao do dataframe'),
    dash_table.DataTable(
        data=df.to_dict('records'),
        page_size=10,
    )
])


# Run the app
if __name__ == '__main__':
    app.run_server(
        debug=True,
        host='192.168.0.194',
        port=3000,
        dev_tools_hot_reload=True,
    )