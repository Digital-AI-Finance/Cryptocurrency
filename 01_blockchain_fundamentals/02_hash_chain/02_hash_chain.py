#!/usr/bin/env python3
"""
Hash Chain Visualization
Shows 4 blocks linked by hash pointers forming a chain
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

# Color palette
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLPURPLE = '#3333B2'

def create_hash_chain():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Title
    ax.text(5, 5.5, 'Blockchain Hash Chain',
            fontsize=18, fontweight='bold', ha='center')

    # Block positions
    block_positions = [0.5, 3, 5.5, 8]
    block_hashes = ['0x7a3f...', '0x9b2c...', '0x4e1d...', '0x6f8a...']
    prev_hashes = ['Genesis', '0x7a3f...', '0x9b2c...', '0x4e1d...']
    block_nums = ['Block 0', 'Block 1', 'Block 2', 'Block 3']

    colors = [MLPURPLE, MLBLUE, MLGREEN, MLORANGE]

    for i, (x_pos, block_hash, prev_hash, block_num, color) in enumerate(
            zip(block_positions, block_hashes, prev_hashes, block_nums, colors)):

        # Block box
        block = FancyBboxPatch((x_pos, 1.5), 2, 2.8,
                               boxstyle="round,pad=0.1",
                               edgecolor=color,
                               facecolor='white',
                               linewidth=2.5)
        ax.add_patch(block)

        # Block number
        ax.text(x_pos + 1, 4.1, block_num,
               fontsize=11, fontweight='bold', ha='center', color=color)

        # Block hash
        ax.text(x_pos + 1, 3.6, 'Hash:',
               fontsize=9, ha='center', fontweight='bold')
        ax.text(x_pos + 1, 3.3, block_hash,
               fontsize=8, ha='center',
               bbox=dict(boxstyle='round,pad=0.2',
                        facecolor=color,
                        alpha=0.2))

        # Previous hash
        ax.text(x_pos + 1, 2.7, 'Prev Hash:',
               fontsize=9, ha='center', fontweight='bold')
        ax.text(x_pos + 1, 2.4, prev_hash,
               fontsize=8, ha='center',
               bbox=dict(boxstyle='round,pad=0.2',
                        facecolor='lightgray',
                        alpha=0.3))

        # Transactions indicator
        ax.text(x_pos + 1, 1.9, 'Transactions',
               fontsize=8, ha='center', style='italic', color='gray')

        # Arrow to next block (except for last block)
        if i < len(block_positions) - 1:
            arrow = FancyArrowPatch((x_pos + 2.1, 2.9),
                                   (block_positions[i+1] - 0.1, 2.9),
                                   arrowstyle='->,head_width=0.3,head_length=0.3',
                                   color=colors[i+1],
                                   linewidth=2.5,
                                   zorder=0)
            ax.add_patch(arrow)

    # Add explanation
    ax.text(5, 0.8, 'Each block contains the hash of the previous block, forming an immutable chain',
           fontsize=10, ha='center', style='italic', color='gray')

    plt.tight_layout()

    # Save in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, '02_hash_chain.pdf')
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")
    plt.close()

if __name__ == '__main__':
    create_hash_chain()
