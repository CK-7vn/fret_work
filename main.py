import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('guitar_frets.xlsx')

df = df.sort_values(['string_number', 'fret_position'])

fig, ax = plt.subplots(figsize=(15, 6));

for string in range(1, 8):  
    string_data = df[df['string_number'] == string]
    
    # Plot the string
    ax.plot(string_data['scale_length'], [string] * len(string_data), color='black', linewidth=1)
    
    # Plot the frets
    ax.scatter(string_data['scale_length'], [string] * len(string_data), color='red', s=50)

# Customize the plot
ax.set_ylim(0.5, 7.5)
ax.set_xlim(0, df['scale_length'].max() * 1.05)
ax.set_yticks(range(1, 8))
ax.set_yticklabels(['String ' + str(i) for i in range(1, 8)])
ax.set_xlabel('Scale Length')
ax.set_title('Guitar Fret Positions')

# Add fret number labels
for fret in df['fret_position'].unique():
    fret_data = df[df['fret_position'] == fret]
    if not fret_data.empty:
        ax.text(fret_data['scale_length'].iloc[0], 0.5, str(int(fret)), 
                ha='center', va='bottom', fontsize=8, rotation=90)

# Invert y-axis to match guitar orientation
ax.invert_yaxis()

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Show the plot
plt.tight_layout()
plt.show()
