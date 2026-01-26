#!/usr/bin/env python3
"""
Blockchain Structure Diagram
Shows the components of a block: header and body with transactions
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import os

# Color palette
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLPURPLE = '#3333B2'

def create_blockchain_structure():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Title
    ax.text(5, 5.5, 'Blockchain Block Structure',
            fontsize=18, fontweight='bold', ha='center')

    # Main block outline
    block_outline = FancyBboxPatch((1, 0.5), 8, 4.5,
                                   boxstyle="round,pad=0.1",
                                   edgecolor=MLBLUE,
                                   facecolor='white',
                                   linewidth=3)
    ax.add_patch(block_outline)

    # Block Header section
    header_box = Rectangle((1.2, 3.5), 7.6, 1.3,
                           facecolor=MLBLUE,
                           edgecolor=MLBLUE,
                           alpha=0.2,
                           linewidth=2)
    ax.add_patch(header_box)
    ax.text(5, 4.6, 'Block Header',
            fontsize=14, fontweight='bold', ha='center', color=MLBLUE)

    # Header components
    header_items = [
        ('Block Hash', 1.5, 4.1),
        ('Previous Hash', 3.5, 4.1),
        ('Timestamp', 5.5, 4.1),
        ('Nonce', 7.2, 4.1),
        ('Merkle Root', 4.5, 3.7)
    ]

    for item, x, y in header_items:
        ax.text(x, y, item, fontsize=10, ha='center',
                bbox=dict(boxstyle='round,pad=0.3',
                         facecolor='white',
                         edgecolor=MLBLUE,
                         linewidth=1))

    # Block Body section
    body_box = Rectangle((1.2, 0.7), 7.6, 2.5,
                         facecolor=MLGREEN,
                         edgecolor=MLGREEN,
                         alpha=0.1,
                         linewidth=2)
    ax.add_patch(body_box)
    ax.text(5, 2.9, 'Block Body (Transactions)',
            fontsize=14, fontweight='bold', ha='center', color=MLGREEN)

    # Transaction entries
    tx_positions = [
        (1.5, 2.3), (3.5, 2.3), (5.5, 2.3), (7.5, 2.3),
        (1.5, 1.7), (3.5, 1.7), (5.5, 1.7), (7.5, 1.7),
        (1.5, 1.1), (3.5, 1.1), (5.5, 1.1), (7.5, 1.1)
    ]

    for i, (x, y) in enumerate(tx_positions):
        ax.text(x, y, f'Tx {i+1}', fontsize=8, ha='center',
               bbox=dict(boxstyle='round,pad=0.2',
                        facecolor=MLGREEN,
                        edgecolor=MLGREEN,
                        alpha=0.3))

    plt.tight_layout()

    # Save in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, '01_blockchain_structure.pdf')
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")

    # Add PNG export for GitHub Pages
    output_png = output_path.replace('.pdf', '.png')
    plt.savefig(output_png, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none', format='png')
    print(f"PNG saved to: {output_png}")

    plt.close()

if __name__ == '__main__':
    create_blockchain_structure()
