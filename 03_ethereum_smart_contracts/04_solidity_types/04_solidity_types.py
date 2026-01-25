#!/usr/bin/env python3
"""
Solidity Data Types Chart
Reference table/grid of Solidity data types
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle
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
ax.text(5, 5.7, 'Solidity Data Types Reference',
        ha='center', va='top', fontsize=18, fontweight='bold')

# Category positions
categories = [
    {
        'title': 'Value Types',
        'color': MLBLUE,
        'bgcolor': '#E3F2FD',
        'x': 0.3,
        'y': 3.0,
        'width': 3.0,
        'height': 2.2,
        'types': [
            ('bool', 'true / false', 'boolean flag'),
            ('int / uint', 'int8 to int256', 'signed/unsigned integers'),
            ('uint256', 'most common', '0 to 2^256-1'),
            ('address', '20 bytes', 'Ethereum address'),
            ('bytes1 to bytes32', 'fixed size', 'byte arrays'),
            ('enum', 'State {Open, Closed}', 'custom types'),
        ]
    },
    {
        'title': 'Reference Types',
        'color': MLGREEN,
        'bgcolor': '#E8F5E9',
        'x': 3.5,
        'y': 3.0,
        'width': 3.0,
        'height': 2.2,
        'types': [
            ('array', 'uint[] / uint[5]', 'dynamic/fixed arrays'),
            ('string', 'UTF-8 text', 'dynamic byte array'),
            ('bytes', 'dynamic size', 'byte array'),
            ('struct', 'custom data', 'grouped variables'),
            ('mapping', 'key => value', 'hash table'),
            ('mapping(address => uint)', 'balances', 'common pattern'),
        ]
    },
    {
        'title': 'Special Types',
        'color': MLPURPLE,
        'bgcolor': '#F3E5F5',
        'x': 6.7,
        'y': 3.0,
        'width': 3.0,
        'height': 2.2,
        'types': [
            ('msg.sender', 'address', 'caller address'),
            ('msg.value', 'uint', 'wei sent'),
            ('block.timestamp', 'uint', 'current time'),
            ('block.number', 'uint', 'current block'),
            ('tx.origin', 'address', 'transaction origin'),
            ('this', 'contract type', 'contract instance'),
        ]
    }
]

# Draw categories
for cat in categories:
    # Main box
    box = FancyBboxPatch((cat['x'], cat['y']), cat['width'], cat['height'],
                         boxstyle="round,pad=0.08",
                         edgecolor=cat['color'], facecolor=cat['bgcolor'],
                         linewidth=2.5, zorder=1)
    ax.add_patch(box)

    # Title
    ax.text(cat['x'] + cat['width']/2, cat['y'] + cat['height'] - 0.15,
            cat['title'], ha='center', va='top',
            fontsize=12, fontweight='bold', color=cat['color'])

    # Types list
    start_y = cat['y'] + cat['height'] - 0.5
    row_height = 0.28

    for i, (type_name, syntax, description) in enumerate(cat['types']):
        y_pos = start_y - i * row_height

        # Type name (bold)
        ax.text(cat['x'] + 0.15, y_pos, type_name,
                ha='left', va='center', fontsize=8,
                fontweight='bold', family='monospace')

        # Syntax (code style)
        ax.text(cat['x'] + cat['width']/2, y_pos, syntax,
                ha='center', va='center', fontsize=7,
                family='monospace', color='#555555')

        # Description (italic)
        ax.text(cat['x'] + cat['width'] - 0.15, y_pos, description,
                ha='right', va='center', fontsize=7,
                style='italic', color='#666666')

# Storage locations section
storage_y = 1.8
ax.text(5, storage_y + 0.5, 'Data Locations',
        ha='center', va='center', fontsize=13, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#F5F5F5',
                 edgecolor='black', linewidth=2))

storage_types = [
    {
        'name': 'storage',
        'color': MLORANGE,
        'bgcolor': '#FFF3E0',
        'x': 0.5,
        'desc': 'Persistent\nOn blockchain\nExpensive',
    },
    {
        'name': 'memory',
        'color': MLBLUE,
        'bgcolor': '#E3F2FD',
        'x': 3.5,
        'desc': 'Temporary\nFunction scope\nCheaper',
    },
    {
        'name': 'calldata',
        'color': MLGREEN,
        'bgcolor': '#E8F5E9',
        'x': 6.5,
        'desc': 'Read-only\nExternal args\nCheapest',
    }
]

storage_width = 2.8
storage_height = 0.9

for st in storage_types:
    box = FancyBboxPatch((st['x'], storage_y - 0.6), storage_width, storage_height,
                         boxstyle="round,pad=0.06",
                         edgecolor=st['color'], facecolor=st['bgcolor'],
                         linewidth=2, zorder=1)
    ax.add_patch(box)

    ax.text(st['x'] + storage_width/2, storage_y + 0.15,
            st['name'], ha='center', va='center',
            fontsize=10, fontweight='bold', family='monospace',
            color=st['color'])

    ax.text(st['x'] + storage_width/2, storage_y - 0.25,
            st['desc'], ha='center', va='center',
            fontsize=7, linespacing=1.3)

# Visibility modifiers
visibility_y = 0.5
ax.text(2.5, visibility_y + 0.3, 'Function Visibility',
        ha='center', va='center', fontsize=11, fontweight='bold')

visibility_items = [
    ('public', MLGREEN, 'All (creates getter)'),
    ('external', MLBLUE, 'External only'),
    ('internal', MLORANGE, 'This + derived'),
    ('private', MLRED, 'This contract only'),
]

vis_x_start = 0.5
vis_width = 1.1
vis_spacing = 0.15

for i, (vis, color, desc) in enumerate(visibility_items):
    x_pos = vis_x_start + i * (vis_width + vis_spacing)

    # Box
    box = FancyBboxPatch((x_pos, visibility_y - 0.35), vis_width, 0.3,
                         boxstyle="round,pad=0.04",
                         edgecolor=color, facecolor='white',
                         linewidth=1.5, zorder=1)
    ax.add_patch(box)

    # Visibility keyword
    ax.text(x_pos + vis_width/2, visibility_y - 0.1,
            vis, ha='center', va='center',
            fontsize=8, fontweight='bold', family='monospace',
            color=color)

    # Description
    ax.text(x_pos + vis_width/2, visibility_y - 0.28,
            desc, ha='center', va='center',
            fontsize=6, style='italic')

# State mutability
ax.text(7.5, visibility_y + 0.3, 'State Mutability',
        ha='center', va='center', fontsize=11, fontweight='bold')

mutability_items = [
    ('view', MLBLUE, 'Read state'),
    ('pure', MLGREEN, 'No state'),
    ('payable', MLORANGE, 'Accepts ETH'),
]

mut_x_start = 6.0
mut_width = 1.3
mut_spacing = 0.1

for i, (mut, color, desc) in enumerate(mutability_items):
    x_pos = mut_x_start + i * (mut_width + mut_spacing)

    # Box
    box = FancyBboxPatch((x_pos, visibility_y - 0.35), mut_width, 0.3,
                         boxstyle="round,pad=0.04",
                         edgecolor=color, facecolor='white',
                         linewidth=1.5, zorder=1)
    ax.add_patch(box)

    # Mutability keyword
    ax.text(x_pos + mut_width/2, visibility_y - 0.1,
            mut, ha='center', va='center',
            fontsize=8, fontweight='bold', family='monospace',
            color=color)

    # Description
    ax.text(x_pos + mut_width/2, visibility_y - 0.28,
            desc, ha='center', va='center',
            fontsize=6, style='italic')

plt.tight_layout()

# Save
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, '04_solidity_types.pdf')
plt.savefig(output_path, dpi=300, bbox_inches='tight', format='pdf')
print(f"Chart saved to: {output_path}")

plt.show()
