import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

d = pd.read_csv("data.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Health'),
    html.Div(children="Unsafe drinking water in countries"),
    dcc.Graph(
        id='country-geo-graph',
        figure= px.scatter_geo(d, locations="iso", color="UWD",
                     hover_name="country", size="UWD",template="plotly_white",
                     projection="natural earth")
    ),
    html.P(children='''
        Visualising current health conditions globally
    ''')
])

if __name__ == '__main__':
    app.run_server(debug=True)
