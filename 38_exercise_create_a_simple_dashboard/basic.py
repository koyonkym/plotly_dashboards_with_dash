#######
# Objective: build a dashboard that imports OldFaithful.csv
# form the data directory, and displays a scatterplot.
# The field names are:
# 'D' = data of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minutes)
# 'Y' = waiting time until the next eruption in minutes (to nearest minute)
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Launch the application
app = dash.Dash()

# Create a DataFrame from the .csv file:
df = pd.read_csv('../data/OldFaithful.csv')

# Create a Dash layout that contains a Graph component:
app.layout = html.Div([dcc.Graph(id='old_faithful',
                                 figure={'data':[go.Scatter(x=df['X'],y=df['Y'],mode='markers')],
                                         'layout':go.Layout(title='Old Faithful Eruptions',xaxis={'title':'Duration'},yaxis={'title':'Interval'})})])

# Add the server clause:
if __name__ == '__main__':
    app.run_server()