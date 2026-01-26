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
ax.text(5, 9.5, 'ERC-20 Token Deployment Workflow',
        ha='center', va='top', fontsize=18, fontweight='bold', color=MLBLUE)

# Define steps
steps = [
    {
        'num': '1',
        'title': 'Write & Compile',
        'content': ['Write Solidity contract', 'Compile to bytecode', 'Generate ABI'],
        'color': MLPURPLE,
        'icon': '{ }'
    },
    {
        'num': '2',
        'title': 'Deploy to Network',
        'content': ['Choose network (mainnet/testnet)', 'Send deployment transaction', 'Pay gas fees'],
        'color': MLORANGE,
        'icon': '↑'
    },
    {
        'num': '3',
        'title': 'Get Contract Address',
        'content': ['Transaction mined', 'Contract assigned address', 'Save address for reference'],
        'color': MLBLUE,
        'icon': '#'
    },
    {
        'num': '4',
        'title': 'Verify on Explorer',
        'content': ['Submit source code', 'Match with bytecode', 'Enable public interaction'],
        'color': MLGREEN,
        'icon': '✓'
    },
    {
        'num': '5',
        'title': 'Interact & Use',
        'content': ['Call contract functions', 'Transfer tokens', 'Monitor events'],
        'color': MLRED,
        'icon': '⟳'
    }
]

# Layout parameters
start_y = 8
step_height = 1.3
step_spacing = 0.2
total_step_height = step_height + step_spacing

# Draw steps
for i, step in enumerate(steps):
    y_pos = start_y - i * total_step_height

    # Step number circle
    circle = Circle((0.8, y_pos - step_height/2 + 0.2), 0.25,
                    color=step['color'], alpha=0.8, ec=step['color'], linewidth=2)
    ax.add_patch(circle)
    ax.text(0.8, y_pos - step_height/2 + 0.2, step['num'],
            ha='center', va='center', fontsize=14, fontweight='bold', color='white')

    # Step box
    step_box = FancyBboxPatch((1.5, y_pos - step_height), 8, step_height,
                              boxstyle="round,pad=0.1",
                              edgecolor=step['color'], facecolor='white',
                              linewidth=2.5)
    ax.add_patch(step_box)

    # Icon
    ax.text(2, y_pos - step_height/2 + 0.2, step['icon'],
            ha='center', va='center', fontsize=20, color=step['color'],
            fontweight='bold')

    # Title
    ax.text(2.8, y_pos - 0.2, step['title'],
            ha='left', va='center', fontsize=12, fontweight='bold',
            color=step['color'])

    # Content items
    content_start_y = y_pos - 0.5
    for j, item in enumerate(step['content']):
        item_y = content_start_y - j * 0.25
        ax.text(3, item_y, f"• {item}",
                ha='left', va='center', fontsize=8, color='black')

    # Arrow to next step (except for last step)
    if i < len(steps) - 1:
        arrow = FancyArrowPatch((0.8, y_pos - step_height - 0.1),
                                (0.8, y_pos - step_height - step_spacing + 0.1),
                                arrowstyle='->', mutation_scale=20,
                                color='gray', linewidth=2.5)
        ax.add_patch(arrow)

# Add network options box
network_y = 0.8
network_box = FancyBboxPatch((1.5, network_y - 0.5), 7, 0.9,
                             boxstyle="round,pad=0.1",
                             edgecolor=MLBLUE, facecolor='lightblue',
                             linewidth=2, alpha=0.3)
ax.add_patch(network_box)

ax.text(2, network_y + 0.15, 'Common Networks:',
        ha='left', va='center', fontsize=10, fontweight='bold', color=MLBLUE)

networks = [
    ('Ethereum Mainnet', 'Production (expensive gas)'),
    ('Sepolia/Goerli', 'Testing (free testnet ETH)'),
    ('Polygon/Arbitrum', 'L2 (cheaper gas)')
]

for i, (name, desc) in enumerate(networks):
    x_pos = 2 + i * 2.3
    ax.text(x_pos, network_y - 0.15, name,
            ha='left', va='center', fontsize=8, fontweight='bold', color=MLBLUE)
    ax.text(x_pos, network_y - 0.3, desc,
            ha='left', va='center', fontsize=7, color='gray', style='italic')

plt.tight_layout()

# Save
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, '04_deployment_steps.pdf')
plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
print(f"Chart saved to {output_path}")

# Add PNG export for GitHub Pages
output_png = output_path.replace('.pdf', '.png')
plt.savefig(output_png, dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none', format='png')
print(f"PNG saved to: {output_png}")

plt.close()
