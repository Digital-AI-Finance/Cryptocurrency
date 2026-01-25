#!/usr/bin/env python3
"""
Smart Contract Lifecycle Chart
Flow: Write (Solidity) → Compile (bytecode) → Deploy → Interact
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
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
ax.text(5, 5.7, 'Smart Contract Lifecycle',
        ha='center', va='top', fontsize=18, fontweight='bold')

# Stage positions
stage_y = 3.5
stage_height = 2.0
stage_width = 2.0
spacing = 0.2

stages = [
    {'x': 0.5, 'title': '1. Write', 'color': MLBLUE, 'bgcolor': '#E3F2FD'},
    {'x': 2.7, 'title': '2. Compile', 'color': MLORANGE, 'bgcolor': '#FFF3E0'},
    {'x': 4.9, 'title': '3. Deploy', 'color': MLGREEN, 'bgcolor': '#E8F5E9'},
    {'x': 7.1, 'title': '4. Interact', 'color': MLPURPLE, 'bgcolor': '#F3E5F5'}
]

# Stage 1: Write Solidity
stage = stages[0]
box1 = FancyBboxPatch((stage['x'], stage_y), stage_width, stage_height,
                      boxstyle="round,pad=0.08",
                      edgecolor=stage['color'], facecolor=stage['bgcolor'],
                      linewidth=3, zorder=2)
ax.add_patch(box1)

# Stage number circle
circle1 = Circle((stage['x']+0.3, stage_y+stage_height-0.3), 0.18,
                color=stage['color'], zorder=3)
ax.add_patch(circle1)
ax.text(stage['x']+0.3, stage_y+stage_height-0.3, '1', ha='center', va='center',
        fontsize=12, fontweight='bold', color='white', zorder=4)

ax.text(stage['x']+stage_width/2, stage_y+stage_height-0.35, 'Write',
        ha='center', va='top', fontsize=13, fontweight='bold', color=stage['color'])
ax.text(stage['x']+stage_width/2, stage_y+1.25, 'Solidity Code',
        ha='center', va='center', fontsize=10, fontweight='bold')

# Code snippet
code_text = ('contract Token {\n'
             '  uint balance;\n'
             '  function send(\n'
             '    address to,\n'
             '    uint amt\n'
             '  ) {...}\n'
             '}')
ax.text(stage['x']+stage_width/2, stage_y+0.5, code_text,
        ha='center', va='center', fontsize=7, family='monospace',
        linespacing=1.3, bbox=dict(boxstyle='round,pad=0.3',
        facecolor='white', edgecolor=stage['color'], linewidth=1))

# Arrow to Stage 2
arrow1 = FancyArrowPatch((stage['x']+stage_width, stage_y+stage_height/2),
                        (stages[1]['x'], stage_y+stage_height/2),
                        arrowstyle='->', mutation_scale=25,
                        linewidth=3, color='#666666', zorder=1)
ax.add_artist(arrow1)
ax.text((stage['x']+stage_width+stages[1]['x'])/2, stage_y+stage_height/2+0.25,
        'solc', ha='center', va='bottom', fontsize=8, style='italic',
        color='#666666')

# Stage 2: Compile
stage = stages[1]
box2 = FancyBboxPatch((stage['x'], stage_y), stage_width, stage_height,
                      boxstyle="round,pad=0.08",
                      edgecolor=stage['color'], facecolor=stage['bgcolor'],
                      linewidth=3, zorder=2)
ax.add_patch(box2)

circle2 = Circle((stage['x']+0.3, stage_y+stage_height-0.3), 0.18,
                color=stage['color'], zorder=3)
ax.add_patch(circle2)
ax.text(stage['x']+0.3, stage_y+stage_height-0.3, '2', ha='center', va='center',
        fontsize=12, fontweight='bold', color='white', zorder=4)

ax.text(stage['x']+stage_width/2, stage_y+stage_height-0.35, 'Compile',
        ha='center', va='top', fontsize=13, fontweight='bold', color=stage['color'])

ax.text(stage['x']+stage_width/2, stage_y+1.3, 'Output:',
        ha='center', va='center', fontsize=9, fontweight='bold')

# Bytecode
bytecode_box = FancyBboxPatch((stage['x']+0.2, stage_y+0.65), stage_width-0.4, 0.4,
                              boxstyle="round,pad=0.05",
                              edgecolor=stage['color'], facecolor='white',
                              linewidth=1.5, zorder=3)
ax.add_patch(bytecode_box)
ax.text(stage['x']+stage_width/2, stage_y+0.95, 'Bytecode',
        ha='center', va='center', fontsize=8, fontweight='bold')
ax.text(stage['x']+stage_width/2, stage_y+0.78, '0x60806040...',
        ha='center', va='center', fontsize=7, family='monospace')

# ABI
abi_box = FancyBboxPatch((stage['x']+0.2, stage_y+0.15), stage_width-0.4, 0.4,
                        boxstyle="round,pad=0.05",
                        edgecolor=stage['color'], facecolor='white',
                        linewidth=1.5, zorder=3)
ax.add_patch(abi_box)
ax.text(stage['x']+stage_width/2, stage_y+0.45, 'ABI',
        ha='center', va='center', fontsize=8, fontweight='bold')
ax.text(stage['x']+stage_width/2, stage_y+0.28, 'Interface JSON',
        ha='center', va='center', fontsize=7, style='italic')

# Arrow to Stage 3
arrow2 = FancyArrowPatch((stage['x']+stage_width, stage_y+stage_height/2),
                        (stages[2]['x'], stage_y+stage_height/2),
                        arrowstyle='->', mutation_scale=25,
                        linewidth=3, color='#666666', zorder=1)
ax.add_artist(arrow2)
ax.text((stage['x']+stage_width+stages[2]['x'])/2, stage_y+stage_height/2+0.25,
        'tx', ha='center', va='bottom', fontsize=8, style='italic',
        color='#666666')

# Stage 3: Deploy
stage = stages[2]
box3 = FancyBboxPatch((stage['x'], stage_y), stage_width, stage_height,
                      boxstyle="round,pad=0.08",
                      edgecolor=stage['color'], facecolor=stage['bgcolor'],
                      linewidth=3, zorder=2)
ax.add_patch(box3)

circle3 = Circle((stage['x']+0.3, stage_y+stage_height-0.3), 0.18,
                color=stage['color'], zorder=3)
ax.add_patch(circle3)
ax.text(stage['x']+0.3, stage_y+stage_height-0.3, '3', ha='center', va='center',
        fontsize=12, fontweight='bold', color='white', zorder=4)

ax.text(stage['x']+stage_width/2, stage_y+stage_height-0.35, 'Deploy',
        ha='center', va='top', fontsize=13, fontweight='bold', color=stage['color'])

ax.text(stage['x']+stage_width/2, stage_y+1.35, 'Transaction',
        ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(stage['x']+stage_width/2, stage_y+1.15, '• Send bytecode', ha='left', va='center',
        fontsize=8, linespacing=1.4)
ax.text(stage['x']+stage_width/2, stage_y+0.95, '• Pay gas fee', ha='left', va='center',
        fontsize=8)
ax.text(stage['x']+stage_width/2, stage_y+0.75, '• Get address', ha='left', va='center',
        fontsize=8)

# Contract address
addr_box = FancyBboxPatch((stage['x']+0.15, stage_y+0.15), stage_width-0.3, 0.45,
                         boxstyle="round,pad=0.05",
                         edgecolor=stage['color'], facecolor='white',
                         linewidth=1.5, zorder=3)
ax.add_patch(addr_box)
ax.text(stage['x']+stage_width/2, stage_y+0.5, 'Contract Address',
        ha='center', va='center', fontsize=8, fontweight='bold')
ax.text(stage['x']+stage_width/2, stage_y+0.3, '0x742d...4e89',
        ha='center', va='center', fontsize=7, family='monospace', color=stage['color'])

# Arrow to Stage 4
arrow3 = FancyArrowPatch((stage['x']+stage_width, stage_y+stage_height/2),
                        (stages[3]['x'], stage_y+stage_height/2),
                        arrowstyle='->', mutation_scale=25,
                        linewidth=3, color='#666666', zorder=1)
ax.add_artist(arrow3)
ax.text((stage['x']+stage_width+stages[3]['x'])/2, stage_y+stage_height/2+0.25,
        'call', ha='center', va='bottom', fontsize=8, style='italic',
        color='#666666')

# Stage 4: Interact
stage = stages[3]
box4 = FancyBboxPatch((stage['x'], stage_y), stage_width, stage_height,
                      boxstyle="round,pad=0.08",
                      edgecolor=stage['color'], facecolor=stage['bgcolor'],
                      linewidth=3, zorder=2)
ax.add_patch(box4)

circle4 = Circle((stage['x']+0.3, stage_y+stage_height-0.3), 0.18,
                color=stage['color'], zorder=3)
ax.add_patch(circle4)
ax.text(stage['x']+0.3, stage_y+stage_height-0.3, '4', ha='center', va='center',
        fontsize=12, fontweight='bold', color='white', zorder=4)

ax.text(stage['x']+stage_width/2, stage_y+stage_height-0.35, 'Interact',
        ha='center', va='top', fontsize=13, fontweight='bold', color=stage['color'])

ax.text(stage['x']+stage_width/2, stage_y+1.35, 'Function Calls',
        ha='center', va='center', fontsize=10, fontweight='bold')

# Read operations
read_box = FancyBboxPatch((stage['x']+0.15, stage_y+0.8), stage_width-0.3, 0.4,
                         boxstyle="round,pad=0.05",
                         edgecolor=MLBLUE, facecolor='white',
                         linewidth=1.5, zorder=3)
ax.add_patch(read_box)
ax.text(stage['x']+stage_width/2, stage_y+1.08, 'Read (Free)',
        ha='center', va='center', fontsize=8, fontweight='bold', color=MLBLUE)
ax.text(stage['x']+stage_width/2, stage_y+0.92, 'view/pure',
        ha='center', va='center', fontsize=7, family='monospace')

# Write operations
write_box = FancyBboxPatch((stage['x']+0.15, stage_y+0.25), stage_width-0.3, 0.4,
                          boxstyle="round,pad=0.05",
                          edgecolor=MLRED, facecolor='white',
                          linewidth=1.5, zorder=3)
ax.add_patch(write_box)
ax.text(stage['x']+stage_width/2, stage_y+0.53, 'Write (Gas)',
        ha='center', va='center', fontsize=8, fontweight='bold', color=MLRED)
ax.text(stage['x']+stage_width/2, stage_y+0.37, 'state changes',
        ha='center', va='center', fontsize=7, style='italic')

# Bottom notes
notes_y = 1.8
ax.text(5, notes_y, 'Key Points:',
        ha='center', va='center', fontsize=11, fontweight='bold')

notes = [
    '• Immutable: Once deployed, code cannot be changed (upgradeable patterns exist)',
    '• Address: Deterministic, derived from deployer address + nonce',
    '• Gas Costs: Deployment is expensive; execution costs vary by operation',
    '• Verification: Etherscan allows source code verification for transparency'
]

for i, note in enumerate(notes):
    ax.text(5, notes_y - 0.3 - i*0.25, note,
            ha='center', va='center', fontsize=8, linespacing=1.3)

plt.tight_layout()

# Save
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, '03_smart_contract_lifecycle.pdf')
plt.savefig(output_path, dpi=300, bbox_inches='tight', format='pdf')
print(f"Chart saved to: {output_path}")

plt.show()
