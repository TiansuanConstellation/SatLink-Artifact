import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import re
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

# Update default settings for plot font size
plt.rcParams.update({'font.size': 15})

def get_throughPut(content, delta=1):
    # Extract timestamps and data lengths from content
    times_values = re.findall(r'\[(.*?)\]:', content)
    data_lens = re.findall(r': \[(.*?)\]', content)

    # Assert to ensure matched lengths of times and data
    assert len(times_values) == len(data_lens)

    # Convert string timestamps to datetime objects
    times_values = [datetime.strptime(t, '%Y-%m-%d %H:%M:%S.%f') for t in times_values]

    count_values = []
    count_sum = 0
    pre_time = times_values[0]
    time_labels = []

    # Calculate throughput over time intervals defined by 'delta'
    for i in range(len(times_values)):
        time = times_values[i]
        if (time - pre_time).total_seconds() >= delta:
            count_values.append(count_sum * 8 / delta / 1000000)  # Convert to Mbps
            time_labels.append(pre_time)
            pre_time = time
            count_sum = int(data_lens[i])
        else:
            count_sum += int(data_lens[i])

    # Append the last computed throughput
    count_values.append(count_sum * 8 / delta / 1000000)
    time_labels.append(pre_time)

    return count_values, time_labels

def plot_throughput(ax, experiments, colors, labels):
    for idx, exp in enumerate(experiments):
        basedir = "../Dataset/" + exp + "/"
        filepath = basedir + 'logfile_[TcpOriLenData]_' + exp + '.txt'
        
        with open(filepath, 'r') as file:
            content = file.read()
        
        throughput, time_labels = get_throughPut(content)

        # Convert time_labels to time deltas from the start for plotting
        start_time = min(time_labels)
        time_deltas = [(t - start_time).total_seconds() for t in time_labels]
        
        # Smooth the data using exponential weighted mean
        df = pd.DataFrame({'Time': time_deltas, 'Throughput': throughput})
        df['Smoothed'] = df['Throughput'].ewm(span=10, adjust=False).mean()

        # Plotting the smoothed throughput data
        ax.plot(df['Time'], df['Smoothed'], label=f'{labels[idx]}', color=colors[idx], linestyle='-', linewidth=0.5)

    # Set plot labels and legends
    ax.set_ylabel('Rate (Mbps)', fontsize=14)
    ax.legend(bbox_to_anchor=(1,0.1), loc='lower right', ncol=1, fontsize=15, frameon=False)
    ax.set_xlabel('Time (s)')
    ax.set_ylim(0, 60)
    
    # Adjust layout and save the plot
    fig.tight_layout()
    outputdir = '.'
    plt.savefig(outputdir + "/figure3.pdf", dpi=1000)
    plt.show()

# Scaling factors for adjusting plot size
a = 0.9
b = 0.8
# Initialize the main figure
fig, ax1 = plt.subplots(figsize=(10*a, 3*b*1.2))
experiments = ["2024-03-26-23_12_39", "2024-03-24-22_31_21", "2024-03-29-22_32_10"]
labels = ["T1", "T2", "T3"]
colors = ['blue', 'green', 'red']  # Colors corresponding to each experiment
plot_throughput(ax1, experiments, colors, labels)
