import pandas as pd
import plotly.graph_objects as go
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

    print("Plotting ECG data...")
    fig = go.Figure()

    for col in voltages.columns:
        fig.add_trace(go.Scatter(x=time, y=voltages[col], mode='lines', name=f'Lead {col}'))

    fig.update_layout(
        title="Electrocardiogram (ECG)",
        xaxis_title="Time (ms)",
        yaxis_title="Voltage (mV)",
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1s", step="second", stepmode="backward"),
                    dict(count=10, label="10s", step="second", stepmode="backward"),
                    dict(count=30, label="30s", step="second", stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(visible=True),
            type="linear"
        ),
        yaxis=dict(fixedrange=False)
    )

    fig.update_layout(dragmode='zoom', hovermode='x')

    print("Displaying the plot...")
    fig.show()

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
