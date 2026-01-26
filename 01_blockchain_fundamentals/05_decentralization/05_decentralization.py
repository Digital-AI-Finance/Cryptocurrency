#!/usr/bin/env python3
"""
Decentralization Comparison
Network diagrams showing centralized (star) vs decentralized (mesh) architectures
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np
import os

# Color palette
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLPURPLE = '#3333B2'

def create_decentralization_comparison():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6), dpi=300)

    # Main title
    fig.suptitle('Network Architecture Comparison', fontsize=18, fontweight='bold', y=0.98)

    # ========== Centralized Network ==========
    ax1.set_xlim(0, 5)
    ax1.set_ylim(0, 6)
    ax1.axis('off')
    ax1.set_title('Centralized Network', fontsize=14, fontweight='bold',
                  color=MLRED, pad=10)

    # Central server (larger)
    center = (2.5, 3)
    central_circle = Circle(center, 0.4, color=MLRED, alpha=0.7, zorder=10)
    ax1.add_patch(central_circle)
    ax1.text(center[0], center[1], 'Server', fontsize=9, ha='center',
            va='center', color='white', fontweight='bold')

    # Client nodes arranged in a circle
    n_clients = 8
    radius = 1.8
    angles = np.linspace(0, 2*np.pi, n_clients, endpoint=False)

    for angle in angles:
        x = center[0] + radius * np.cos(angle)
        y = center[1] + radius * np.sin(angle)

        # Client node
        client_circle = Circle((x, y), 0.25, color=MLBLUE, alpha=0.5, zorder=10)
        ax1.add_patch(client_circle)
        ax1.text(x, y, 'C', fontsize=7, ha='center', va='center',
                color='white', fontweight='bold')

        # Connection to center
        arrow = FancyArrowPatch((x, y), center,
                               arrowstyle='-',
                               color='gray',
                               linewidth=1.5,
                               alpha=0.5,
                               zorder=1)
        ax1.add_patch(arrow)

    # Characteristics
    characteristics_central = [
        '• Single point of failure',
        '• Controlled by one entity',
        '• Fast but vulnerable',
        '• Easy to censor'
    ]

    for i, char in enumerate(characteristics_central):
        ax1.text(0.2, 0.9 - i*0.22, char, fontsize=8, va='top')

    # ========== Decentralized Network ==========
    ax2.set_xlim(0, 5)
    ax2.set_ylim(0, 6)
    ax2.axis('off')
    ax2.set_title('Decentralized Network', fontsize=14, fontweight='bold',
                  color=MLGREEN, pad=10)

    # Peer nodes in a mesh
    n_peers = 9
    positions = [
        (1.2, 4.5), (2.5, 4.8), (3.8, 4.5),
        (1.0, 3.2), (2.5, 3.0), (4.0, 3.2),
        (1.2, 1.5), (2.5, 1.2), (3.8, 1.5)
    ]

    # Draw connections (partial mesh for clarity)
    connections = [
        (0, 1), (1, 2), (0, 3), (1, 4), (2, 5),
        (3, 4), (4, 5), (3, 6), (4, 7), (5, 8),
        (6, 7), (7, 8), (0, 4), (2, 4), (4, 6), (4, 8)
    ]

    for i, j in connections:
        x1, y1 = positions[i]
        x2, y2 = positions[j]
        arrow = FancyArrowPatch((x1, y1), (x2, y2),
                               arrowstyle='-',
                               color='gray',
                               linewidth=1.2,
                               alpha=0.4,
                               zorder=1)
        ax2.add_patch(arrow)

    # Draw peer nodes
    for i, (x, y) in enumerate(positions):
        peer_circle = Circle((x, y), 0.25, color=MLGREEN, alpha=0.6, zorder=10)
        ax2.add_patch(peer_circle)
        ax2.text(x, y, 'P', fontsize=7, ha='center', va='center',
                color='white', fontweight='bold')

    # Characteristics
    characteristics_decentral = [
        '• No single point of failure',
        '• Distributed control',
        '• Resilient and robust',
        '• Censorship resistant'
    ]

    for i, char in enumerate(characteristics_decentral):
        ax2.text(0.2, 0.9 - i*0.22, char, fontsize=8, va='top')

    plt.tight_layout()

    # Save in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, '05_decentralization.pdf')
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")

    # Add PNG export for GitHub Pages
    output_png = output_path.replace('.pdf', '.png')
    plt.savefig(output_png, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none', format='png')
    print(f"PNG saved to: {output_png}")

    plt.close()

if __name__ == '__main__':
    create_decentralization_comparison()
