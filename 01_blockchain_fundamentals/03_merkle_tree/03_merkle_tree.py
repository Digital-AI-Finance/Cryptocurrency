#!/usr/bin/env python3
"""
Merkle Tree Visualization
Shows how transaction hashes combine to form a Merkle root
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyArrowPatch
import os

# Color palette
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLPURPLE = '#3333B2'

def create_merkle_tree():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Title
    ax.text(5, 5.7, 'Merkle Tree Structure',
            fontsize=18, fontweight='bold', ha='center')

    # Level 0: Merkle Root
    root_circle = Circle((5, 4.8), 0.25, color=MLPURPLE, alpha=0.7, zorder=10)
    ax.add_patch(root_circle)
    ax.text(5, 4.8, 'Root', fontsize=8, ha='center', va='center',
           color='white', fontweight='bold')
    ax.text(6.2, 4.8, 'H(ABCD)', fontsize=9, va='center', color=MLPURPLE)

    # Level 1: Intermediate hashes
    level1_positions = [2.5, 7.5]
    level1_labels = ['H(AB)', 'H(CD)']
    for x_pos, label in zip(level1_positions, level1_labels):
        circle = Circle((x_pos, 3.5), 0.22, color=MLBLUE, alpha=0.6, zorder=10)
        ax.add_patch(circle)
        ax.text(x_pos, 3.5, label, fontsize=7, ha='center', va='center',
               color='white', fontweight='bold')

        # Arrow from root to intermediate
        arrow = FancyArrowPatch((5, 4.6), (x_pos, 3.75),
                               arrowstyle='-',
                               color='gray',
                               linewidth=1.5,
                               alpha=0.6,
                               zorder=1)
        ax.add_patch(arrow)

    # Level 2: Transaction hashes
    level2_positions = [1.2, 3.8, 6.2, 8.8]
    level2_labels = ['H(A)', 'H(B)', 'H(C)', 'H(D)']
    level2_colors = [MLGREEN, MLGREEN, MLGREEN, MLGREEN]

    for i, (x_pos, label, color) in enumerate(zip(level2_positions, level2_labels, level2_colors)):
        circle = Circle((x_pos, 2.2), 0.2, color=color, alpha=0.5, zorder=10)
        ax.add_patch(circle)
        ax.text(x_pos, 2.2, label, fontsize=7, ha='center', va='center',
               color='white', fontweight='bold')

        # Arrow from intermediate to transaction hash
        parent_x = level1_positions[i // 2]
        arrow = FancyArrowPatch((parent_x, 3.3), (x_pos, 2.42),
                               arrowstyle='-',
                               color='gray',
                               linewidth=1.5,
                               alpha=0.6,
                               zorder=1)
        ax.add_patch(arrow)

    # Level 3: Transactions (leaf nodes)
    tx_positions = [1.2, 3.8, 6.2, 8.8]
    tx_labels = ['Tx A', 'Tx B', 'Tx C', 'Tx D']

    for x_pos, label in zip(tx_positions, tx_labels):
        ax.text(x_pos, 1.2, label,
               fontsize=9, ha='center', va='center',
               bbox=dict(boxstyle='round,pad=0.3',
                        facecolor=MLORANGE,
                        edgecolor=MLORANGE,
                        alpha=0.3))

        # Arrow from transaction to hash
        arrow = FancyArrowPatch((x_pos, 1.45), (x_pos, 2.0),
                               arrowstyle='->',
                               color=MLGREEN,
                               linewidth=1.5,
                               alpha=0.7,
                               zorder=1)
        ax.add_patch(arrow)

    # Add legend/explanation
    ax.text(5, 0.5, 'H(X) = Hash of X  |  Each parent hash combines its children hashes',
           fontsize=9, ha='center', style='italic', color='gray')

    # Add layer labels on the left
    ax.text(0.3, 4.8, 'Root', fontsize=9, ha='right', va='center',
           color='gray', style='italic')
    ax.text(0.3, 3.5, 'Level 1', fontsize=9, ha='right', va='center',
           color='gray', style='italic')
    ax.text(0.3, 2.2, 'Level 2', fontsize=9, ha='right', va='center',
           color='gray', style='italic')
    ax.text(0.3, 1.2, 'Leaves', fontsize=9, ha='right', va='center',
           color='gray', style='italic')

    plt.tight_layout()

    # Save in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, '03_merkle_tree.pdf')
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")

    # Add PNG export for GitHub Pages
    output_png = output_path.replace('.pdf', '.png')
    plt.savefig(output_png, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none', format='png')
    print(f"PNG saved to: {output_png}")

    plt.close()

if __name__ == '__main__':
    create_merkle_tree()
