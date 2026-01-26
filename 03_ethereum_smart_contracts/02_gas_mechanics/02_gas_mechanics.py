#!/usr/bin/env python3
"""
Gas Mechanics Chart
Visual formula: Gas Fee = Gas Used × Gas Price, with example
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
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
ax.text(5, 5.7, 'Gas Mechanics: Transaction Cost Model',
        ha='center', va='top', fontsize=18, fontweight='bold')

# Main Formula Section
formula_y = 4.5
ax.text(5, formula_y, 'Gas Fee  =  Gas Used  ×  Gas Price',
        ha='center', va='center', fontsize=20, fontweight='bold',
        family='monospace', color=MLBLUE)

# Components breakdown
breakdown_y = 3.6

# Gas Used box
gas_used_box = FancyBboxPatch((0.8, breakdown_y), 2.5, 1.2,
                             boxstyle="round,pad=0.08",
                             edgecolor=MLGREEN, facecolor='#E8F5E9',
                             linewidth=2.5, zorder=2)
ax.add_patch(gas_used_box)
ax.text(2.05, breakdown_y+1.0, 'Gas Used', ha='center', va='center',
        fontsize=13, fontweight='bold', color=MLGREEN)
ax.text(2.05, breakdown_y+0.7, '(Computational Work)', ha='center', va='center',
        fontsize=9, style='italic')
ax.text(2.05, breakdown_y+0.45, 'Operations:', ha='center', va='center',
        fontsize=9, fontweight='bold')
ax.text(2.05, breakdown_y+0.25, '• SSTORE: 20,000', ha='left', va='center',
        fontsize=8, family='monospace')
ax.text(2.05, breakdown_y+0.1, '• SLOAD: 800', ha='left', va='center',
        fontsize=8, family='monospace')
ax.text(2.05, breakdown_y-0.05, '• ADD: 3', ha='left', va='center',
        fontsize=8, family='monospace')

# Multiplication symbol
ax.text(3.6, breakdown_y+0.6, '×', ha='center', va='center',
        fontsize=28, fontweight='bold', color=MLBLUE)

# Gas Price box
gas_price_box = FancyBboxPatch((4.1, breakdown_y), 2.5, 1.2,
                              boxstyle="round,pad=0.08",
                              edgecolor=MLORANGE, facecolor='#FFF3E0',
                              linewidth=2.5, zorder=2)
ax.add_patch(gas_price_box)
ax.text(5.35, breakdown_y+1.0, 'Gas Price', ha='center', va='center',
        fontsize=13, fontweight='bold', color=MLORANGE)
ax.text(5.35, breakdown_y+0.7, '(Market Rate)', ha='center', va='center',
        fontsize=9, style='italic')
ax.text(5.35, breakdown_y+0.45, 'User Sets:', ha='center', va='center',
        fontsize=9, fontweight='bold')
ax.text(5.35, breakdown_y+0.2, 'Gwei per gas unit', ha='center', va='center',
        fontsize=8)
ax.text(5.35, breakdown_y, 'Higher = Faster', ha='center', va='center',
        fontsize=8, color=MLRED, fontweight='bold')

# Equals symbol
ax.text(6.9, breakdown_y+0.6, '=', ha='center', va='center',
        fontsize=28, fontweight='bold', color=MLBLUE)

# Total Fee box
total_box = FancyBboxPatch((7.4, breakdown_y), 2.0, 1.2,
                          boxstyle="round,pad=0.08",
                          edgecolor=MLBLUE, facecolor='#E3F2FD',
                          linewidth=2.5, zorder=2)
ax.add_patch(total_box)
ax.text(8.4, breakdown_y+1.0, 'Total Fee', ha='center', va='center',
        fontsize=13, fontweight='bold', color=MLBLUE)
ax.text(8.4, breakdown_y+0.7, '(ETH)', ha='center', va='center',
        fontsize=9, style='italic')
ax.text(8.4, breakdown_y+0.4, 'Paid to Miners/', ha='center', va='center',
        fontsize=8)
ax.text(8.4, breakdown_y+0.2, 'Validators', ha='center', va='center',
        fontsize=8)
ax.text(8.4, breakdown_y, 'Burned (EIP-1559)', ha='center', va='center',
        fontsize=7, style='italic')

# Example Calculation Section
example_y = 2.0

# Example title
ax.text(5, example_y+0.8, 'Example: Simple Token Transfer',
        ha='center', va='center', fontsize=14, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#F5F5F5', edgecolor='black', linewidth=1.5))

# Example calculation boxes
calc_box = FancyBboxPatch((1.5, example_y-0.7), 7, 1.3,
                         boxstyle="round,pad=0.08",
                         edgecolor='#666666', facecolor='white',
                         linewidth=2, zorder=1)
ax.add_patch(calc_box)

# Step-by-step calculation
calc_text_y = example_y+0.3
ax.text(2.5, calc_text_y, 'Gas Used:', ha='right', va='center',
        fontsize=11, fontweight='bold')
ax.text(2.7, calc_text_y, '21,000 gas', ha='left', va='center',
        fontsize=11, family='monospace', color=MLGREEN)

ax.text(2.5, calc_text_y-0.3, 'Gas Price:', ha='right', va='center',
        fontsize=11, fontweight='bold')
ax.text(2.7, calc_text_y-0.3, '50 Gwei', ha='left', va='center',
        fontsize=11, family='monospace', color=MLORANGE)

# Arrow to result
arrow = FancyArrowPatch((4.2, calc_text_y-0.15), (5.3, calc_text_y-0.15),
                       arrowstyle='->', mutation_scale=25,
                       linewidth=2.5, color=MLBLUE)
ax.add_artist(arrow)

# Result
result_box = FancyBboxPatch((5.5, calc_text_y-0.45), 2.8, 0.6,
                           boxstyle="round,pad=0.08",
                           edgecolor=MLBLUE, facecolor='#E3F2FD',
                           linewidth=2.5, zorder=3)
ax.add_patch(result_box)
ax.text(6.9, calc_text_y-0.15, '0.00105 ETH', ha='center', va='center',
        fontsize=14, fontweight='bold', family='monospace', color=MLBLUE)

# Conversion to USD (example)
ax.text(6.9, calc_text_y-0.55, '≈ $2.10 (@ $2,000/ETH)', ha='center', va='center',
        fontsize=9, style='italic', color='#666666')

# Gas Limit explanation
gas_limit_y = 0.3
limit_box = FancyBboxPatch((0.5, gas_limit_y-0.5), 4.2, 0.8,
                          boxstyle="round,pad=0.06",
                          edgecolor=MLRED, facecolor='#FFEBEE',
                          linewidth=2, zorder=1)
ax.add_patch(limit_box)
ax.text(2.6, gas_limit_y+0.1, 'Gas Limit (Safety Cap)', ha='center', va='center',
        fontsize=11, fontweight='bold', color=MLRED)
ax.text(2.6, gas_limit_y-0.15, 'Maximum gas willing to spend', ha='center', va='center',
        fontsize=8)
ax.text(2.6, gas_limit_y-0.3, 'Unused gas is refunded', ha='center', va='center',
        fontsize=8, style='italic')

# EIP-1559 note
eip_box = FancyBboxPatch((5.3, gas_limit_y-0.5), 4.2, 0.8,
                        boxstyle="round,pad=0.06",
                        edgecolor=MLPURPLE, facecolor='#F3E5F5',
                        linewidth=2, zorder=1)
ax.add_patch(eip_box)
ax.text(7.4, gas_limit_y+0.1, 'EIP-1559 (Post-London)', ha='center', va='center',
        fontsize=11, fontweight='bold', color=MLPURPLE)
ax.text(7.4, gas_limit_y-0.15, 'Base Fee (burned) + Priority Tip', ha='center', va='center',
        fontsize=8)
ax.text(7.4, gas_limit_y-0.3, 'More predictable fees', ha='center', va='center',
        fontsize=8, style='italic')

plt.tight_layout()

# Save
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, '02_gas_mechanics.pdf')
plt.savefig(output_path, dpi=300, bbox_inches='tight', format='pdf')
print(f"Chart saved to: {output_path}")

# Add PNG export for GitHub Pages
output_png = output_path.replace('.pdf', '.png')
plt.savefig(output_png, dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none', format='png')
print(f"PNG saved to: {output_png}")

# plt.show()
