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
ax.text(5, 9.5, 'ERC-20 Token Standard Interface',
        ha='center', va='top', fontsize=18, fontweight='bold', color=MLBLUE)

# Main container for ERC-20 interface
interface_box = FancyBboxPatch((0.5, 1), 9, 7.5,
                               boxstyle="round,pad=0.1",
                               edgecolor=MLBLUE, facecolor='white',
                               linewidth=2.5, zorder=1)
ax.add_patch(interface_box)

ax.text(5, 8, 'ERC-20 Interface',
        ha='center', va='center', fontsize=14, fontweight='bold', color=MLBLUE)

# Functions section
functions_y_start = 7
function_height = 0.5
function_spacing = 0.7

functions = [
    ('totalSupply()', 'Returns total token supply', MLGREEN),
    ('balanceOf(address)', 'Returns balance of address', MLGREEN),
    ('transfer(address, uint256)', 'Transfer tokens to address', MLORANGE),
    ('approve(address, uint256)', 'Approve spender allowance', MLPURPLE),
    ('allowance(address, address)', 'Check approved amount', MLPURPLE),
    ('transferFrom(address, address, uint256)', 'Transfer on behalf', MLORANGE)
]

ax.text(1, functions_y_start + 0.3, 'Required Functions (6):',
        ha='left', va='center', fontsize=12, fontweight='bold', color=MLBLUE)

for i, (func_name, description, color) in enumerate(functions):
    y_pos = functions_y_start - (i + 1) * function_spacing

    # Function box
    func_box = FancyBboxPatch((1, y_pos - function_height/2), 3.5, function_height,
                              boxstyle="round,pad=0.05",
                              edgecolor=color, facecolor=color,
                              linewidth=1.5, alpha=0.3)
    ax.add_patch(func_box)

    # Function name
    ax.text(2.75, y_pos, func_name,
            ha='center', va='center', fontsize=9,
            fontweight='bold', color=color, family='monospace')

    # Description
    ax.text(4.8, y_pos, description,
            ha='left', va='center', fontsize=8, color='black')

# Events section
events_y = 2
ax.text(1, events_y + 0.5, 'Required Events (2):',
        ha='left', va='center', fontsize=12, fontweight='bold', color=MLBLUE)

events = [
    ('Transfer(from, to, value)', 'Emitted on token transfer', MLORANGE),
    ('Approval(owner, spender, value)', 'Emitted on approval', MLPURPLE)
]

for i, (event_name, description, color) in enumerate(events):
    y_pos = events_y - i * 0.6

    # Event box
    event_box = FancyBboxPatch((1, y_pos - 0.25), 3.5, 0.4,
                               boxstyle="round,pad=0.05",
                               edgecolor=color, facecolor='white',
                               linewidth=2, linestyle='--')
    ax.add_patch(event_box)

    # Event name
    ax.text(2.75, y_pos, event_name,
            ha='center', va='center', fontsize=9,
            fontweight='bold', color=color, family='monospace')

    # Description
    ax.text(4.8, y_pos, description,
            ha='left', va='center', fontsize=8, color='black')

# Add legend for categories
legend_y = 0.5
legend_items = [
    (MLGREEN, 'Query Functions'),
    (MLORANGE, 'Transfer Functions'),
    (MLPURPLE, 'Approval Functions')
]

ax.text(1, legend_y + 0.3, 'Function Categories:',
        ha='left', va='center', fontsize=10, fontweight='bold', color=MLBLUE)

for i, (color, label) in enumerate(legend_items):
    x_pos = 1 + i * 2.8
    circle = plt.Circle((x_pos + 0.5, legend_y), 0.1, color=color, alpha=0.5)
    ax.add_patch(circle)
    ax.text(x_pos + 0.8, legend_y, label,
            ha='left', va='center', fontsize=8, color=color)

plt.tight_layout()

# Save
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, '01_erc20_interface.pdf')
plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")
plt.close()
