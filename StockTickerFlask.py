import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from tools.db.helpers import DbStockPriceHelper

import flask
import pandas as pd
import time
import os

server = flask.Flask('app')
server.secret_key = os.environ.get('secret_key', 'secret')

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')

app = dash.Dash('app', server=server)

app.scripts.config.serve_locally = False
dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

app.layout = html.Div([
    html.H1('Doomberg Stock Tickers'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'},
            {'label': 'SPY', 'value': 'SPY'},
            {'label': 'KraneWebShares', 'value': 'KWEB'},
            {'label': 'Net Worth', 'value': 'NETWORTH'}
        ],
        value='TSLA'
    ),
    dcc.Graph(id='my-graph')
], className="container")

@app.callback(Output('my-graph', 'figure'),
              [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    dateList = DbStockPriceHelper.getStockPriceTsOverTime(selected_dropdown_value)
    priceList = DbStockPriceHelper.getStockPriceOverTime(selected_dropdown_value)
    return {
        'data': [{
            'x': dateList,
            'y': priceList,
            'line': {
                'width': 3,
                'shape': 'lines'
            }
        }],
        'layout': {
            'margin': {
                'l': 30,
                'r': 20,
                'b': 30,
                't': 20
            }
        }
    }

if __name__ == '__main__':
    app.run_server(host= '0.0.0.0')