"""
信号与系统实验：连续信号与离散信号的绘制
使用Python + Matplotlib + NumPy/SciPy
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 设置中文字体（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建图形窗口
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('连续信号与离散信号对比展示', fontsize=16, fontweight='bold')

# ==================== 3. 连续阶跃信号 ====================
ax3 = axes[1, 0]
t_step = np.linspace(-1, 3, 1000)
# 使用scipy.signal.unit_step或手动定义
unit_step = np.where(t_step >= 0, 1, 0)
# 或者使用: unit_step = signal.unit_step(t_step)

ax3.plot(t_step, unit_step, 'g-', linewidth=2.5, label='$u(t)$')
ax3.axvline(x=0, color='gray', linestyle='--', alpha=0.5, label='t=0')
ax3.set_title('连续信号：单位阶跃信号', fontsize=12, fontweight='bold')
ax3.set_xlabel('时间 t (s)')
ax3.set_ylabel('幅值')
ax3.grid(True, alpha=0.3)
ax3.legend()
ax3.set_xlim([-1, 3])
ax3.set_ylim([-0.2, 1.5])

# ==================== 4. 离散阶跃序列 ====================
ax4 = axes[1, 1]
n_step = np.arange(-5, 15)  # n从-5到14
# 离散单位阶跃序列 u[n]
unit_step_discrete = np.where(n_step >= 0, 1, 0)

markerline, stemlines, baseline = ax4.stem(n_step, unit_step_discrete, 
                                            linefmt='m-', markerfmt='mo', basefmt='k-')
plt.setp(stemlines, 'linewidth', 2.5)
plt.setp(markerline, 'markersize', 7)
ax4.axvline(x=0, color='gray', linestyle='--', alpha=0.5)
ax4.set_title('离散信号：单位阶跃序列', fontsize=12, fontweight='bold')
ax4.set_xlabel('采样点 n')
ax4.set_ylabel('幅值 u[n]')
ax4.grid(True, alpha=0.3)
ax4.set_xlim([-6, 15])
ax4.set_ylim([-0.2, 1.5])

plt.tight_layout()
plt.show()

print("信号绘制完成！")
