import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
from numpy import random

app = dash.Dash()

df = pd.read_csv('../data/mpg.csv')
# Adding Noise, adding jitter
# 1978.2, 1977.7
df['year'] = random.randint(-4,5,len(df))*0.1 + df['model_year']

app.layout = html.Div([
    html.Div([
      dcc.Graph(id='mpg-scatter',
                figure={
                    'data':[go.Scatter(
                        x=df['year']+1900,
                        y=df['mpg'],
                        text=df['name'],
                        # hoverinfo='text'+'y'+'x',
                        mode='markers'
                    )],
                    'layout':go.Layout(title='MPG Data',
                                      xaxis={'title':'Model Year'},
                                      yaxis={'title':'MPG'},
                                      hovermode='closest')
                })        
    ],style={'width':'50%','display':'inline-block'}),
    html.Div([
        dcc.Graph(id='mpg_line',
                  figure={'data':[go.Scatter(x=[0,1],
                                             y=[0,1],
                                             mode='lines')],
                          'layout':go.Layout(title='Acceleration',margin={'l':0})})
    ],style={'width':'20%','height':'50%','display':'inline-block'})
])

@app.callback(Output('mpg_line','figure'),
              [Input('mpg-scatter','hoverData')])
def callback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    figure = {'data':[go.Scatter(x=[0,1],
                                 y=[0,60/df.iloc[v_index]['acceleration']],
                                 mode='lines')],
              'layout':go.Layout(title=df.iloc[v_index]['name'],
                                 xaxis={'visible':False},
                                 yaxis={'visible':False,'range':[0,60/df['acceleration'].min()]},
                                 margin={'l':0},
                                 height=300)}
    return figure

if __name__ == '__main__':
    app.run_server()