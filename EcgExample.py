import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
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
    fig, ax = plt.subplots(figsize=(10, 6)) 

    for col in voltages.columns:
        ax.plot(time, voltages[col], label=f'Lead {col}')

    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Voltage (mV)')
    ax.set_title('Electrocardiogram (ECG)')

    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    ax.axhline(y=0, color='black', linewidth=1)

    mplcursors.cursor(hover=True)

    def zoom(event):
        if event.button == 'up':
            scale_factor = 0.9
        elif event.button == 'down':
            scale_factor = 1.1
        else:
            return

        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()

        x_range = (cur_xlim[1] - cur_xlim[0]) * scale_factor
        y_range = (cur_ylim[1] - cur_ylim[0]) * scale_factor

        new_xlim = [cur_xlim[0] + (cur_xlim[1] - cur_xlim[0]) * (1 - scale_factor) / 2,
                    cur_xlim[1] - (cur_xlim[1] - cur_xlim[0]) * (1 - scale_factor) / 2]
        new_ylim = [cur_ylim[0] + (cur_ylim[1] - cur_ylim[0]) * (1 - scale_factor) / 2,
                    cur_ylim[1] - (cur_ylim[1] - cur_ylim[0]) * (1 - scale_factor) / 2]

        ax.set_xlim(new_xlim)
        ax.set_ylim(new_ylim)
        plt.draw()

    fig.canvas.mpl_connect('scroll_event', zoom)

    print("Displaying the plot...")
    plt.tight_layout()
    plt.legend()
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
