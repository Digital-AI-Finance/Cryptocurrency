#!/usr/bin/env python3
"""
Hash Function Flowchart
Shows: Input → SHA-256 → Fixed 256-bit output
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

def create_hash_function_flowchart():
    """Create flowchart showing hash function process."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Title
    ax.text(5, 5.5, 'Hash Function Process',
            fontsize=20, fontweight='bold', ha='center', va='top')

    # Input box
    input_box = FancyBboxPatch((0.5, 3), 2, 1,
                                boxstyle="round,pad=0.1",
                                edgecolor=MLBLUE, facecolor='lightblue',
                                linewidth=2)
    ax.add_patch(input_box)
    ax.text(1.5, 3.5, 'Input Data\n(Any Size)',
            fontsize=12, ha='center', va='center', fontweight='bold')

    # Arrow 1
    arrow1 = FancyArrowPatch((2.5, 3.5), (3.5, 3.5),
                             arrowstyle='->', mutation_scale=30,
                             linewidth=2, color=MLPURPLE)
    ax.add_patch(arrow1)

    # SHA-256 box (processing)
    sha_box = FancyBboxPatch((3.5, 2.5), 3, 2,
                              boxstyle="round,pad=0.1",
                              edgecolor=MLORANGE, facecolor='#FFE5CC',
                              linewidth=3)
    ax.add_patch(sha_box)
    ax.text(5, 4, 'SHA-256',
            fontsize=16, ha='center', va='center', fontweight='bold', color=MLORANGE)
    ax.text(5, 3.4, 'Hash Function',
            fontsize=11, ha='center', va='center', style='italic')
    ax.text(5, 2.9, '• Deterministic\n• One-way\n• Collision-resistant',
            fontsize=9, ha='center', va='center')

    # Arrow 2
    arrow2 = FancyArrowPatch((6.5, 3.5), (7.5, 3.5),
                             arrowstyle='->', mutation_scale=30,
                             linewidth=2, color=MLPURPLE)
    ax.add_patch(arrow2)

    # Output box
    output_box = FancyBboxPatch((7.5, 3), 2, 1,
                                 boxstyle="round,pad=0.1",
                                 edgecolor=MLGREEN, facecolor='lightgreen',
                                 linewidth=2)
    ax.add_patch(output_box)
    ax.text(8.5, 3.5, 'Fixed Output\n(256 bits)',
            fontsize=12, ha='center', va='center', fontweight='bold')

    # Example at bottom
    example_text = (
        'Example:\n'
        'Input: "Hello, World!"\n'
        'Output: dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f'
    )
    ax.text(5, 1.5, example_text,
            fontsize=10, ha='center', va='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

    # Properties box
    properties_text = (
        'Key Properties:\n'
        '1. Same input always produces same output\n'
        '2. Cannot reverse engineer input from output\n'
        '3. Tiny input change drastically changes output'
    )
    ax.text(5, 0.3, properties_text,
            fontsize=9, ha='center', va='bottom', style='italic',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))

    plt.tight_layout()
    return fig

def main():
    """Generate and save the hash function flowchart."""
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(os.path.abspath(__file__))

    # Generate chart
    fig = create_hash_function_flowchart()

    # Save as PDF
    output_path = os.path.join(output_dir, '01_hash_function.pdf')
    fig.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == "__main__":
    main()
