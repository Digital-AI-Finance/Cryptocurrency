#!/usr/bin/env python3
"""
Wallet Architecture Components Diagram
Shows: seed phrase, private key, public key, address, balance
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import os

# Color palette
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLPURPLE = '#3333B2'

def create_wallet_architecture():
    """Create wallet architecture components diagram."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Title
    ax.text(5, 5.8, 'Bitcoin Wallet Architecture',
            fontsize=20, fontweight='bold', ha='center', va='top')
    ax.text(5, 5.5, 'Hierarchical Deterministic (HD) Wallet Components',
            fontsize=11, ha='center', va='top', style='italic')

    # Layer 1: Seed Phrase (top)
    seed_box = FancyBboxPatch((1, 4.7), 8, 0.6,
                               boxstyle="round,pad=0.1",
                               edgecolor=MLPURPLE, facecolor='#E6D5F5',
                               linewidth=3)
    ax.add_patch(seed_box)
    ax.text(5, 5.15, 'Seed Phrase (Mnemonic)', fontsize=12, ha='center', va='center', fontweight='bold')
    ax.text(5, 4.9, '12 or 24 words - Master backup for entire wallet', fontsize=9, ha='center', va='center', style='italic')
    ax.text(5, 4.5, 'e.g., "witch collapse practice feed shame open despair creek road again ice least"',
            fontsize=7, ha='center', va='top', family='monospace',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

    # Arrow down
    arrow1 = FancyArrowPatch((5, 4.7), (5, 4.3),
                             arrowstyle='->', mutation_scale=25,
                             linewidth=2, color=MLPURPLE)
    ax.add_patch(arrow1)
    ax.text(5.5, 4.5, 'BIP39/BIP32', fontsize=8, style='italic')

    # Layer 2: Master Private Key
    master_box = FancyBboxPatch((1.5, 3.5), 3, 0.7,
                                 boxstyle="round,pad=0.1",
                                 edgecolor=MLRED, facecolor='#FFE6E6',
                                 linewidth=2)
    ax.add_patch(master_box)
    ax.text(3, 3.95, 'Master Private Key', fontsize=11, ha='center', va='center', fontweight='bold', color=MLRED)
    ax.text(3, 3.7, '🔒 Never exposed', fontsize=8, ha='center', va='center', style='italic')

    # Layer 2: Derivation path
    deriv_box = FancyBboxPatch((5.5, 3.5), 3, 0.7,
                                boxstyle="round,pad=0.1",
                                edgecolor=MLORANGE, facecolor='#FFE5CC',
                                linewidth=2)
    ax.add_patch(deriv_box)
    ax.text(7, 3.95, 'Derivation Path', fontsize=11, ha='center', va='center', fontweight='bold')
    ax.text(7, 3.7, "m/44'/0'/0'/0/0", fontsize=9, ha='center', va='center', family='monospace')

    # Arrows to derived keys
    arrow2a = FancyArrowPatch((3, 3.5), (2.5, 3.0),
                              arrowstyle='->', mutation_scale=20,
                              linewidth=1.5, color=MLPURPLE)
    ax.add_patch(arrow2a)

    arrow2b = FancyArrowPatch((7, 3.5), (7.5, 3.0),
                              arrowstyle='->', mutation_scale=20,
                              linewidth=1.5, color=MLPURPLE)
    ax.add_patch(arrow2b)

    # Layer 3: Child Keys (multiple accounts)
    # Account 0
    acc0_label = ax.text(1, 2.8, 'Account 0', fontsize=9, ha='center', fontweight='bold')

    pk0_box = FancyBboxPatch((0.3, 2.0), 1.4, 0.5,
                              boxstyle="round,pad=0.05",
                              edgecolor=MLRED, facecolor='#FFE6E6',
                              linewidth=1.5)
    ax.add_patch(pk0_box)
    ax.text(1, 2.35, 'Private Key', fontsize=8, ha='center', va='center', fontweight='bold')
    ax.text(1, 2.15, '🔒', fontsize=9, ha='center', va='center')

    arrow3a = FancyArrowPatch((1, 2.0), (1, 1.6),
                              arrowstyle='->', mutation_scale=15,
                              linewidth=1.2, color=MLPURPLE)
    ax.add_patch(arrow3a)

    pub0_box = FancyBboxPatch((0.3, 1.0), 1.4, 0.5,
                               boxstyle="round,pad=0.05",
                               edgecolor=MLBLUE, facecolor='#E6F2FF',
                               linewidth=1.5)
    ax.add_patch(pub0_box)
    ax.text(1, 1.35, 'Public Key', fontsize=8, ha='center', va='center', fontweight='bold')
    ax.text(1, 1.15, '✓', fontsize=9, ha='center', va='center')

    arrow4a = FancyArrowPatch((1, 1.0), (1, 0.6),
                              arrowstyle='->', mutation_scale=15,
                              linewidth=1.2, color=MLPURPLE)
    ax.add_patch(arrow4a)

    addr0_box = FancyBboxPatch((0.3, 0.0), 1.4, 0.5,
                                boxstyle="round,pad=0.05",
                                edgecolor=MLGREEN, facecolor='#E6FFE6',
                                linewidth=1.5)
    ax.add_patch(addr0_box)
    ax.text(1, 0.35, 'Address', fontsize=8, ha='center', va='center', fontweight='bold')
    ax.text(1, 0.15, '1A1zP1...', fontsize=6, ha='center', va='center', family='monospace')

    # Account 1
    acc1_label = ax.text(3, 2.8, 'Account 1', fontsize=9, ha='center', fontweight='bold')

    pk1_box = FancyBboxPatch((2.3, 2.0), 1.4, 0.5,
                              boxstyle="round,pad=0.05",
                              edgecolor=MLRED, facecolor='#FFE6E6',
                              linewidth=1.5)
    ax.add_patch(pk1_box)
    ax.text(3, 2.35, 'Private Key', fontsize=8, ha='center', va='center', fontweight='bold')
    ax.text(3, 2.15, '🔒', fontsize=9, ha='center', va='center')

    arrow3b = FancyArrowPatch((3, 2.0), (3, 1.6),
                              arrowstyle='->', mutation_scale=15,
                              linewidth=1.2, color=MLPURPLE)
    ax.add_patch(arrow3b)

    pub1_box = FancyBboxPatch((2.3, 1.0), 1.4, 0.5,
                               boxstyle="round,pad=0.05",
                               edgecolor=MLBLUE, facecolor='#E6F2FF',
                               linewidth=1.5)
    ax.add_patch(pub1_box)
    ax.text(3, 1.35, 'Public Key', fontsize=8, ha='center', va='center', fontweight='bold')
    ax.text(3, 1.15, '✓', fontsize=9, ha='center', va='center')

    arrow4b = FancyArrowPatch((3, 1.0), (3, 0.6),
                              arrowstyle='->', mutation_scale=15,
                              linewidth=1.2, color=MLPURPLE)
    ax.add_patch(arrow4b)

    addr1_box = FancyBboxPatch((2.3, 0.0), 1.4, 0.5,
                                boxstyle="round,pad=0.05",
                                edgecolor=MLGREEN, facecolor='#E6FFE6',
                                linewidth=1.5)
    ax.add_patch(addr1_box)
    ax.text(3, 0.35, 'Address', fontsize=8, ha='center', va='center', fontweight='bold')
    ax.text(3, 0.15, '3J98t1...', fontsize=6, ha='center', va='center', family='monospace')

    # Account N (...)
    ax.text(5, 2.8, '...', fontsize=14, ha='center', fontweight='bold')
    ax.text(5, 2.3, 'Multiple\nAccounts', fontsize=8, ha='center', style='italic')

    # Balance/Blockchain interaction (right side)
    blockchain_box = FancyBboxPatch((6.5, 1.8), 3, 1.2,
                                     boxstyle="round,pad=0.1",
                                     edgecolor=MLORANGE, facecolor='#FFF5E6',
                                     linewidth=2)
    ax.add_patch(blockchain_box)
    ax.text(8, 2.75, 'Blockchain Interaction', fontsize=11, ha='center', va='center', fontweight='bold')

    # Balance info
    balance_text = (
        'Balance Calculation:\n'
        '• Query blockchain for UTXOs\n'
        '• Sum unspent outputs\n'
        '• Display to user'
    )
    ax.text(8, 2.25, balance_text, fontsize=8, ha='center', va='center')

    # Connection arrows
    arrow_bc1 = FancyArrowPatch((1.7, 0.25), (6.5, 2.2),
                                arrowstyle='<->', mutation_scale=15,
                                linewidth=1, color=MLGREEN, linestyle='dashed')
    ax.add_patch(arrow_bc1)

    arrow_bc2 = FancyArrowPatch((3.7, 0.25), (6.5, 2.0),
                                arrowstyle='<->', mutation_scale=15,
                                linewidth=1, color=MLGREEN, linestyle='dashed')
    ax.add_patch(arrow_bc2)

    # Wallet functions box
    functions_box = FancyBboxPatch((6.5, 0.2), 3, 1.3,
                                    boxstyle="round,pad=0.1",
                                    edgecolor=MLBLUE, facecolor='#E6F2FF',
                                    linewidth=2)
    ax.add_patch(functions_box)
    ax.text(8, 1.3, 'Wallet Functions', fontsize=11, ha='center', va='center', fontweight='bold')

    functions_text = (
        '📤 Send: Sign tx with private key\n'
        '📥 Receive: Generate new address\n'
        '💰 Balance: Query blockchain\n'
        '📜 History: Fetch transactions\n'
        '🔄 Backup: Export seed phrase'
    )
    ax.text(8, 0.7, functions_text, fontsize=8, ha='center', va='center')

    # Security note at bottom
    security_note = (
        '⚠️ Security: Never share seed phrase or private keys!\n'
        'Whoever has the seed can control ALL funds in the wallet.'
    )
    ax.text(5, -0.4, security_note,
            fontsize=8, ha='center', va='top',
            bbox=dict(boxstyle='round', facecolor='#FFE6E6', alpha=0.8, edgecolor=MLRED, linewidth=2))

    plt.tight_layout()
    return fig

def main():
    """Generate and save the wallet architecture diagram."""
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(os.path.abspath(__file__))

    # Generate chart
    fig = create_wallet_architecture()

    # Save as PDF
    output_path = os.path.join(output_dir, '05_wallet_architecture.pdf')
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
