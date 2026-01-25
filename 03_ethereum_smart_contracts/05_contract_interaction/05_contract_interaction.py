#!/usr/bin/env python3
"""
Contract Interaction Comparison Chart
Comparison: Call (read, free) vs Transaction (write, costs gas)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon, Rectangle
import os

# Color palette
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLPURPLE = '#3333B2'

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Title
ax.text(5, 5.7, 'Smart Contract Interaction Methods',
        ha='center', va='top', fontsize=18, fontweight='bold')

# Subtitle
ax.text(5, 5.35, 'Call vs Transaction: When to Use Each',
        ha='center', va='center', fontsize=12, style='italic', color='#666666')

# Dividing line
ax.plot([5, 5], [0.8, 5.0], 'k--', linewidth=2, alpha=0.3, zorder=1)

# LEFT SIDE: CALL (Read)
call_x = 2.5
call_y_top = 4.5

# Call header
call_header = FancyBboxPatch((0.5, call_y_top), 4, 0.6,
                            boxstyle="round,pad=0.08",
                            edgecolor=MLBLUE, facecolor=MLBLUE,
                            linewidth=2, zorder=2)
ax.add_patch(call_header)
ax.text(call_x, call_y_top + 0.3, 'CALL (Read Operation)',
        ha='center', va='center', fontsize=14, fontweight='bold',
        color='white')

# Call icon
read_circle = Circle((1.2, call_y_top + 0.3), 0.18, color='white', zorder=3)
ax.add_patch(read_circle)
ax.text(1.2, call_y_top + 0.3, '📖', ha='center', va='center',
        fontsize=14, zorder=4)

# Call characteristics box
call_box = FancyBboxPatch((0.5, call_y_top - 3.2), 4, 3.0,
                         boxstyle="round,pad=0.08",
                         edgecolor=MLBLUE, facecolor='#E3F2FD',
                         linewidth=2, zorder=1)
ax.add_patch(call_box)

# Call characteristics
char_y = call_y_top - 0.5

characteristics_call = [
    ('Purpose', 'Read blockchain state', True),
    ('Cost', 'FREE (no gas)', True),
    ('Speed', 'Instant response', True),
    ('State Change', 'NO modifications', True),
    ('Returns', 'Data immediately', True),
    ('Broadcast', 'Local execution only', False),
    ('Confirmation', 'Not needed', False),
]

for i, (label, value, is_positive) in enumerate(characteristics_call):
    y_pos = char_y - i * 0.35

    # Label
    ax.text(0.8, y_pos, f'{label}:',
            ha='left', va='center', fontsize=9, fontweight='bold')

    # Value with color coding
    value_color = MLGREEN if is_positive else '#666666'
    ax.text(2.0, y_pos, value,
            ha='left', va='center', fontsize=9, color=value_color)

# Call function examples
examples_y = call_y_top - 2.9
ax.text(call_x, examples_y, 'Function Types:',
        ha='center', va='center', fontsize=10, fontweight='bold',
        color=MLBLUE)

# View function
view_box = FancyBboxPatch((0.7, examples_y - 0.45), 3.6, 0.3,
                         boxstyle="round,pad=0.04",
                         edgecolor=MLBLUE, facecolor='white',
                         linewidth=1.5, zorder=2)
ax.add_patch(view_box)
ax.text(call_x, examples_y - 0.3, 'function getBalance() public view returns (uint)',
        ha='center', va='center', fontsize=7, family='monospace')

# Pure function
pure_box = FancyBboxPatch((0.7, examples_y - 0.8), 3.6, 0.3,
                         boxstyle="round,pad=0.04",
                         edgecolor=MLGREEN, facecolor='white',
                         linewidth=1.5, zorder=2)
ax.add_patch(pure_box)
ax.text(call_x, examples_y - 0.65, 'function add(uint a, uint b) public pure returns (uint)',
        ha='center', va='center', fontsize=7, family='monospace')

# RIGHT SIDE: TRANSACTION (Write)
tx_x = 7.5
tx_y_top = 4.5

# Transaction header
tx_header = FancyBboxPatch((5.5, tx_y_top), 4, 0.6,
                          boxstyle="round,pad=0.08",
                          edgecolor=MLRED, facecolor=MLRED,
                          linewidth=2, zorder=2)
ax.add_patch(tx_header)
ax.text(tx_x, tx_y_top + 0.3, 'TRANSACTION (Write Operation)',
        ha='center', va='center', fontsize=14, fontweight='bold',
        color='white')

# Transaction icon
write_circle = Circle((8.8, tx_y_top + 0.3), 0.18, color='white', zorder=3)
ax.add_patch(write_circle)
ax.text(8.8, tx_y_top + 0.3, '✍', ha='center', va='center',
        fontsize=14, zorder=4)

# Transaction characteristics box
tx_box = FancyBboxPatch((5.5, tx_y_top - 3.2), 4, 3.0,
                       boxstyle="round,pad=0.08",
                       edgecolor=MLRED, facecolor='#FFEBEE',
                       linewidth=2, zorder=1)
ax.add_patch(tx_box)

# Transaction characteristics
characteristics_tx = [
    ('Purpose', 'Modify blockchain state', True),
    ('Cost', 'COSTS GAS', False),
    ('Speed', '~12 seconds (Ethereum)', False),
    ('State Change', 'YES - permanent', True),
    ('Returns', 'Transaction hash', False),
    ('Broadcast', 'Network-wide', True),
    ('Confirmation', 'Required (blocks)', False),
]

for i, (label, value, is_positive) in enumerate(characteristics_tx):
    y_pos = char_y - i * 0.35

    # Label
    ax.text(5.8, y_pos, f'{label}:',
            ha='left', va='center', fontsize=9, fontweight='bold')

    # Value with color coding
    value_color = MLGREEN if is_positive else MLRED
    if 'GAS' in value:
        value_color = MLRED
    elif 'seconds' in value:
        value_color = MLORANGE
    ax.text(7.0, y_pos, value,
            ha='left', va='center', fontsize=9, color=value_color)

# Transaction function examples
ax.text(tx_x, examples_y, 'Function Types:',
        ha='center', va='center', fontsize=10, fontweight='bold',
        color=MLRED)

# State-changing function
state_box = FancyBboxPatch((5.7, examples_y - 0.45), 3.6, 0.3,
                          boxstyle="round,pad=0.04",
                          edgecolor=MLRED, facecolor='white',
                          linewidth=1.5, zorder=2)
ax.add_patch(state_box)
ax.text(tx_x, examples_y - 0.3, 'function transfer(address to, uint amt) public',
        ha='center', va='center', fontsize=7, family='monospace')

# Payable function
payable_box = FancyBboxPatch((5.7, examples_y - 0.8), 3.6, 0.3,
                            boxstyle="round,pad=0.04",
                            edgecolor=MLORANGE, facecolor='white',
                            linewidth=1.5, zorder=2)
ax.add_patch(payable_box)
ax.text(tx_x, examples_y - 0.65, 'function deposit() public payable',
        ha='center', va='center', fontsize=7, family='monospace')

# Bottom comparison table
table_y = 0.6
table_height = 0.4

# Table header
header_box = FancyBboxPatch((0.5, table_y + table_height), 9, 0.25,
                           boxstyle="round,pad=0.02",
                           edgecolor='black', facecolor='#DDDDDD',
                           linewidth=2, zorder=1)
ax.add_patch(header_box)

ax.text(1.5, table_y + table_height + 0.125, 'Criterion',
        ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(4.0, table_y + table_height + 0.125, 'Call',
        ha='center', va='center', fontsize=9, fontweight='bold', color=MLBLUE)
ax.text(7.5, table_y + table_height + 0.125, 'Transaction',
        ha='center', va='center', fontsize=9, fontweight='bold', color=MLRED)

# Table rows
rows = [
    ('Gas Required?', 'No ✓', 'Yes (user pays)', MLGREEN, MLRED),
    ('Blockchain Change?', 'No ✓', 'Yes (permanent)', MLGREEN, MLORANGE),
    ('Wait Time?', 'Instant ✓', '~12 seconds', MLGREEN, MLORANGE),
]

row_height = 0.13
for i, (criterion, call_val, tx_val, call_color, tx_color) in enumerate(rows):
    y_pos = table_y + table_height - 0.05 - i * row_height

    # Background alternating
    if i % 2 == 0:
        row_bg = Rectangle((0.5, y_pos - row_height/2), 9, row_height,
                          facecolor='#F9F9F9', edgecolor='none', zorder=0)
        ax.add_patch(row_bg)

    ax.text(1.5, y_pos, criterion,
            ha='center', va='center', fontsize=8)
    ax.text(4.0, y_pos, call_val,
            ha='center', va='center', fontsize=8, color=call_color)
    ax.text(7.5, y_pos, tx_val,
            ha='center', va='center', fontsize=8, color=tx_color)

plt.tight_layout()

# Save
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, '05_contract_interaction.pdf')
plt.savefig(output_path, dpi=300, bbox_inches='tight', format='pdf')
print(f"Chart saved to: {output_path}")

plt.show()
