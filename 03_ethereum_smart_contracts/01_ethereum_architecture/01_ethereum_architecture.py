#!/usr/bin/env python3
"""
Ethereum Virtual Machine (EVM) Architecture Chart
Shows: accounts, state, storage, bytecode execution
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

# Color palette
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLPURPLE = '#3333B2'

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Title
ax.text(5, 5.5, 'Ethereum Virtual Machine (EVM) Architecture',
        ha='center', va='top', fontsize=18, fontweight='bold')

# EVM Container
evm_box = FancyBboxPatch((0.5, 1), 9, 3.8,
                         boxstyle="round,pad=0.1",
                         edgecolor=MLBLUE, facecolor='#E6F2FF',
                         linewidth=2.5, zorder=1)
ax.add_patch(evm_box)
ax.text(5, 4.6, 'Ethereum Virtual Machine',
        ha='center', va='center', fontsize=14, fontweight='bold', color=MLBLUE)

# Accounts Section (left side)
accounts_box = FancyBboxPatch((0.8, 2.8), 2.2, 1.5,
                             boxstyle="round,pad=0.05",
                             edgecolor=MLGREEN, facecolor='#E8F5E9',
                             linewidth=2, zorder=2)
ax.add_patch(accounts_box)
ax.text(1.9, 4.15, 'Accounts', ha='center', va='center',
        fontsize=11, fontweight='bold', color=MLGREEN)

# EOA (Externally Owned Account)
eoa_box = FancyBboxPatch((0.9, 3.4), 1.9, 0.5,
                        boxstyle="round,pad=0.03",
                        edgecolor=MLGREEN, facecolor='white',
                        linewidth=1.5, zorder=3)
ax.add_patch(eoa_box)
ax.text(1.85, 3.65, 'EOA', ha='center', va='center',
        fontsize=9, fontweight='bold')
ax.text(1.85, 3.52, '• Balance\n• Nonce', ha='center', va='center',
        fontsize=7, linespacing=1.2)

# Contract Account
contract_box = FancyBboxPatch((0.9, 2.9), 1.9, 0.5,
                             boxstyle="round,pad=0.03",
                             edgecolor=MLGREEN, facecolor='white',
                             linewidth=1.5, zorder=3)
ax.add_patch(contract_box)
ax.text(1.85, 3.15, 'Contract', ha='center', va='center',
        fontsize=9, fontweight='bold')
ax.text(1.85, 3.0, '• Balance • Nonce\n• Code • Storage',
        ha='center', va='center', fontsize=7, linespacing=1.2)

# State Section (middle-left)
state_box = FancyBboxPatch((3.3, 2.8), 2.5, 1.5,
                          boxstyle="round,pad=0.05",
                          edgecolor=MLORANGE, facecolor='#FFF3E0',
                          linewidth=2, zorder=2)
ax.add_patch(state_box)
ax.text(4.55, 4.15, 'World State', ha='center', va='center',
        fontsize=11, fontweight='bold', color=MLORANGE)

# State tree visualization
ax.text(4.55, 3.7, 'Merkle Patricia Trie', ha='center', va='center',
        fontsize=9, style='italic')
ax.text(4.55, 3.4, 'address → account', ha='center', va='center',
        fontsize=8)
ax.text(4.55, 3.15, '0x123... → {balance, nonce, ...}',
        ha='center', va='center', fontsize=7, family='monospace')
ax.text(4.55, 2.95, 'State Root Hash: 0xabc...',
        ha='center', va='center', fontsize=7, family='monospace', color=MLORANGE)

# Storage Section (middle-right)
storage_box = FancyBboxPatch((6.1, 2.8), 1.7, 1.5,
                            boxstyle="round,pad=0.05",
                            edgecolor=MLPURPLE, facecolor='#F3E5F5',
                            linewidth=2, zorder=2)
ax.add_patch(storage_box)
ax.text(6.95, 4.15, 'Storage', ha='center', va='center',
        fontsize=11, fontweight='bold', color=MLPURPLE)

# Storage details
ax.text(6.95, 3.7, 'Contract Data', ha='center', va='center',
        fontsize=9)
ax.text(6.95, 3.45, 'Key-Value Store', ha='center', va='center',
        fontsize=8, style='italic')
ax.text(6.95, 3.15, 'slot[0] → value', ha='center', va='center',
        fontsize=7, family='monospace')
ax.text(6.95, 2.95, 'Persistent', ha='center', va='center',
        fontsize=7, fontweight='bold')

# Bytecode Execution Section (right)
exec_box = FancyBboxPatch((8.0, 2.8), 1.7, 1.5,
                         boxstyle="round,pad=0.05",
                         edgecolor=MLRED, facecolor='#FFEBEE',
                         linewidth=2, zorder=2)
ax.add_patch(exec_box)
ax.text(8.85, 4.15, 'Execution', ha='center', va='center',
        fontsize=11, fontweight='bold', color=MLRED)

# Execution components
ax.text(8.85, 3.75, 'Stack', ha='center', va='center',
        fontsize=9, fontweight='bold')
ax.text(8.85, 3.5, 'Memory', ha='center', va='center',
        fontsize=9, fontweight='bold')
ax.text(8.85, 3.25, 'PC Counter', ha='center', va='center',
        fontsize=9, fontweight='bold')
ax.text(8.85, 2.95, 'Opcodes', ha='center', va='center',
        fontsize=8, style='italic')

# Bottom Flow: Transaction Processing
flow_y = 1.8

# Transaction input
tx_box = FancyBboxPatch((0.8, flow_y), 1.5, 0.5,
                       boxstyle="round,pad=0.05",
                       edgecolor=MLBLUE, facecolor='white',
                       linewidth=1.5, zorder=2)
ax.add_patch(tx_box)
ax.text(1.55, flow_y+0.25, 'Transaction', ha='center', va='center',
        fontsize=9, fontweight='bold')

# Arrow to State Update
arrow1 = FancyArrowPatch((2.3, flow_y+0.25), (3.5, flow_y+0.25),
                        arrowstyle='->', mutation_scale=20,
                        linewidth=2, color=MLBLUE)
ax.add_artist(arrow1)

# State Update
update_box = FancyBboxPatch((3.5, flow_y), 1.8, 0.5,
                           boxstyle="round,pad=0.05",
                           edgecolor=MLORANGE, facecolor='white',
                           linewidth=1.5, zorder=2)
ax.add_patch(update_box)
ax.text(4.4, flow_y+0.25, 'State Update', ha='center', va='center',
        fontsize=9, fontweight='bold')

# Arrow to Gas Consumption
arrow2 = FancyArrowPatch((5.3, flow_y+0.25), (6.3, flow_y+0.25),
                        arrowstyle='->', mutation_scale=20,
                        linewidth=2, color=MLBLUE)
ax.add_artist(arrow2)

# Gas Consumption
gas_box = FancyBboxPatch((6.3, flow_y), 1.5, 0.5,
                        boxstyle="round,pad=0.05",
                        edgecolor=MLRED, facecolor='white',
                        linewidth=1.5, zorder=2)
ax.add_patch(gas_box)
ax.text(7.05, flow_y+0.25, 'Gas Used', ha='center', va='center',
        fontsize=9, fontweight='bold')

# Arrow to Output
arrow3 = FancyArrowPatch((7.8, flow_y+0.25), (8.7, flow_y+0.25),
                        arrowstyle='->', mutation_scale=20,
                        linewidth=2, color=MLBLUE)
ax.add_artist(arrow3)

# Output/Receipt
receipt_box = FancyBboxPatch((8.7, flow_y), 0.8, 0.5,
                            boxstyle="round,pad=0.05",
                            edgecolor=MLGREEN, facecolor='white',
                            linewidth=1.5, zorder=2)
ax.add_patch(receipt_box)
ax.text(9.1, flow_y+0.25, 'Receipt', ha='center', va='center',
        fontsize=9, fontweight='bold')

# Key Properties at bottom
ax.text(5, 1.2, 'Key Properties:', ha='center', va='center',
        fontsize=10, fontweight='bold')
props_text = ('• Deterministic: Same input → Same output\n'
              '• Isolated: No external dependencies\n'
              '• Turing-complete: Can compute anything (with gas limits)')
ax.text(5, 0.6, props_text, ha='center', va='center',
        fontsize=8, linespacing=1.5)

plt.tight_layout()

# Save
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, '01_ethereum_architecture.pdf')
plt.savefig(output_path, dpi=300, bbox_inches='tight', format='pdf')
print(f"Chart saved to: {output_path}")

plt.show()
