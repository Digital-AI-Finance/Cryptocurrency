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
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'ERC-20 transfer() Flow',
        ha='center', va='top', fontsize=18, fontweight='bold', color=MLBLUE)

# Initial state - Sender and Receiver accounts
sender_y = 7.5
receiver_y = 7.5

# Sender account (before)
ax.text(1.5, 8.2, 'Sender Account', ha='center', va='center',
        fontsize=11, fontweight='bold', color=MLBLUE)
sender_box = FancyBboxPatch((0.5, sender_y - 0.4), 2, 0.8,
                            boxstyle="round,pad=0.1",
                            edgecolor=MLBLUE, facecolor=MLBLUE,
                            linewidth=2, alpha=0.3)
ax.add_patch(sender_box)
ax.text(1.5, sender_y, 'Balance: 100', ha='center', va='center',
        fontsize=10, fontweight='bold', family='monospace')

# Receiver account (before)
ax.text(8.5, 8.2, 'Receiver Account', ha='center', va='center',
        fontsize=11, fontweight='bold', color=MLGREEN)
receiver_box = FancyBboxPatch((7.5, receiver_y - 0.4), 2, 0.8,
                              boxstyle="round,pad=0.1",
                              edgecolor=MLGREEN, facecolor=MLGREEN,
                              linewidth=2, alpha=0.3)
ax.add_patch(receiver_box)
ax.text(8.5, receiver_y, 'Balance: 50', ha='center', va='center',
        fontsize=10, fontweight='bold', family='monospace')

# Step 1: Check balance
step1_y = 6
step_box_1 = FancyBboxPatch((0.5, step1_y - 0.3), 4, 0.6,
                            boxstyle="round,pad=0.05",
                            edgecolor=MLPURPLE, facecolor='white',
                            linewidth=2)
ax.add_patch(step_box_1)
ax.text(0.8, step1_y, '1', ha='center', va='center',
        fontsize=12, fontweight='bold', color='white',
        bbox=dict(boxstyle='circle', facecolor=MLPURPLE))
ax.text(2.5, step1_y, 'require(balance[sender] >= amount)',
        ha='center', va='center', fontsize=9, family='monospace',
        fontweight='bold', color=MLPURPLE)

# Arrow from sender to step 1
arrow1 = FancyArrowPatch((1.5, sender_y - 0.4), (1.5, step1_y + 0.3),
                         arrowstyle='->', mutation_scale=20,
                         color=MLPURPLE, linewidth=2)
ax.add_patch(arrow1)

# Step 2: Debit sender
step2_y = 4.8
step_box_2 = FancyBboxPatch((0.5, step2_y - 0.3), 4, 0.6,
                            boxstyle="round,pad=0.05",
                            edgecolor=MLRED, facecolor='white',
                            linewidth=2)
ax.add_patch(step_box_2)
ax.text(0.8, step2_y, '2', ha='center', va='center',
        fontsize=12, fontweight='bold', color='white',
        bbox=dict(boxstyle='circle', facecolor=MLRED))
ax.text(2.5, step2_y, 'balance[sender] -= amount',
        ha='center', va='center', fontsize=9, family='monospace',
        fontweight='bold', color=MLRED)

# Arrow step 1 to step 2
arrow2 = FancyArrowPatch((2.5, step1_y - 0.35), (2.5, step2_y + 0.35),
                         arrowstyle='->', mutation_scale=20,
                         color='gray', linewidth=2)
ax.add_patch(arrow2)

# Step 3: Credit receiver
step3_y = 3.6
step_box_3 = FancyBboxPatch((5.5, step3_y - 0.3), 4, 0.6,
                            boxstyle="round,pad=0.05",
                            edgecolor=MLGREEN, facecolor='white',
                            linewidth=2)
ax.add_patch(step_box_3)
ax.text(5.8, step3_y, '3', ha='center', va='center',
        fontsize=12, fontweight='bold', color='white',
        bbox=dict(boxstyle='circle', facecolor=MLGREEN))
ax.text(7.5, step3_y, 'balance[receiver] += amount',
        ha='center', va='center', fontsize=9, family='monospace',
        fontweight='bold', color=MLGREEN)

# Arrow step 2 to step 3
arrow3 = FancyArrowPatch((4.5, step2_y - 0.15), (5.5, step3_y + 0.15),
                         arrowstyle='->', mutation_scale=20,
                         color='gray', linewidth=2, linestyle='--')
ax.add_patch(arrow3)
ax.text(5, step2_y - 0.6, 'Transfer 25 tokens', ha='center', va='center',
        fontsize=9, color=MLORANGE, fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='white', edgecolor=MLORANGE))

# Step 4: Emit event
step4_y = 2.4
step_box_4 = FancyBboxPatch((2, step4_y - 0.3), 6, 0.6,
                            boxstyle="round,pad=0.05",
                            edgecolor=MLORANGE, facecolor='white',
                            linewidth=2, linestyle='--')
ax.add_patch(step_box_4)
ax.text(2.3, step4_y, '4', ha='center', va='center',
        fontsize=12, fontweight='bold', color='white',
        bbox=dict(boxstyle='circle', facecolor=MLORANGE))
ax.text(5, step4_y, 'emit Transfer(sender, receiver, amount)',
        ha='center', va='center', fontsize=9, family='monospace',
        fontweight='bold', color=MLORANGE)

# Arrow from step 3 to step 4
arrow4 = FancyArrowPatch((7.5, step3_y - 0.35), (5, step4_y + 0.35),
                         arrowstyle='->', mutation_scale=20,
                         color='gray', linewidth=2)
ax.add_patch(arrow4)

# Final state - Updated balances
final_y = 0.8

# Sender account (after)
sender_final_box = FancyBboxPatch((0.5, final_y - 0.4), 2, 0.8,
                                  boxstyle="round,pad=0.1",
                                  edgecolor=MLBLUE, facecolor=MLBLUE,
                                  linewidth=2, alpha=0.6)
ax.add_patch(sender_final_box)
ax.text(1.5, final_y + 0.3, 'Sender (After)', ha='center', va='center',
        fontsize=10, fontweight='bold', color=MLBLUE)
ax.text(1.5, final_y, 'Balance: 75', ha='center', va='center',
        fontsize=10, fontweight='bold', family='monospace', color='white')

# Receiver account (after)
receiver_final_box = FancyBboxPatch((7.5, final_y - 0.4), 2, 0.8,
                                    boxstyle="round,pad=0.1",
                                    edgecolor=MLGREEN, facecolor=MLGREEN,
                                    linewidth=2, alpha=0.6)
ax.add_patch(receiver_final_box)
ax.text(8.5, final_y + 0.3, 'Receiver (After)', ha='center', va='center',
        fontsize=10, fontweight='bold', color=MLGREEN)
ax.text(8.5, final_y, 'Balance: 75', ha='center', va='center',
        fontsize=10, fontweight='bold', family='monospace', color='white')

plt.tight_layout()

# Save
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, '02_token_flow.pdf')
plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
plt.close()
