#!/usr/bin/env python3
"""
Public-Private Key Derivation Diagram
Shows: Private Key → Public Key → Address derivation
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import os

# Color palette
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLPURPLE = '#3333B2'

def create_key_derivation_diagram():
    """Create diagram showing key derivation process."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Title
    ax.text(5, 5.7, 'Public-Private Key Derivation',
            fontsize=20, fontweight='bold', ha='center', va='top')
    ax.text(5, 5.4, 'Cryptographic key hierarchy in Bitcoin',
            fontsize=11, ha='center', va='top', style='italic')

    # Step 1: Random Number Generator
    y_pos = 4.5
    rng_circle = Circle((1.5, y_pos), 0.4, edgecolor=MLPURPLE, facecolor='#E6D5F5', linewidth=2)
    ax.add_patch(rng_circle)
    ax.text(1.5, y_pos, 'RNG', fontsize=10, ha='center', va='center', fontweight='bold')
    ax.text(1.5, y_pos - 0.7, 'Random\nNumber', fontsize=9, ha='center', va='top')

    # Arrow to Private Key
    arrow1 = FancyArrowPatch((1.9, y_pos), (2.8, y_pos),
                             arrowstyle='->', mutation_scale=25,
                             linewidth=2, color=MLPURPLE)
    ax.add_patch(arrow1)
    ax.text(2.35, y_pos + 0.2, 'Generate', fontsize=8, ha='center', style='italic')

    # Step 2: Private Key
    pk_box = FancyBboxPatch((2.8, y_pos - 0.5), 2.4, 1,
                             boxstyle="round,pad=0.1",
                             edgecolor=MLRED, facecolor='#FFE6E6',
                             linewidth=3)
    ax.add_patch(pk_box)
    ax.text(4, y_pos + 0.25, 'Private Key', fontsize=12, ha='center', va='center', fontweight='bold', color=MLRED)
    ax.text(4, y_pos - 0.1, '256-bit secret', fontsize=9, ha='center', va='center')
    ax.text(4, y_pos - 0.35, '🔒 KEEP SECRET', fontsize=8, ha='center', va='center', style='italic')

    # Example private key (truncated)
    ax.text(4, y_pos - 0.9, 'e.g., 5KYZdU...', fontsize=7, ha='center', va='top', family='monospace',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

    # Arrow to Public Key
    arrow2 = FancyArrowPatch((5.2, y_pos), (6.1, y_pos),
                             arrowstyle='->', mutation_scale=25,
                             linewidth=2, color=MLPURPLE)
    ax.add_patch(arrow2)
    ax.text(5.65, y_pos + 0.3, 'ECDSA', fontsize=8, ha='center', fontweight='bold')
    ax.text(5.65, y_pos + 0.15, 'Elliptic Curve', fontsize=7, ha='center', style='italic')

    # Step 3: Public Key
    pub_box = FancyBboxPatch((6.1, y_pos - 0.5), 2.4, 1,
                              boxstyle="round,pad=0.1",
                              edgecolor=MLBLUE, facecolor='#E6F2FF',
                              linewidth=3)
    ax.add_patch(pub_box)
    ax.text(7.3, y_pos + 0.25, 'Public Key', fontsize=12, ha='center', va='center', fontweight='bold', color=MLBLUE)
    ax.text(7.3, y_pos - 0.1, 'Derived from private', fontsize=9, ha='center', va='center')
    ax.text(7.3, y_pos - 0.35, '✓ Safe to share', fontsize=8, ha='center', va='center', style='italic')

    # Example public key (truncated)
    ax.text(7.3, y_pos - 0.9, 'e.g., 04a34b...', fontsize=7, ha='center', va='top', family='monospace',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

    # Arrow down to hashing
    arrow3 = FancyArrowPatch((7.3, y_pos - 0.5), (7.3, y_pos - 1.3),
                             arrowstyle='->', mutation_scale=25,
                             linewidth=2, color=MLPURPLE)
    ax.add_patch(arrow3)
    ax.text(7.8, y_pos - 0.9, 'SHA-256 +', fontsize=8, ha='left', fontweight='bold')
    ax.text(7.8, y_pos - 1.05, 'RIPEMD-160', fontsize=8, ha='left', fontweight='bold')

    # Step 4: Address
    addr_box = FancyBboxPatch((6.1, y_pos - 2.2), 2.4, 0.9,
                               boxstyle="round,pad=0.1",
                               edgecolor=MLGREEN, facecolor='#E6FFE6',
                               linewidth=3)
    ax.add_patch(addr_box)
    ax.text(7.3, y_pos - 1.5, 'Bitcoin Address', fontsize=12, ha='center', va='center', fontweight='bold', color=MLGREEN)
    ax.text(7.3, y_pos - 1.8, 'Public identifier', fontsize=9, ha='center', va='center')

    # Example address (truncated)
    ax.text(7.3, y_pos - 2.3, 'e.g., 1A1zP1eP5Q...', fontsize=7, ha='center', va='top', family='monospace',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

    # One-way property annotation
    ax.annotate('', xy=(6.1, y_pos), xytext=(5.2, y_pos),
                arrowprops=dict(arrowstyle='<-', color='red', linewidth=1.5, linestyle='dashed'))
    ax.text(5.65, y_pos - 0.2, '✗ Cannot reverse', fontsize=7, ha='center', color=MLRED, fontweight='bold')

    # Information boxes at bottom
    # Security note
    security_box = (
        'Security Properties:\n'
        '• Private key must remain secret\n'
        '• Public key can be freely shared\n'
        '• Cannot derive private from public\n'
        '• One private key → One public key'
    )
    ax.text(2.5, 1.2, security_box,
            fontsize=9, ha='left', va='top',
            bbox=dict(boxstyle='round', facecolor='#FFE6E6', alpha=0.7, edgecolor=MLRED, linewidth=2))

    # Use case note
    usecase_box = (
        'Use Cases:\n'
        '• Private key: Sign transactions\n'
        '• Public key: Verify signatures\n'
        '• Address: Receive Bitcoin'
    )
    ax.text(7.5, 1.2, usecase_box,
            fontsize=9, ha='right', va='top',
            bbox=dict(boxstyle='round', facecolor='#E6FFE6', alpha=0.7, edgecolor=MLGREEN, linewidth=2))

    plt.tight_layout()
    return fig

def main():
    """Generate and save the key derivation diagram."""
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(os.path.abspath(__file__))

    # Generate chart
    fig = create_key_derivation_diagram()

    # Save as PDF
    output_path = os.path.join(output_dir, '03_public_private_keys.pdf')
    fig.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == "__main__":
    main()
