import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def is_time_series(series):
    return series.diff().dropna().gt(0).all()

def plot_ecg(csv_file):
    print("Loading CSV file...")
    data = pd.read_csv(csv_file, header=None)
    print("CSV file loaded successfully.")

    if data.shape[0] < data.shape[1]:
        data = data.T  

    if data.shape[1] > 1 and is_time_series(data[0]):
        time = data[0]
        voltages = data.iloc[:, 1:]
    else:
        time = pd.Series(range(len(data))) * 1000.0 / len(data)
        voltages = data

    num_leads = voltages.shape[1]

    # Create a single figure for all leads
    fig = make_subplots(
        rows=num_leads, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03,
        subplot_titles=[f'Lead {i}' for i in range(num_leads)]
    )

    # Add traces for all leads
    for i in range(num_leads):
        fig.add_trace(
            go.Scatter(x=time, y=voltages.iloc[:, i], mode='lines', name=f'Lead {i}'),
            row=i+1, col=1
        )

        fig.update_yaxes(
            title_text=f"Lead {i}",
            row=i+1, col=1,
            fixedrange=False,
            showline=True,
            linewidth=2,
            linecolor="Black"
        )

    # Define dropdown buttons for each lead
    buttons = [
        {
            'args': [{'visible': [i == j for j in range(num_leads)]},
                     {'height': 1000, 'width': 1200}],  # Larger size for selected lead
            'label': f'Show Lead {i}',
            'method': 'update'
        }
        for i in range(num_leads)
    ]
    
    # Add 'Show All' button
    buttons.insert(0, {
        'args': [{'visible': [True] * num_leads},
                 {'height': 250 * num_leads, 'width': 1200}],  # Default size for all leads
        'label': 'Show All',
        'method': 'update'
    })

    # Update layout with dropdown menu
    fig.update_layout(
        title="Electrocardiogram (ECG)",
        height=600,  # Keep height constant
        width=1200,  # Adjusted width
        margin=dict(l=40, r=40, t=40, b=100),
        dragmode='zoom',
        updatemenus=[
            {
                'buttons': buttons,
                'direction': 'down',
                'showactive': True,
                'x': 0.9,  # Position of dropdown menu to the right side
                'xanchor': 'right',
                'y': 1.1,
                'yanchor': 'top'
            }
        ],
        hovermode='x unified'
    )

    fig.update_xaxes(
        title_text="Time (ms)",
        rangeslider=dict(
            visible=True,
            thickness=0.1,
            bgcolor='rgba(255,255,255,0.9)'
        ),
        row=num_leads, col=1
    )

    fig.update_traces(
        hoverinfo="x+y",
        selector=dict(mode='lines')
    )

    # Remove unwanted annotations
    fig.update_layout(
        annotations=[]
    )

    print("Displaying the figure...")
    fig.show(config={'scrollZoom': True})  # Enable scroll zoom

def select_file():
    print("Opening file dialog...")
    root = Tk()
    root.withdraw()
    filename = askopenfilename(title="Select ECG CSV file", filetypes=[("CSV files", "*.csv")])
    root.destroy()
    print(f"File selected: {filename}")
    return filename

if __name__ == "__main__":
    print("Starting the script...")
    csv_file = select_file()
    if csv_file:
        plot_ecg(csv_file)
    else:
        print("No file selected")
