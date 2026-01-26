#!/usr/bin/env python3
"""
Consensus Mechanisms Comparison
Side-by-side comparison of Proof of Work (PoW) vs Proof of Stake (PoS)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch
import os

# Color palette
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLPURPLE = '#3333B2'

def create_consensus_comparison():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6), dpi=300)

    # Main title
    fig.suptitle('Consensus Mechanisms Comparison', fontsize=18, fontweight='bold', y=0.98)

    # ========== Proof of Work (PoW) ==========
    ax1.set_xlim(0, 5)
    ax1.set_ylim(0, 6)
    ax1.axis('off')
    ax1.set_title('Proof of Work (PoW)', fontsize=14, fontweight='bold',
                  color=MLBLUE, pad=10)

    # Mining process
    ax1.text(2.5, 5, 'Mining Process', fontsize=11, ha='center',
            fontweight='bold', color=MLBLUE)

    # Miners
    miner_positions = [(0.8, 3.8), (2.5, 3.8), (4.2, 3.8)]
    for i, (x, y) in enumerate(miner_positions):
        circle = Circle((x, y), 0.3, color=MLBLUE, alpha=0.3, zorder=10)
        ax1.add_patch(circle)
        ax1.text(x, y, f'M{i+1}', fontsize=9, ha='center', va='center',
                fontweight='bold', color=MLBLUE)
        ax1.text(x, y-0.6, 'Computing\nHash', fontsize=7, ha='center',
                style='italic')

    # Computational work indicator
    ax1.text(2.5, 2.6, 'Computational Power', fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.4',
                     facecolor=MLBLUE,
                     alpha=0.2))

    # Winner
    winner_box = FancyBboxPatch((1.5, 1.2), 2, 0.6,
                                boxstyle="round,pad=0.1",
                                edgecolor=MLGREEN,
                                facecolor=MLGREEN,
                                alpha=0.3,
                                linewidth=2)
    ax1.add_patch(winner_box)
    ax1.text(2.5, 1.5, 'First to find valid nonce wins',
            fontsize=8, ha='center', fontweight='bold')

    # Key characteristics
    characteristics_pow = [
        '• Energy intensive',
        '• Hardware competition',
        '• 51% attack risk',
        '• Proven security'
    ]

    for i, char in enumerate(characteristics_pow):
        ax1.text(0.3, 0.8 - i*0.2, char, fontsize=8, va='top')

    # ========== Proof of Stake (PoS) ==========
    ax2.set_xlim(0, 5)
    ax2.set_ylim(0, 6)
    ax2.axis('off')
    ax2.set_title('Proof of Stake (PoS)', fontsize=14, fontweight='bold',
                  color=MLORANGE, pad=10)

    # Staking process
    ax2.text(2.5, 5, 'Staking Process', fontsize=11, ha='center',
            fontweight='bold', color=MLORANGE)

    # Validators with stakes
    validator_positions = [(0.8, 3.8), (2.5, 3.8), (4.2, 3.8)]
    stakes = ['1000', '5000', '2000']
    for i, ((x, y), stake) in enumerate(zip(validator_positions, stakes)):
        circle = Circle((x, y), 0.3, color=MLORANGE, alpha=0.3, zorder=10)
        ax2.add_patch(circle)
        ax2.text(x, y, f'V{i+1}', fontsize=9, ha='center', va='center',
                fontweight='bold', color=MLORANGE)
        ax2.text(x, y-0.6, f'Stake:\n{stake} coins', fontsize=7, ha='center',
                style='italic')

    # Selection mechanism
    ax2.text(2.5, 2.6, 'Random Selection\n(weighted by stake)',
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.4',
                     facecolor=MLORANGE,
                     alpha=0.2))

    # Selected validator
    selected_box = FancyBboxPatch((1.5, 1.2), 2, 0.6,
                                  boxstyle="round,pad=0.1",
                                  edgecolor=MLGREEN,
                                  facecolor=MLGREEN,
                                  alpha=0.3,
                                  linewidth=2)
    ax2.add_patch(selected_box)
    ax2.text(2.5, 1.5, 'Selected validator proposes block',
            fontsize=8, ha='center', fontweight='bold')

    # Key characteristics
    characteristics_pos = [
        '• Energy efficient',
        '• Stake-based selection',
        '• Economic penalties',
        '• Lower barriers to entry'
    ]

    for i, char in enumerate(characteristics_pos):
        ax2.text(0.3, 0.8 - i*0.2, char, fontsize=8, va='top')

    plt.tight_layout()

    # Save in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, '04_consensus_comparison.pdf')
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")

    # Add PNG export for GitHub Pages
    output_png = output_path.replace('.pdf', '.png')
    plt.savefig(output_png, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none', format='png')
    print(f"PNG saved to: {output_png}")

    plt.close()

if __name__ == '__main__':
    create_consensus_comparison()
