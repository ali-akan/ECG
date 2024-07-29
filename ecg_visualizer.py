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

    # Create a subplot figure with stacked plots
    fig = make_subplots(
        rows=num_leads, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03
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

    # Create buttons for focusing on each channel
    buttons = []
    for i in range(num_leads):
        button = {
            'label': f'Lead {i}',
            'method': 'update',
            'args': [
                {'visible': [j == i for j in range(num_leads)]},
                {'height': [600 if j == i else 150 for j in range(num_leads)]}
            ]
        }
        buttons.append(button)

    # Add reset button to show all channels
    buttons.append({
        'label': 'Show All',
        'method': 'update',
        'args': [
            {'visible': [True] * num_leads},
            {'height': [600] * num_leads}
        ]
    })

    # Update layout
    fig.update_layout(
        title="Electrocardiogram (ECG)",
        height=600,  # Default height
        width=1400,  # Adjusted width
        margin=dict(l=40, r=40, t=40, b=0),
        dragmode='zoom',
        hovermode='x unified',
        updatemenus=[
            {
                'buttons': buttons,
                'direction': 'down',
                'showactive': True,
                'x': 1.01,
                'xanchor': 'left',
                'y': 0.66,
                'yanchor': 'top'
            }
        ]
    )

    # Debugging: Print button configurations
    # print("Buttons configuration:")
    # for button in buttons:
    #     print(button)

    fig.update_xaxes(
        title_text="Time (ms)",
        rangeslider=dict(
            visible=True,
            thickness=0.1,
            # bgcolor='rgba(0,0,255,0.9)'  # Make slider background white
        ),
        row=num_leads, col=1
    )

    # Update X-axes for each subplot
    for i in range(num_leads):
        if i == num_leads - 1:
            fig.update_xaxes(
                showticklabels=True,  # Show X-axis labels on the last subplot
                row=i+1, col=1
            )
        else:
            fig.update_xaxes(
                showticklabels=False,  # Hide X-axis labels on other subplots
                row=i+1, col=1
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
    