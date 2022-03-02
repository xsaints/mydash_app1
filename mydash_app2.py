import dash
from dash import html, dcc
import plotly.express as px


app = dash.Dash(__name__)

app.layout = html.Div([

	html.H1('Hello')





])






if __name__ == '__main__':
	app.run_server(debug= True)

