import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from matplotlib import transforms
import math


# —— 参数：整体间距与分组间隔（可按需调大/调小）——
SPACING   = 1.5   # >1 时，相邻柱子之间更疏
GROUP_GAP = 0.80   # 秒组与分钟组之间的额外间隙


# 设置字体和图表样式
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 0.8


# 数据定义
labels = ['pass-through', 'obfuscation', 'blending$^{\dagger}$', 'blending$^{\dagger\dagger}$', 'blending$^{\ddagger\ddagger}$', 'repetition',
          'tunable responder', 'apache server']
# 前6个数据（秒），后2个数据（分钟）
values_seconds = [6.54, 8.94, 12.72, 23.95, 35.82, 89.71]
values_minutes = [7.71, 40.03]
value_labels = ['6.54', '8.94', '12.72', '23.95', '35.82', '89.71', '7.71', '40.03']


# 创建图表
fig, ax1 = plt.subplots(figsize=(3.5, 3))


# 定义不同的颜色和图案
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']
patterns = ['///', '...', '+++', 'xxx', '\\\\\\', '|||', '---', 'ooo']


# —— 计算 x 位置：按 SPACING 拉开距离，并在两组之间加 GROUP_GAP ——
n_sec, n_min = 6, 2
x_pos_seconds = np.arange(n_sec) * SPACING
x_start_minutes = n_sec * SPACING + GROUP_GAP
x_pos_minutes = x_start_minutes + np.arange(n_min) * SPACING

# # 创建柱状图的x位置（增加第6和第7个柱子之间的距离）
# x_pos_seconds = np.arange(6)  # 前6个
# x_pos_minutes = np.array([6.8, 7.8])  # 后2个，明确指定2个位置

BAR_WIDTH = 0.7

# 绘制前6个柱子（秒单位）
bars_seconds = ax1.bar(x_pos_seconds, values_seconds, color='white',
                       edgecolor=colors[:6], linewidth=1.2, width=BAR_WIDTH)
# 为前6个柱子添加图案
for bar, color, pattern in zip(bars_seconds, colors[:6], patterns[:6]):
    bar.set_facecolor('white')
    bar.set_edgecolor(color)
    bar.set_hatch(pattern)
    bar.set_linewidth(1.2)


# 创建第二个y轴用于分钟单位
ax2 = ax1.twinx()


# 绘制后2个柱子（分钟单位）
bars_minutes = ax2.bar(x_pos_minutes, values_minutes, color='white',
                       edgecolor=colors[6:8], linewidth=1.2, width=BAR_WIDTH)
# 为后2个柱子添加图案
for bar, color, pattern in zip(bars_minutes, colors[6:8], patterns[6:8]):
    bar.set_facecolor('white')
    bar.set_edgecolor(color)
    bar.set_hatch(pattern)
    bar.set_linewidth(1.2)


# 在柱子上方添加数值标签
# 前6个柱子的标签
for i, (bar, value_label) in enumerate(zip(bars_seconds, value_labels[:6])):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + max(values_seconds)*0.05,
            value_label, ha='center', va='bottom', fontsize=8, fontweight='bold', clip_on=False)
# 后2个柱子的标签
for i, (bar, value_label) in enumerate(zip(bars_minutes, value_labels[6:])):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + max(values_minutes)*0.05,
            value_label, ha='center', va='bottom', fontsize=8, fontweight='bold', clip_on=False)


# 设置x轴标签（倾斜45度）
# all_x_pos = np.concatenate([x_pos_seconds, x_pos_minutes])
# ax1.set_xticks(all_x_pos)
# ax1.set_xticklabels(labels, rotation=45, ha='right')
# 取消x轴刻度标签
ax1.set_xticks([])
# 移除x轴标题
ax1.set_xlabel('')


# 设置y轴标签
ax1.set_ylabel('Time (s)', fontweight='bold', color='black')
ax2.set_ylabel('Time (min)', fontweight='bold', color='black')
# 设置y轴范围
ax1.set_ylim(0, max(values_seconds) * 1.2)
ax2.set_ylim(0, max(values_minutes) * 1.2)


# 让两端也留点边距，避免柱子/文字贴边
ax1.margins(x=0.05)


