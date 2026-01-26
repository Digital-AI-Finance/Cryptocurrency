#!/usr/bin/env python3
"""
Digital Signature Flow Diagram
Shows: message + private key → signature → verify with public key
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Wedge
import os

# Color palette
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLPURPLE = '#3333B2'

def create_digital_signature_flow():
    """Create flowchart showing digital signature process."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Title
    ax.text(5, 5.8, 'Digital Signature Flow',
            fontsize=20, fontweight='bold', ha='center', va='top')
    ax.text(5, 5.5, 'How Bitcoin transactions are signed and verified',
            fontsize=11, ha='center', va='top', style='italic')

    # ===== SIGNING PROCESS (LEFT SIDE) =====
    ax.text(2.5, 5, 'SIGNING', fontsize=14, ha='center', fontweight='bold',
            color=MLORANGE, bbox=dict(boxstyle='round', facecolor='#FFE5CC'))

    # Message/Transaction
    msg_box = FancyBboxPatch((0.5, 3.8), 2, 0.7,
                              boxstyle="round,pad=0.05",
                              edgecolor=MLBLUE, facecolor='lightblue',
                              linewidth=2)
    ax.add_patch(msg_box)
    ax.text(1.5, 4.35, 'Message', fontsize=10, ha='center', va='center', fontweight='bold')
    ax.text(1.5, 4.0, '(Transaction Data)', fontsize=8, ha='center', va='center', style='italic')

    # Private Key
    pk_box = FancyBboxPatch((2.7, 3.8), 1.6, 0.7,
                             boxstyle="round,pad=0.05",
                             edgecolor=MLRED, facecolor='#FFE6E6',
                             linewidth=2)
    ax.add_patch(pk_box)
    ax.text(3.5, 4.35, 'Private Key', fontsize=10, ha='center', va='center', fontweight='bold')
    ax.text(3.5, 4.0, '🔒 Secret', fontsize=8, ha='center', va='center')

    # Arrows to signing
    arrow1 = FancyArrowPatch((1.5, 3.8), (2.0, 3.3),
                             arrowstyle='->', mutation_scale=20,
                             linewidth=1.5, color=MLPURPLE)
    ax.add_patch(arrow1)

    arrow2 = FancyArrowPatch((3.5, 3.8), (3.0, 3.3),
                             arrowstyle='->', mutation_scale=20,
                             linewidth=1.5, color=MLPURPLE)
    ax.add_patch(arrow2)

    # Signing algorithm box
    sign_box = FancyBboxPatch((1.5, 2.5), 2, 0.8,
                               boxstyle="round,pad=0.1",
                               edgecolor=MLORANGE, facecolor='#FFE5CC',
                               linewidth=2)
    ax.add_patch(sign_box)
    ax.text(2.5, 3.1, 'ECDSA Sign', fontsize=11, ha='center', va='center', fontweight='bold')
    ax.text(2.5, 2.8, 'Signing Algorithm', fontsize=8, ha='center', va='center', style='italic')

    # Arrow to signature
    arrow3 = FancyArrowPatch((2.5, 2.5), (2.5, 1.9),
                             arrowstyle='->', mutation_scale=20,
                             linewidth=2, color=MLPURPLE)
    ax.add_patch(arrow3)

    # Digital Signature
    sig_box = FancyBboxPatch((1.5, 1.1), 2, 0.8,
                              boxstyle="round,pad=0.1",
                              edgecolor=MLGREEN, facecolor='#E6FFE6',
                              linewidth=2)
    ax.add_patch(sig_box)
    ax.text(2.5, 1.7, 'Digital Signature', fontsize=10, ha='center', va='center', fontweight='bold')
    ax.text(2.5, 1.35, 'Proves ownership\nwithout revealing key', fontsize=8, ha='center', va='center')

    # ===== VERIFICATION PROCESS (RIGHT SIDE) =====
    ax.text(7.5, 5, 'VERIFICATION', fontsize=14, ha='center', fontweight='bold',
            color=MLGREEN, bbox=dict(boxstyle='round', facecolor='#E6FFE6'))

    # Signature (copy from left)
    sig_box2 = FancyBboxPatch((6.5, 3.8), 2, 0.5,
                               boxstyle="round,pad=0.05",
                               edgecolor=MLGREEN, facecolor='#E6FFE6',
                               linewidth=2)
    ax.add_patch(sig_box2)
    ax.text(7.5, 4.15, 'Signature', fontsize=9, ha='center', va='center', fontweight='bold')
    ax.text(7.5, 3.95, '(from sender)', fontsize=7, ha='center', va='center', style='italic')

    # Message (copy)
    msg_box2 = FancyBboxPatch((6.5, 3.1), 2, 0.5,
                               boxstyle="round,pad=0.05",
                               edgecolor=MLBLUE, facecolor='lightblue',
                               linewidth=2)
    ax.add_patch(msg_box2)
    ax.text(7.5, 3.45, 'Message', fontsize=9, ha='center', va='center', fontweight='bold')
    ax.text(7.5, 3.25, '(transaction)', fontsize=7, ha='center', va='center', style='italic')

    # Public Key
    pub_box = FancyBboxPatch((6.5, 2.4), 2, 0.5,
                              boxstyle="round,pad=0.05",
                              edgecolor=MLBLUE, facecolor='#E6F2FF',
                              linewidth=2)
    ax.add_patch(pub_box)
    ax.text(7.5, 2.75, 'Public Key', fontsize=9, ha='center', va='center', fontweight='bold')
    ax.text(7.5, 2.55, '✓ Can share', fontsize=7, ha='center', va='center', style='italic')

    # Arrows to verification
    arrow4 = FancyArrowPatch((7.5, 3.8), (7.5, 2.3),
                             arrowstyle='->', mutation_scale=20,
                             linewidth=1.5, color=MLPURPLE)
    ax.add_patch(arrow4)

    # Verification algorithm box
    verify_box = FancyBboxPatch((6.5, 1.5), 2, 0.7,
                                 boxstyle="round,pad=0.1",
                                 edgecolor=MLGREEN, facecolor='#E6FFE6',
                                 linewidth=2)
    ax.add_patch(verify_box)
    ax.text(7.5, 2.05, 'ECDSA Verify', fontsize=11, ha='center', va='center', fontweight='bold')
    ax.text(7.5, 1.75, 'Verification Algorithm', fontsize=8, ha='center', va='center', style='italic')

    # Arrow to result
    arrow5 = FancyArrowPatch((7.5, 1.5), (7.5, 1.0),
                             arrowstyle='->', mutation_scale=20,
                             linewidth=2, color=MLPURPLE)
    ax.add_patch(arrow5)

    # Result
    result_box = FancyBboxPatch((6.5, 0.3), 2, 0.7,
                                 boxstyle="round,pad=0.1",
                                 edgecolor=MLGREEN, facecolor='lightgreen',
                                 linewidth=3)
    ax.add_patch(result_box)
    ax.text(7.5, 0.8, '✓ Valid', fontsize=12, ha='center', va='center', fontweight='bold', color=MLGREEN)
    ax.text(7.5, 0.5, 'or', fontsize=9, ha='center', va='center')
    ax.text(7.5, 0.35, '✗ Invalid', fontsize=10, ha='center', va='center', color=MLRED)

    # Transfer arrow from signing to verification
    transfer_arrow = FancyArrowPatch((3.5, 1.5), (6.5, 4.0),
                                     arrowstyle='->', mutation_scale=25,
                                     linewidth=2, color=MLPURPLE, linestyle='dashed')
    ax.add_patch(transfer_arrow)
    ax.text(5, 3, 'Broadcast to\nnetwork', fontsize=8, ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    # Key properties at bottom
    properties = (
        'Key Properties:\n'
        '• Only private key holder can create valid signature\n'
        '• Anyone with public key can verify signature\n'
        '• Signature is unique to both message and private key\n'
        '• Tampering with message invalidates signature'
    )
    ax.text(5, -0.3, properties,
            fontsize=8, ha='center', va='top',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.6))

    plt.tight_layout()
    return fig

def main():
    """Generate and save the digital signature flow chart."""
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(os.path.abspath(__file__))

    # Generate chart
    fig = create_digital_signature_flow()

    # Save as PDF
    output_path = os.path.join(output_dir, '04_digital_signature_flow.pdf')
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
