import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from tools.db.helpers import DbStockPriceHelper
from tools.db.helpers import DbHelper
from tools.other import Tools
from tools.other import Time

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
        options=DbHelper.getSymbolDictForFrontEndUse(),
        value='TSLA'
    ),
    dcc.Dropdown(
        id='my-dropdown2',
        options=DbHelper.getSymbolDictForFrontEndUse(),
        value='TSLA'
    ),
    dcc.Dropdown(
        id='my-dropdown3',
        options=DbHelper.getSymbolDictForFrontEndUse(),
        value='TSLA'
    ),
    dcc.Dropdown(
        id='my-dropdown4',
        options=DbHelper.getSymbolDictForFrontEndUse(),
        value='TSLA'
    ),
    dcc.Dropdown(
        id='options',
        options=[
            {'label': 'Normalize', 'value': 'Normalize'},
            {'label': 'Do not Normalize', 'value': 'Do not Normalize'},
        ],
        value='Do not Normalize'
    ),
    dcc.Dropdown(
        id='daterange',
        options=[
            {'label': 'Last Hour', 'value': 'last hour'},
            {'label': 'Last Day', 'value': 'last day'},
            {'label': 'Last 2 Days', 'value': 'last 2 days'},
            {'label': 'Last Week', 'value': 'last week'},
            {'label': 'Max', 'value': 'max'},
        ],
        value='Last Hour'
    ),
    dcc.Graph(id='my-graph'),
    dcc.Graph(id='my-graph2'),
    dcc.Graph(id='my-graph3'),
    dcc.Graph(id='my-graph4')
], className="container")

def updateGraphHelper(selected_dropdown_value, normalizeStr, dateRange):
    if "Do not" in str(normalizeStr):
        normalize = False
    else: normalize = True
    if "last hour" in dateRange:
        dateRange = Time.getDateOffset("hour -1")
    elif "last day" in dateRange:
        dateRange = Time.getDateOffset("day -1")
    elif "last 2 days" in dateRange:
        dateRange = Time.getDateOffset("day -2")
    else: dateRange = "1900-01-01"
    dateList = DbStockPriceHelper.getStockPriceTsOverTimeDateFilter(selected_dropdown_value,dateRange)
    priceList = DbStockPriceHelper.getStockPriceOverTimeDateFilter(selected_dropdown_value,dateRange)
    if normalize:
        maxMin = Tools.getMaxMinFromArray(priceList)
        priceList = Tools.normalizeArray(priceList,maxMin)
    return {
        'data': [{
            'x': dateList,
            'y': priceList,
            'line': {
                'width': 2,
                'shape': 'spline'
            }
        },
        ],
        'layout': {
            'margin': {
                'l': 30,
                'r': 20,
                'b': 30,
                't': 20
            },
            'legend': 'asddas'
        }
    }

@app.callback(Output('my-graph', 'figure'),
              [Input('my-dropdown', 'value'), Input('options', 'value'),Input('daterange', 'value')],)
def update_graph(selected_dropdown_value, normalizeStr, dateRange):
    return updateGraphHelper(selected_dropdown_value, normalizeStr, dateRange)

@app.callback(Output('my-graph2', 'figure'),
              [Input('my-dropdown2', 'value'), Input('options', 'value'),Input('daterange', 'value')],)
def update_graph(selected_dropdown_value, normalizeStr, dateRange):
    return updateGraphHelper(selected_dropdown_value, normalizeStr, dateRange)

@app.callback(Output('my-graph3', 'figure'),
              [Input('my-dropdown3', 'value'), Input('options', 'value'),Input('daterange', 'value')],)
def update_graph(selected_dropdown_value, normalizeStr, dateRange):
    return updateGraphHelper(selected_dropdown_value, normalizeStr, dateRange)

@app.callback(Output('my-graph4', 'figure'),
              [Input('my-dropdown4', 'value'), Input('options', 'value'),Input('daterange', 'value')],)
def update_graph(selected_dropdown_value, normalizeStr, dateRange):
    return updateGraphHelper(selected_dropdown_value, normalizeStr, dateRange)

if __name__ == '__main__':
    app.run_server(host= '0.0.0.0')