import re
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import config
import pandas as pd
import csv
from matplotlib.ticker import ScalarFormatter

# Configuration for experiment
exp = "2024-03-29-22_32_10"  # Experiment identifier from config
basedir = "../Dataset/" + exp + "/"

# Update default settings for plot font sizes
plt.rcParams.update({'font.size': 14})
# Define a color palette for visual clarity
colors = {'Error': '#800000', 'Lost': '#003366', 'Received': '#004d00'}

# Scaling factors for adjusting plot size
a = 0.9
b = 0.8
# Initialize the main figure
fig, ax1 = plt.subplots(figsize=(10 * a, 3 * b * 1.4))

# Additional axes setup
ax2 = ax1.twinx()  # Duplicate axis for second set of data
ax3 = ax1  # Duplicate axis for third set of data
ax4 = ax1.twinx()  # Duplicate axis for fourth set of data
ax4.spines['right'].set_position(('outward', 45))

# Load and plot additional data
csv_path = basedir + "HSB_"+ exp + '.csv'
df_csv = pd.read_csv(csv_path, encoding='utf8')
df_csv['Datetime'] = pd.to_datetime(df_csv.iloc[:, 0], format='%Y-%m-%d %H:%M:%S.%f')
df_csv['Seconds'] = (df_csv['Datetime'] - df_csv['Datetime'].min()).dt.total_seconds()


# Plot data on respective axes
ax2.plot(df_csv['Seconds'], df_csv.iloc[:, 24], label='Error', color=colors['Error'], linestyle='--')
ax2.set_ylim(0, max(df_csv.iloc[:, 24].dropna()) * 1.5)
ax2.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax2.tick_params(axis='y', colors=colors['Error'])
ax2.get_yaxis().get_offset_text().set_x(1.04)  
ax2.get_yaxis().get_offset_text().set_y(1.1)  


ax3.plot(df_csv['Seconds'], df_csv.iloc[:, 25], label='Lost', color=colors['Lost'], linestyle='-.')
ax3.set_ylim(0, max(df_csv.iloc[:, 25].dropna()) * 2.5)
ax3.tick_params(axis='y', colors=colors['Lost'])

ax4.plot(df_csv['Seconds'], df_csv.iloc[:, 23], label='Received', color=colors['Received'], linestyle=':')
ax4.set_ylim(0, max(df_csv.iloc[:, 23].dropna()) * 1.1)
ax4.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax4.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax4.tick_params(axis='y', colors=colors['Received'])
ax4.get_yaxis().get_offset_text().set_x(1.16)
ax4.get_yaxis().get_offset_text().set_y(1.1)


ax1.set_xlabel('Time (s)')

# Gather labels for legend
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
lines4, labels4 = ax4.get_legend_handles_labels()

# Configure legend
ax1.legend(lines2 + lines3 + lines4, labels2 + labels3 + labels4, loc='upper center', ncol=3, frameon=False, bbox_to_anchor=(0.46, 1.2), fontsize=15)

fig.tight_layout()

# Save and display the plot
outputdir = '.'
plt.savefig(outputdir + "/figure4.pdf", dpi=1000)
plt.show()
