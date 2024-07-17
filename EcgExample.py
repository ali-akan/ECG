import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import RangeSlider
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def plot_ecg(csv_file):
    print("Loading CSV file...")
    data = pd.read_csv(csv_file, header=None)
    print("CSV file loaded successfully.")

    if data.shape[1] > 1 and data[0].dtype in [float, int]:
        time = data[0]
        voltages = data.iloc[:, 1:]
    else:
        time = pd.Series(range(len(data))) / 1000.0
        voltages = data

    print("Plotting ECG data...")
    
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)
    for col in voltages.columns:
        ax.plot(time, voltages[col], label=f'Lead {col}')
    
    ax.set_title("Electrocardiogram (ECG)")
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Voltage (mV)")
    ax.legend()

    # Create double range slider
    axcolor = 'lightgoldenrodyellow'
    ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
    time_slider = RangeSlider(ax_slider, 'Time', time.min(), time.max(), valinit=(time.min(), time.max()))

    # Update function for slider
    def update(val):
        ax.set_xlim([time_slider.val[0], time_slider.val[1]])
        fig.canvas.draw_idle()

    time_slider.on_changed(update)

    print("Displaying the plot...")
    plt.show()

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
