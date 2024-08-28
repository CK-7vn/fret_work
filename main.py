import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel('FretCalculator.xlsx', header=1)

# Extract fret positions for each string
frets = df.iloc[:, 0].dropna()
frets = frets[frets != 'Open'].astype(int)  # Exclude 'Open' and convert to int
string_positions = df.iloc[:, [1, 4, 7, 10, 13, 16, 19]].dropna()

# Set up the plot
fig, ax = plt.subplots(figsize=(20, 10))  # Increased figure size

# Define string names
string_names = ['E4', 'B3', 'G3', 'D3', 'A2', 'E2', 'A1']

# Plot each string
for i, string_name in enumerate(string_names):
    y = 6 - i  # Reverse the order of strings
    x = string_positions.iloc[:, i]
    ax.plot(x, [y] * len(x), 'k-', linewidth=1)
    
    # Plot frets
    for fret, pos in zip(['Open'] + list(frets), x):
        ax.plot([pos, pos], [y-0.1, y+0.1], 'r-', linewidth=2)

# Set plot limits and labels
ax.set_xlim(24, 27.5)  # Adjusted to focus on the fretboard
ax.set_ylim(-1, 6.5)  # Increased bottom margin for fret numbers
ax.set_yticks(range(7))
ax.set_yticklabels(string_names)
ax.set_xlabel('Scale Length (inches)', fontsize=12)
ax.set_title('Guitar Fret Positions', fontsize=16)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add fret numbers
for fret, pos in zip(['Open'] + list(frets), string_positions.iloc[:, 0]):
    ax.text(pos, -0.5, str(fret), ha='center', va='top', rotation=90, fontsize=10)

# Adjust layout
plt.subplots_adjust(bottom=0.15, left=0.05, right=0.95, top=0.95)

plt.show()
