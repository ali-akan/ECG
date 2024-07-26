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
    max_leads_per_fig = 10
    num_figures = (num_leads + max_leads_per_fig - 1) // max_leads_per_fig

    for fig_num in range(num_figures):
        start_index = fig_num * max_leads_per_fig
        end_index = min(start_index + max_leads_per_fig, num_leads)
        num_rows = end_index - start_index

        # Calculate height dynamically based on the number of subplots
        subplot_height = 300  # Reduced subplot height for better fitting
        total_height = num_rows * subplot_height + 100  # Added buffer space for sliders

        # Create the subplot figure
        fig = make_subplots(
            rows=num_rows,
            cols=1,
            shared_xaxes=False,  # Disable shared x-axes
            vertical_spacing=0.05,
            subplot_titles=[f'Lead {i}' for i in range(start_index, end_index)]
        )

        for i in range(start_index, end_index):
            fig.add_trace(
                go.Scatter(x=time, y=voltages.iloc[:, i], mode='lines', name=f'Lead {i}'),
                row=i - start_index + 1, col=1
            )

            fig.update_xaxes(
                title_text="Time (ms)",
                row=i - start_index + 1, col=1,
                rangeselector=dict(
                    buttons=list([
                        dict(count=1, label="1s", step="second", stepmode="backward"),
                        dict(count=10, label="10s", step="second", stepmode="backward"),
                        dict(count=30, label="30s", step="second", stepmode="backward"),
                        dict(step="all")
                    ])
                ),
                rangeslider=dict(
                    visible=True,
                    thickness=0.05
                ),
                type="linear"
            )

            fig.update_yaxes(
                title_text="Voltage (mV)",
                row=i - start_index + 1, col=1,
                fixedrange=False,
                showline=True,
                linewidth=2,
                linecolor="Black"
            )

        # Update layout
        fig.update_layout(
            title=f"Electrocardiogram (ECG) - Part {fig_num + 1}",
            height=total_height,
            width=1400,
            margin=dict(l=60, r=60, t=60, b=60),
            dragmode='zoom',
            hovermode='x'
        )

        # Display figure
        print(f"Displaying figure {fig_num + 1}...")
        config = dict({'scrollZoom': True})
        fig.show(config=config)

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