# 添加虚线分隔（在第6和第7个柱子之间，调整位置）
split_x = (x_pos_seconds[-1] + x_pos_minutes[0]) / 2
ax1.axvline(x=split_x, color='gray', linestyle='--', linewidth=1, alpha=0.7)
# ax1.axvline(x=5.9, color='gray', linestyle='--', linewidth=1, alpha=0.7)

# 设置网格（只在左侧y轴显示）
ax1.grid(True, axis='y', alpha=0.3, linewidth=0.5)
ax1.set_axisbelow(True)
ax2.grid(False)  # 关闭右侧网格避免重叠


# 调整布局
# plt.tight_layout()


# 设置图表边框
for spine in ax1.spines.values():
    spine.set_linewidth(0.8)
for spine in ax2.spines.values():
    spine.set_linewidth(0.8)


# —— 在图下方添加“样式+名称”的自定义图例 ——
handles = [
    mpatches.Patch(facecolor='white', edgecolor=colors[i],
                   hatch=patterns[i], linewidth=1.2)
    for i in range(len(labels))
]
# 用 fig.legend 放到图下方中央；两行展示更紧凑
legend = fig.legend(
    handles, labels, loc='lower center',
    ncol=3,  # 每行放置 2 个图例
    frameon=False,      # 可设 True + fancybox=True 添加边框
    handlelength=1.6, handletextpad=0.6, columnspacing=1.4, borderaxespad=0.8,
    labelspacing=0.6       # 行间距（可再小一点，比如 0.5）
)
# # 设置图例斜体显示
# for txt in legend.get_texts():
#     txt.set_fontstyle('italic')


# —— 在横坐标下方加两段分组标签 ——
# 使用“数据 x + 轴坐标 y”的混合变换，这样随数据位置而自动居中，且与 y 轴范围无关
trans = transforms.blended_transform_factory(ax1.transData, ax1.transAxes)

# 组的左右边界与中心
left_sec  = x_pos_seconds[0]   - BAR_WIDTH/2
right_sec = x_pos_seconds[-1]  + BAR_WIDTH/2
center_sec = 0.5*(left_sec + right_sec)

left_min  = x_pos_minutes[0]   - BAR_WIDTH/2
right_min = x_pos_minutes[-1]  + BAR_WIDTH/2
center_min = 0.5*(left_min + right_min)

# 文本与“括号线”相对轴的 y 位置（负值表示在轴下方；可按需微调）
y_line_top    = -0.03  # 竖线的上端（靠近轴）
y_line_bottom = -0.06  # 横线所在（更靠下）
y_text        = -0.09  # 文字位置（在括号下方）

# 画括号线（可注释掉，如果只要文字）
# for L, R in [(left_sec, right_sec), (left_min, right_min)]:
#     ax1.plot([L, R], [y_line_top, y_line_top], transform=trans, clip_on=False, color='black', lw=0.8)
#     ax1.plot([L, L], [y_line_top, y_line_bottom], transform=trans, clip_on=False, color='black', lw=0.8)
#     ax1.plot([R, R], [y_line_top, y_line_bottom], transform=trans, clip_on=False, color='black', lw=0.8)
for L, R in [(left_sec, right_sec), (left_min, right_min)]:
    # 横线放底部
    ax1.plot([L, R], [y_line_bottom, y_line_bottom],
             transform=trans, clip_on=False, color='black', lw=0.8)
    # 竖线向上
    ax1.plot([L, L], [y_line_bottom, y_line_top],
             transform=trans, clip_on=False, color='black', lw=0.8)
    ax1.plot([R, R], [y_line_bottom, y_line_top],
             transform=trans, clip_on=False, color='black', lw=0.8)



# 写分组标题
ax1.text(center_sec, y_text, "mutation strategy", transform=trans,
         ha='center', va='top', fontsize=10)
ax1.text(center_min, y_text, "responder", transform=trans,
         ha='center', va='top', fontsize=10)


# 给下方同时容纳“分组标签 + 图例”留空间（如重叠可继续调大）
plt.subplots_adjust(bottom=0.41)  # 视情况调到 0.28~0.36 之间更合适
# rows = math.ceil(len(labels) / 2)
# plt.subplots_adjust(bottom=0.30 + 0.08*(rows-1))


# 保存高清矢量图
plt.savefig('performance.pdf', bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.savefig('performance.svg', bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.savefig('performance.eps', bbox_inches='tight',
            facecolor='white', edgecolor='none')

# 显示图表
plt.show()