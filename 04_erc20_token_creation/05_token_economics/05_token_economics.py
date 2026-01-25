import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Wedge
import numpy as np
import os

# Color palette
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLPURPLE = '#3333B2'

# Create figure with 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 6))

# Main title
fig.suptitle('Token Supply Models', fontsize=18, fontweight='bold', color=MLBLUE, y=0.98)

# Model 1: Fixed Supply
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')

ax1.text(5, 9, 'Fixed Supply', ha='center', va='center',
         fontsize=14, fontweight='bold', color=MLGREEN)

# Timeline visualization
timeline_y = 7
ax1.plot([2, 8], [timeline_y, timeline_y], color='gray', linewidth=2)

# Markers at different times
times = [2, 5, 8]
labels = ['Deploy', 'Year 1', 'Year 5']
for time, label in zip(times, labels):
    ax1.plot(time, timeline_y, 'o', markersize=10, color=MLGREEN)
    ax1.text(time, timeline_y - 0.5, label, ha='center', va='top',
             fontsize=8, color='gray')

# Supply box at each time
supply_y = 5.5
for time in times:
    supply_box = FancyBboxPatch((time - 0.6, supply_y - 0.3), 1.2, 0.6,
                                boxstyle="round,pad=0.05",
                                edgecolor=MLGREEN, facecolor=MLGREEN,
                                linewidth=2, alpha=0.5)
    ax1.add_patch(supply_box)
    ax1.text(time, supply_y, '1M', ha='center', va='center',
             fontsize=10, fontweight='bold', color='white')

# Horizontal line showing constant supply
ax1.plot([2, 8], [supply_y, supply_y], color=MLGREEN, linewidth=2, linestyle='--', alpha=0.5)

# Characteristics
char_y = 3.5
characteristics = [
    '• Total supply fixed at creation',
    '• No new tokens can be minted',
    '• Predictable scarcity',
    '• Example: Bitcoin (21M cap)'
]

for i, char in enumerate(characteristics):
    ax1.text(5, char_y - i * 0.6, char, ha='center', va='center',
             fontsize=7, color='black')

# Benefits box
benefit_box = FancyBboxPatch((1, 0.5), 8, 0.8,
                             boxstyle="round,pad=0.1",
                             edgecolor=MLGREEN, facecolor='white',
                             linewidth=1.5)
ax1.add_patch(benefit_box)
ax1.text(5, 0.9, 'Anti-inflationary, value preservation',
         ha='center', va='center', fontsize=7, color=MLGREEN,
         fontweight='bold', style='italic')

# Model 2: Inflationary Supply
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')

ax2.text(5, 9, 'Inflationary Supply', ha='center', va='center',
         fontsize=14, fontweight='bold', color=MLORANGE)

# Timeline
timeline_y = 7
ax2.plot([2, 8], [timeline_y, timeline_y], color='gray', linewidth=2)

times = [2, 5, 8]
labels = ['Deploy', 'Year 1', 'Year 5']
for time, label in zip(times, labels):
    ax2.plot(time, timeline_y, 'o', markersize=10, color=MLORANGE)
    ax2.text(time, timeline_y - 0.5, label, ha='center', va='top',
             fontsize=8, color='gray')

# Increasing supply
supply_values = [1.0, 1.5, 2.5]
supply_y_base = 5.5

for time, supply_val in zip(times, supply_values):
    box_height = supply_val * 0.4
    supply_box = FancyBboxPatch((time - 0.6, supply_y_base - box_height/2), 1.2, box_height,
                                boxstyle="round,pad=0.05",
                                edgecolor=MLORANGE, facecolor=MLORANGE,
                                linewidth=2, alpha=0.5)
    ax2.add_patch(supply_box)
    ax2.text(time, supply_y_base, f'{supply_val:.1f}M', ha='center', va='center',
             fontsize=9, fontweight='bold', color='white')

# Growth curve
supply_curve_x = np.linspace(2, 8, 50)
supply_curve_y = 5.5 + 0.3 * (supply_curve_x - 2) * 0.5
ax2.plot(supply_curve_x, supply_curve_y, color=MLORANGE, linewidth=2, linestyle='--', alpha=0.5)

# Characteristics
char_y = 3.5
characteristics = [
    '• New tokens minted over time',
    '• Rewards for staking/mining',
    '• Controlled inflation rate',
    '• Example: Ethereum (post-merge)'
]

for i, char in enumerate(characteristics):
    ax2.text(5, char_y - i * 0.6, char, ha='center', va='center',
             fontsize=7, color='black')

# Benefits box
benefit_box = FancyBboxPatch((1, 0.5), 8, 0.8,
                             boxstyle="round,pad=0.1",
                             edgecolor=MLORANGE, facecolor='white',
                             linewidth=1.5)
ax2.add_patch(benefit_box)
ax2.text(5, 0.9, 'Incentivizes participation, network growth',
         ha='center', va='center', fontsize=7, color=MLORANGE,
         fontweight='bold', style='italic')

# Model 3: Deflationary Supply
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 10)
ax3.axis('off')

ax3.text(5, 9, 'Deflationary Supply', ha='center', va='center',
         fontsize=14, fontweight='bold', color=MLRED)

# Timeline
timeline_y = 7
ax3.plot([2, 8], [timeline_y, timeline_y], color='gray', linewidth=2)

times = [2, 5, 8]
labels = ['Deploy', 'Year 1', 'Year 5']
for time, label in zip(times, labels):
    ax3.plot(time, timeline_y, 'o', markersize=10, color=MLRED)
    ax3.text(time, timeline_y - 0.5, label, ha='center', va='top',
             fontsize=8, color='gray')

# Decreasing supply
supply_values = [1.0, 0.8, 0.5]
supply_y_base = 5.5

for time, supply_val in zip(times, supply_values):
    box_height = supply_val * 0.6
    supply_box = FancyBboxPatch((time - 0.6, supply_y_base - box_height/2), 1.2, box_height,
                                boxstyle="round,pad=0.05",
                                edgecolor=MLRED, facecolor=MLRED,
                                linewidth=2, alpha=0.5)
    ax3.add_patch(supply_box)
    ax3.text(time, supply_y_base, f'{supply_val:.1f}M', ha='center', va='center',
             fontsize=9, fontweight='bold', color='white')

# Decline curve
supply_curve_x = np.linspace(2, 8, 50)
supply_curve_y = 5.5 - 0.15 * (supply_curve_x - 2) * 0.5
ax3.plot(supply_curve_x, supply_curve_y, color=MLRED, linewidth=2, linestyle='--', alpha=0.5)

# Fire icon for burn
ax3.text(8.5, 4.8, '🔥', ha='center', va='center', fontsize=16)

# Characteristics
char_y = 3.5
characteristics = [
    '• Tokens burned/destroyed',
    '• Transaction fee burns',
    '• Buyback and burn programs',
    '• Example: BNB (quarterly burns)'
]

for i, char in enumerate(characteristics):
    ax3.text(5, char_y - i * 0.6, char, ha='center', va='center',
             fontsize=7, color='black')

# Benefits box
benefit_box = FancyBboxPatch((1, 0.5), 8, 0.8,
                             boxstyle="round,pad=0.1",
                             edgecolor=MLRED, facecolor='white',
                             linewidth=1.5)
ax3.add_patch(benefit_box)
ax3.text(5, 0.9, 'Increases scarcity, potential price appreciation',
         ha='center', va='center', fontsize=7, color=MLRED,
         fontweight='bold', style='italic')

plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, '05_token_economics.pdf')
plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
plt.close()
