import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import config

# Define the list of experiments
experiments = ["2024-03-26-23_12_39", "2024-03-24-22_31_21", "2024-03-29-22_32_10"]
label_names = ["T1", "T2", "T3"]
colors = ['blue', 'green', 'red']  # Colors corresponding to each experiment

plt.rcParams.update({'font.size': 14})  # Update the font size for better readability

# Scaling factors for adjusting plot size
a = 0.9
b = 0.8
# Initialize the main figure
fig, ax1 = plt.subplots(figsize=(10 * a, 5 * b))
ax2 = ax1.twinx()  # Create a second y-axis that shares the x-axis

for idx, exp in enumerate(experiments):
    color = colors[idx]  # Select color for the current experiment
    basedir = "../Dataset/" + exp + "/"

    # Read the first CSV file
    csv_path = basedir +"HSB_"+ exp + '.csv'
    df1 = pd.read_csv(csv_path, encoding='utf8')
    df1['Datetime'] = pd.to_datetime(df1.iloc[:, 0], errors='coerce', format='%Y-%m-%d %H:%M:%S.%f')
    df1 = df1.dropna(subset=['Datetime'])  # Remove rows with NaN in the datetime conversion
    df1['Eb/No'] = df1.iloc[:, 4].astype(float)
    start_time_eb_no = df1['Datetime'].min()
    end_time_eb_no = df1['Datetime'].max()
    df1['TimeDelta'] = (df1['Datetime'] - start_time_eb_no).dt.total_seconds()

    # Read AGC data
    file_path = 'ACU_TY28_' + exp + '.mae'
    columns = [
        'Date', 'Time', 'Azimuth/Elevation Mode', 'Third Axis Mode', 'S Transmission Polarization', 
        'X Transmission Polarization', 'S Co-Polarization', 'S Cross-Polarization', 'X Cross-Polarization',
        'Earth Azimuth Angle', 'Earth Elevation Angle', 'Earth Azimuth Command', 'Earth Elevation Command',
        'Measurement Azimuth Angle', 'Measurement Elevation Angle', 'Measurement Third Axis Angle', 
        'Measurement Azimuth Command', 'Measurement Elevation Command', 'Measurement Third Axis Command',
        'Tracking Control Lock', 'Tracking Control AGC', 'Tracking Control Uaz', 'Tracking Control Uel',
        'Data Transmission Lock', 'Data Transmission AGC', 'Data Transmission Uaz', 'Data Transmission Uel',
        'Azimuth Speed', 'Elevation Speed', 'Third Axis Speed', 'Azimuth Current 1', 'Azimuth Current 2',
        'Elevation Current 1', 'Elevation Current 2', 'Third Axis Current 1', 'Third Axis Current 2',
        'Azimuth Speed Command', 'Elevation Speed Command', 'Third Axis Speed Command'
    ]
    df2 = pd.read_csv(basedir + file_path, sep=r',', header=None, names=columns, encoding='utf8')
    df2['Datetime'] = pd.to_datetime(df2['Date'] + ' ' + df2['Time'], errors='coerce', format='%Y-%m-%d %H:%M:%S')
    df2 = df2.dropna(subset=['Datetime'])
    df2['Data Transmission AGC'] = pd.to_numeric(df2['Data Transmission AGC'], errors='coerce')
    df2['TimeDelta'] = (df2['Datetime'] - start_time_eb_no).dt.total_seconds()

    # Filter AGC data based on the time range of Eb/No
    df2_filtered = df2[(df2['Datetime'] >= start_time_eb_no) & (df2['Datetime'] <= end_time_eb_no)]

    # Plot Eb/No and AGC data
    ax1.plot(df1['TimeDelta'], df1['Eb/No'], label=f'Eb/N0 {label_names[idx]}', color=color, linestyle='-')
    print(df2_filtered['Data Transmission AGC'])
    ax2.plot(df2_filtered['TimeDelta'], df2_filtered['Data Transmission AGC'], label=f'AGC {label_names[idx]}', color=color, linestyle='--')

# Get legends for both axes
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()

# Combine and create a unified legend
ax1.legend(handles1 + handles2, labels1 + labels2, loc='upper right', ncol=1, frameon=False, bbox_to_anchor=(1.02, 1))

# Set titles and labels for axes
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Eb/N0 (dB)')
ax2.set_ylabel('AGC (dB)')
ax2.set_ylim(0, 7)  # Adjust the y-axis limit for AGC

ax1.set_xlim(0, 690)
ax2.set_xlim(0, 690)

fig.tight_layout()  # Optimize layout

outputdir = '.'
plt.savefig(outputdir + "/figure2.pdf", dpi=1000)  # Save the figure as a PDF
plt.show()  # Display the plot
