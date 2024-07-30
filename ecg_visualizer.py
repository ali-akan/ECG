import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pandas as pd
import io
import base64
from plotly.subplots import make_subplots
import webbrowser
from threading import Timer

app = dash.Dash(__name__)

# Define a set of colors for the traces
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

app.layout = html.Div([
    html.Div(id='header-container', children=[
        html.H2("ECG Data Visualization Program", style={'text-align': 'center', 'color': '#333', 'font-size': '24px', 'margin': '10px 0'}),
        dcc.Upload(
            id='upload-data',
            children=html.Button('Open CSV File', style={'backgroundColor': '#007bff', 'color': 'white', 'border': 'none', 'padding': '8px 16px', 'cursor': 'pointer', 'font-size': '14px'}),
            multiple=False,
            style={'display': 'flex', 'justify-content': 'center', 'margin': '10px auto', 'width': 'fit-content', 'padding': '5px'}
        ),
        dcc.Dropdown(id='channel-dropdown', multi=True, style={'margin': '10px'})
    ], style={'backgroundColor': '#f0f0f0', 'padding': '5px 0', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)', 'margin-bottom': '10px'}),

    dcc.Graph(id='ecg-plot', config={'displayModeBar': True, 'scrollZoom': True}),
    
    html.Div([
        dcc.RangeSlider(
            id='time-slider',
            marks={i: f'{i:.2f}' for i in range(0, 101, 10)},
            value=[0, 100],  # Default range
            updatemode='drag',
            included=True
        )
    ], style={
        'position': 'fixed',
        'bottom': '0',
        'left': '0',
        'width': '100%',
        'backgroundColor': '#f0f0f0',
        'padding': '5px',
        'boxShadow': '0 -2px 5px rgba(0,0,0,0.1)'
    }),
    html.Div(id='slider-time-range', style={'text-align': 'center', 'padding': '5px', 'color': '#555'})
], style={'height': '100vh', 'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-between', 'backgroundColor': '#f5f5f5'})

@app.callback(
    [Output('channel-dropdown', 'options'),
     Output('channel-dropdown', 'value'),
     Output('time-slider', 'min'),
     Output('time-slider', 'max'),
     Output('time-slider', 'value'),
     Output('header-container', 'style')],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename')]
)
def update_dropdown(contents, filename):
    if contents is None:
        return [], [], 0, 100, [0, 100], {'backgroundColor': '#f0f0f0', 'padding': '5px 0', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)', 'margin-bottom': '10px'}
    
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    
    # Check if the first column is time or index
    try:
        df[df.columns[0]] = pd.to_numeric(df[df.columns[0]], errors='coerce')
        is_time = df[df.columns[0]].notna().all()
    except Exception:
        is_time = False

    options = [{'label': f'Signal {i + 1}', 'value': col} for i, col in enumerate(df.columns[1:])]
    
    min_time = df[df.columns[0]].min()
    max_time = df[df.columns[0]].max() if is_time else len(df) * 0.008
    
    header_style = {'backgroundColor': '#f0f0f0', 'padding': '2px 0', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)', 'margin-bottom': '5px'} if contents else {'backgroundColor': '#f0f0f0', 'padding': '5px 0', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)', 'margin-bottom': '10px'}
    
    return options, [col for col in df.columns[1:]], min_time, max_time, [min_time, max_time], header_style

@app.callback(
    [Output('ecg-plot', 'figure'),
     Output('slider-time-range', 'children')],
    [Input('channel-dropdown', 'value'),
     Input('time-slider', 'value')],
    [State('upload-data', 'contents')]
)
def update_graph(selected_channels, slider_range, contents):
    if contents is None or not selected_channels:
        return go.Figure(), 'Select a time range'
    
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    
    is_time = pd.api.types.is_numeric_dtype(df[df.columns[0]])
    
    if is_time:
        x_data = df[df.columns[0]]
    else:
        x_data = df.index * 0.008
    
    slider_min, slider_max = slider_range
    
    x_data_filtered = x_data[(x_data >= slider_min) & (x_data <= slider_max)]
    df_filtered = df[(x_data >= slider_min) & (x_data <= slider_max)]
    
    fig = make_subplots(
        rows=len(selected_channels),
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.02
    )
    
    for i, (channel, color) in enumerate(zip(selected_channels, colors)):
        fig.add_trace(go.Scatter(
            x=x_data_filtered,
            y=df_filtered[channel],
            mode='lines',
            name=f'Signal {i + 1}',
            line=dict(color=color)
        ), row=i + 1, col=1)
    
    fig.update_layout(
        xaxis=dict(
            title='Time',
            range=[slider_range[0], slider_range[1]],  # Dynamically set x-axis range
            showgrid=True,
            zeroline=False,
            gridcolor='lightgray'
        ),
        title='',
        showlegend=True,
        margin=dict(l=50, r=0, t=0, b=120),
        height=400
    )

    for i in range(len(selected_channels)):
        fig.update_yaxes(
            title=f'S {i + 1}',
            row=i + 1,
            col=1,
            gridcolor='lightgray'
        )

    return fig, f'Time range: {slider_range[0]:.2f} to {slider_range[1]:.2f} seconds'

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

if __name__ == '__main__':
    if not app.run_server.__defaults__:
        Timer(1, open_browser).start()
    app.run_server()
