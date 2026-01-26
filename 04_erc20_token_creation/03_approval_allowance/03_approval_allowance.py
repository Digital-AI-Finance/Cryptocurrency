import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
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
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'Approval & Allowance Pattern (DEX Trading)',
        ha='center', va='top', fontsize=18, fontweight='bold', color=MLBLUE)

# Three actors
owner_x, owner_y = 1.5, 7.5
dex_x, dex_y = 5, 7.5
recipient_x, recipient_y = 8.5, 7.5

# Owner
owner_circle = Circle((owner_x, owner_y), 0.4, color=MLBLUE, alpha=0.3, ec=MLBLUE, linewidth=2.5)
ax.add_patch(owner_circle)
ax.text(owner_x, owner_y, 'O', ha='center', va='center',
        fontsize=14, fontweight='bold', color=MLBLUE)
ax.text(owner_x, owner_y - 0.7, 'Token Owner', ha='center', va='top',
        fontsize=10, fontweight='bold', color=MLBLUE)
ax.text(owner_x, owner_y - 1, 'Balance: 1000', ha='center', va='top',
        fontsize=8, family='monospace')

# DEX/Spender
dex_circle = Circle((dex_x, dex_y), 0.4, color=MLPURPLE, alpha=0.3, ec=MLPURPLE, linewidth=2.5)
ax.add_patch(dex_circle)
ax.text(dex_x, dex_y, 'D', ha='center', va='center',
        fontsize=14, fontweight='bold', color=MLPURPLE)
ax.text(dex_x, dex_y - 0.7, 'DEX (Spender)', ha='center', va='top',
        fontsize=10, fontweight='bold', color=MLPURPLE)
ax.text(dex_x, dex_y - 1, 'Allowance: 0 → 500', ha='center', va='top',
        fontsize=8, family='monospace')

# Recipient
recipient_circle = Circle((recipient_x, recipient_y), 0.4, color=MLGREEN, alpha=0.3, ec=MLGREEN, linewidth=2.5)
ax.add_patch(recipient_circle)
ax.text(recipient_x, recipient_y, 'R', ha='center', va='center',
        fontsize=14, fontweight='bold', color=MLGREEN)
ax.text(recipient_x, recipient_y - 0.7, 'Recipient', ha='center', va='top',
        fontsize=10, fontweight='bold', color=MLGREEN)
ax.text(recipient_x, recipient_y - 1, 'Balance: 0', ha='center', va='top',
        fontsize=8, family='monospace')

# Phase 1: approve()
phase1_y = 5.5
ax.text(0.5, phase1_y + 0.5, 'Phase 1: Approval',
        ha='left', va='center', fontsize=12, fontweight='bold', color=MLPURPLE)

# approve() call
approve_box = FancyBboxPatch((1, phase1_y - 0.25), 3.5, 0.5,
                             boxstyle="round,pad=0.05",
                             edgecolor=MLPURPLE, facecolor='white',
                             linewidth=2)
ax.add_patch(approve_box)
ax.text(2.75, phase1_y, 'approve(DEX, 500)',
        ha='center', va='center', fontsize=9, family='monospace',
        fontweight='bold', color=MLPURPLE)

# Arrow from owner to DEX
arrow1 = FancyArrowPatch((2, owner_y - 0.5), (4.5, phase1_y + 0.15),
                         arrowstyle='->', mutation_scale=20,
                         color=MLPURPLE, linewidth=2.5, linestyle='--')
ax.add_patch(arrow1)

# Allowance update
allowance_box = FancyBboxPatch((5, phase1_y - 0.25), 3, 0.5,
                               boxstyle="round,pad=0.05",
                               edgecolor=MLPURPLE, facecolor=MLPURPLE,
                               linewidth=2, alpha=0.3)
ax.add_patch(allowance_box)
ax.text(6.5, phase1_y, 'allowance[O][D] = 500',
        ha='center', va='center', fontsize=9, family='monospace',
        fontweight='bold', color=MLPURPLE)

# Emit Approval event
event1_box = FancyBboxPatch((1, phase1_y - 0.9), 4, 0.4,
                            boxstyle="round,pad=0.05",
                            edgecolor=MLORANGE, facecolor='white',
                            linewidth=1.5, linestyle='--')
