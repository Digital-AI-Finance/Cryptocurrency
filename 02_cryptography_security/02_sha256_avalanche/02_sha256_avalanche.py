#!/usr/bin/env python3
"""
SHA-256 Avalanche Effect Visualization
Visual comparison of two similar inputs producing vastly different hashes
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import hashlib
import os

# Color palette
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLPURPLE = '#3333B2'

def hash_to_binary(text):
    """Convert text to SHA-256 hash in binary format."""
    hash_hex = hashlib.sha256(text.encode()).hexdigest()
    # Convert hex to binary (256 bits)
    hash_bin = bin(int(hash_hex, 16))[2:].zfill(256)
    return hash_hex, hash_bin

def create_sha256_avalanche_chart():
    """Create visual comparison of avalanche effect."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Title
    ax.text(5, 5.7, 'SHA-256 Avalanche Effect',
            fontsize=20, fontweight='bold', ha='center', va='top')
    ax.text(5, 5.4, 'Tiny input change → Drastically different output',
            fontsize=12, ha='center', va='top', style='italic', color=MLRED)

    # Input 1
    input1 = "Bitcoin"
    hash1_hex, hash1_bin = hash_to_binary(input1)

    input1_box = FancyBboxPatch((0.2, 4.2), 4.3, 0.6,
                                 boxstyle="round,pad=0.05",
                                 edgecolor=MLBLUE, facecolor='lightblue',
                                 linewidth=2)
    ax.add_patch(input1_box)
    ax.text(0.4, 4.65, f'Input 1:', fontsize=10, fontweight='bold', va='center')
    ax.text(0.4, 4.35, f'"{input1}"', fontsize=11, va='center', family='monospace')

    # Hash 1 (truncated display)
    hash1_box = FancyBboxPatch((0.2, 3.4), 4.3, 0.6,
                                boxstyle="round,pad=0.05",
                                edgecolor=MLGREEN, facecolor='lightgreen',
                                linewidth=2)
    ax.add_patch(hash1_box)
    ax.text(0.4, 3.85, 'Hash 1:', fontsize=10, fontweight='bold', va='center')
    ax.text(0.4, 3.55, hash1_hex[:32] + '...', fontsize=8, va='center', family='monospace')

    # Input 2 (one character different)
    input2 = "bitcoin"  # lowercase 'b'
    hash2_hex, hash2_bin = hash_to_binary(input2)

    input2_box = FancyBboxPatch((5.5, 4.2), 4.3, 0.6,
                                 boxstyle="round,pad=0.05",
                                 edgecolor=MLBLUE, facecolor='lightblue',
                                 linewidth=2)
    ax.add_patch(input2_box)
    ax.text(5.7, 4.65, f'Input 2:', fontsize=10, fontweight='bold', va='center')
    ax.text(5.7, 4.35, f'"{input2}"', fontsize=11, va='center', family='monospace')
    # Highlight the difference
    ax.text(7.8, 4.05, '← Only 1 char different!', fontsize=8, color=MLRED, style='italic', va='center')

    # Hash 2 (truncated display)
    hash2_box = FancyBboxPatch((5.5, 3.4), 4.3, 0.6,
                                boxstyle="round,pad=0.05",
                                edgecolor=MLGREEN, facecolor='lightgreen',
                                linewidth=2)
    ax.add_patch(hash2_box)
    ax.text(5.7, 3.85, 'Hash 2:', fontsize=10, fontweight='bold', va='center')
    ax.text(5.7, 3.55, hash2_hex[:32] + '...', fontsize=8, va='center', family='monospace')

    # Binary visualization section
    ax.text(5, 2.9, 'Binary Bit Comparison (first 64 bits shown)',
            fontsize=11, ha='center', va='center', fontweight='bold')

    # Display first 64 bits of each hash as colored blocks
    block_size = 0.12
    start_x = 0.5
    y1 = 2.3
    y2 = 1.8

    for i in range(64):
        bit1 = hash1_bin[i]
        bit2 = hash2_bin[i]

        x = start_x + i * block_size

        # Hash 1 bit
        color1 = MLBLUE if bit1 == '1' else 'white'
        rect1 = Rectangle((x, y1), block_size * 0.9, 0.3,
                          facecolor=color1, edgecolor='black', linewidth=0.5)
        ax.add_patch(rect1)

        # Hash 2 bit
        color2 = MLORANGE if bit2 == '1' else 'white'
        rect2 = Rectangle((x, y2), block_size * 0.9, 0.3,
                          facecolor=color2, edgecolor='black', linewidth=0.5)
        ax.add_patch(rect2)

        # Highlight differences
        if bit1 != bit2:
            rect_highlight = Rectangle((x, y2 - 0.05), block_size * 0.9, 0.4,
                                       facecolor='none', edgecolor=MLRED, linewidth=2)
            ax.add_patch(rect_highlight)

    ax.text(0.3, y1 + 0.15, 'Hash 1:', fontsize=9, va='center', fontweight='bold')
    ax.text(0.3, y2 + 0.15, 'Hash 2:', fontsize=9, va='center', fontweight='bold')

    # Count differences
    differences = sum(1 for i in range(256) if hash1_bin[i] != hash2_bin[i])
    percentage = (differences / 256) * 100

    # Statistics box
    stats_text = (
        f'Bit Differences: {differences} out of 256 bits ({percentage:.1f}%)\n'
        f'Red boxes show differing bits'
    )
    ax.text(5, 1.2, stats_text,
            fontsize=10, ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # Explanation
    explanation = (
        'The Avalanche Effect ensures that even the smallest change in input\n'
        'produces a completely different, unpredictable hash output.'
    )
    ax.text(5, 0.4, explanation,
            fontsize=9, ha='center', va='center', style='italic',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))

    plt.tight_layout()
    return fig

def main():
    """Generate and save the SHA-256 avalanche effect chart."""
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(os.path.abspath(__file__))

    # Generate chart
    fig = create_sha256_avalanche_chart()

    # Save as PDF
    output_path = os.path.join(output_dir, '02_sha256_avalanche.pdf')
    fig.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    # Add PNG export for GitHub Pages
    output_png = output_path.replace('.pdf', '.png')
    fig.savefig(output_png, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none', format='png')
    print(f"PNG saved to: {output_png}")

    plt.close()

if __name__ == "__main__":
    main()
