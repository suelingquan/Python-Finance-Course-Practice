import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(14, 2.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 1)
ax.axis('off')

# 使用英文
steps = ['Data Loading', 'Data Cleaning', 'Industry Filter', 'Data Merge',
         'PE Calc', 'Outlier Remove', 'Group by Industry', 'Visualization', 'Output']

x_positions = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5]

for i, (step, x) in enumerate(zip(steps, x_positions)):
    rect = patches.FancyBboxPatch((x - 0.4, 0.35), 0.8, 0.4,
                                  boxstyle="round,pad=0.05",
                                  facecolor='lightblue',
                                  edgecolor='navy',
                                  linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x, 0.55, step, ha='center', va='center', fontsize=8, fontweight='bold')

    if i < len(steps) - 1:
        ax.annotate('', xy=(x + 0.45, 0.55), xytext=(x + 0.4, 0.55),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))

plt.title('Technical Roadmap', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig('技术路线图.png', dpi=300, bbox_inches='tight')
plt.show()