ax.add_patch(event1_box)
ax.text(3, phase1_y - 0.7, 'emit Approval(Owner, DEX, 500)',
        ha='center', va='center', fontsize=8, family='monospace',
        color=MLORANGE, style='italic')

# Phase 2: transferFrom()
phase2_y = 3.5
ax.text(0.5, phase2_y + 0.5, 'Phase 2: Transfer',
        ha='left', va='center', fontsize=12, fontweight='bold', color=MLGREEN)

# transferFrom() call
transfer_box = FancyBboxPatch((1, phase2_y - 0.25), 4.5, 0.5,
                              boxstyle="round,pad=0.05",
                              edgecolor=MLGREEN, facecolor='white',
                              linewidth=2)
ax.add_patch(transfer_box)
ax.text(3.25, phase2_y, 'transferFrom(Owner, Recipient, 100)',
        ha='center', va='center', fontsize=9, family='monospace',
        fontweight='bold', color=MLGREEN)

# Check allowance
check_box = FancyBboxPatch((1, phase2_y - 1), 4.5, 0.5,
                           boxstyle="round,pad=0.05",
                           edgecolor=MLRED, facecolor='white',
                           linewidth=2)
ax.add_patch(check_box)
ax.text(3.25, phase2_y - 0.75, 'require(allowance[O][D] >= 100)',
        ha='center', va='center', fontsize=8, family='monospace',
        fontweight='bold', color=MLRED)

# Arrow from DEX initiating transfer
arrow2 = FancyArrowPatch((5, dex_y - 0.5), (3.5, phase2_y + 0.15),
                         arrowstyle='->', mutation_scale=20,
                         color=MLGREEN, linewidth=2.5)
ax.add_patch(arrow2)

# Update balances
balance_update_y = 1.8
balance_box = FancyBboxPatch((5.5, balance_update_y - 0.25), 4, 0.5,
                             boxstyle="round,pad=0.05",
                             edgecolor=MLGREEN, facecolor=MLGREEN,
                             linewidth=2, alpha=0.3)
ax.add_patch(balance_box)
ax.text(7.5, balance_update_y, 'balance[O] -= 100, balance[R] += 100',
        ha='center', va='center', fontsize=8, family='monospace',
        fontweight='bold', color=MLGREEN)

# Arrow from check to balance update
arrow3 = FancyArrowPatch((3.25, phase2_y - 1.05), (6, balance_update_y + 0.2),
                         arrowstyle='->', mutation_scale=20,
                         color='gray', linewidth=2, linestyle='--')
ax.add_patch(arrow3)

# Decrease allowance
allowance_update_y = 1.1
allowance_update_box = FancyBboxPatch((1, allowance_update_y - 0.25), 4, 0.5,
                                      boxstyle="round,pad=0.05",
                                      edgecolor=MLPURPLE, facecolor=MLPURPLE,
                                      linewidth=2, alpha=0.6)
ax.add_patch(allowance_update_box)
ax.text(3, allowance_update_y, 'allowance[O][D] = 400',
        ha='center', va='center', fontsize=9, family='monospace',
        fontweight='bold', color='white')

# Emit Transfer event
event2_box = FancyBboxPatch((5.5, allowance_update_y - 0.25), 4, 0.5,
                            boxstyle="round,pad=0.05",
                            edgecolor=MLORANGE, facecolor='white',
                            linewidth=1.5, linestyle='--')
ax.add_patch(event2_box)
ax.text(7.5, allowance_update_y, 'emit Transfer(O, R, 100)',
        ha='center', va='center', fontsize=8, family='monospace',
        color=MLORANGE, style='italic')

# Summary box
summary_y = 0.3
summary_text = 'DEX can spend up to approved amount on behalf of owner'
ax.text(5, summary_y, summary_text,
        ha='center', va='center', fontsize=9, color=MLBLUE,
        style='italic',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor=MLBLUE))

plt.tight_layout()

# Save
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, '03_approval_allowance.pdf')
plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")

# Add PNG export for GitHub Pages
output_png = output_path.replace('.pdf', '.png')
plt.savefig(output_png, dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none', format='png')
print(f"PNG saved to: {output_png}")

plt.close()
