#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
三维空间发散场与二维平面相互作用的逼真3D动画
3D Space Divergent Field and 2D Plane Interaction Animation

核心概念：质量M产生球对称空间发散场，与质量m在二维平面上相互作用
Author: Physics Visualization Master
Date: 2025-09-16
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.patches import Circle, FancyBboxPatch
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap

# 设置中文字体和高质量渲染
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 12
plt.rcParams['figure.dpi'] = 120
plt.rcParams['savefig.dpi'] = 300

class SpaceFieldInteractionAnimator:
    """空间场相互作用动画器"""
    
    def __init__(self):
        self.fig = None
        self.total_frames = 300
        
        # 物理参数
        self.mass_M_pos = np.array([-2, 0, 0])  # 质量M位置
        self.mass_m_pos = np.array([2, 0, 0])   # 质量m位置
        self.interaction_plane_z = 0             # 相互作用平面z=0
        
        # 颜色配置 - 更逼真的物理色彩
        self.colors = {
            'mass_M': '#FF4444',        # 红色质量M
            'mass_m': '#4444FF',        # 蓝色质量m
            'field_M': '#FF6B6B',       # M的场
            'field_m': '#6B6BFF',       # m的场
            'interaction_plane': '#44FF44',  # 绿色相互作用平面
            'field_lines': '#FFD700',   # 金色场线
            'projection': '#FF8C00',    # 橙色投影
            'background': '#F0F8FF',    # 淡蓝背景
            'text': '#2C3E50'
        }
        
        # 创建自定义颜色映射
        self.field_cmap = LinearSegmentedColormap.from_list(
            'field', ['white', '#FFE4E1', '#FF6B6B', '#FF0000'], N=256)
        
    def setup_figure(self):
        """设置高质量图形布局"""
        self.fig = plt.figure(figsize=(20, 16))
        self.fig.patch.set_facecolor(self.colors['background'])
        
        # 主标题
        self.fig.suptitle('三维空间发散场与二维平面相互作用的物理原理', 
                         fontsize=22, fontweight='bold', color=self.colors['text'])
        
        # 创建子图布局 (2x2 主要视图 + 2个说明图)
        self.ax_main = self.fig.add_subplot(221, projection='3d')
        self.ax_side = self.fig.add_subplot(222, projection='3d')
        self.ax_projection = self.fig.add_subplot(223)
        self.ax_explanation = self.fig.add_subplot(224)
        
        return self.fig
    
    def create_spherical_field(self, center, radius_max=3, n_points=20):
        """创建球对称发散场"""
        # 创建球面网格
        u = np.linspace(0, 2*np.pi, n_points)
        v = np.linspace(0, np.pi, n_points//2)
        
        spheres = []
        for r in np.linspace(0.5, radius_max, 6):
            x = center[0] + r * np.outer(np.cos(u), np.sin(v))
            y = center[1] + r * np.outer(np.sin(u), np.sin(v))
            z = center[2] + r * np.outer(np.ones(np.size(u)), np.cos(v))
            spheres.append((x, y, z, r))
        
        return spheres
    
    def create_field_vectors(self, center, n_vectors=50):
        """创建从中心发散的场矢量"""
        vectors = []
        
        # 随机生成球面上的点
        np.random.seed(42)  # 固定随机种子保证一致性
        
        for i in range(n_vectors):
            # 球坐标
            theta = np.random.uniform(0, 2*np.pi)
            phi = np.random.uniform(0, np.pi)
            
            # 转换为直角坐标
            direction = np.array([
                np.sin(phi) * np.cos(theta),
                np.sin(phi) * np.sin(theta),
                np.cos(phi)
            ])
            
            # 矢量起点和终点
            start = center
            end = center + 2.5 * direction
            
            vectors.append({
                'start': start,
                'end': end,
                'direction': direction,
                'theta': theta,
                'phi': phi
            })
        
        return vectors
    
    def draw_main_3d_view(self, frame):
        """绘制主要的3D视图"""
        self.ax_main.clear()
        
        # 设置视角
        rotation = frame * 360 / self.total_frames
        self.ax_main.view_init(elev=20, azim=rotation)
        
        # 绘制质量M (红色球体)
        u = np.linspace(0, 2*np.pi, 20)
        v = np.linspace(0, np.pi, 20)
        x_M = self.mass_M_pos[0] + 0.3 * np.outer(np.cos(u), np.sin(v))
        y_M = self.mass_M_pos[1] + 0.3 * np.outer(np.sin(u), np.sin(v))
        z_M = self.mass_M_pos[2] + 0.3 * np.outer(np.ones(np.size(u)), np.cos(v))
        self.ax_main.plot_surface(x_M, y_M, z_M, color=self.colors['mass_M'], alpha=0.8)
        
        # 绘制质量m (蓝色球体)
        x_m = self.mass_m_pos[0] + 0.2 * np.outer(np.cos(u), np.sin(v))
        y_m = self.mass_m_pos[1] + 0.2 * np.outer(np.sin(u), np.sin(v))
        z_m = self.mass_m_pos[2] + 0.2 * np.outer(np.ones(np.size(u)), np.cos(v))
        self.ax_main.plot_surface(x_m, y_m, z_m, color=self.colors['mass_m'], alpha=0.8)
        
        # 绘制M的球对称发散场
        spheres_M = self.create_spherical_field(self.mass_M_pos)
        for i, (x, y, z, r) in enumerate(spheres_M):
            alpha = 0.1 - i * 0.015  # 越远越透明
            if alpha > 0:
                self.ax_main.plot_wireframe(x, y, z, alpha=alpha, 
                                          color=self.colors['field_M'], linewidth=0.8)
        
        # 绘制m的球对称发散场 (较小)
        spheres_m = self.create_spherical_field(self.mass_m_pos, radius_max=2, n_points=15)
        for i, (x, y, z, r) in enumerate(spheres_m):
            alpha = 0.08 - i * 0.012
            if alpha > 0:
                self.ax_main.plot_wireframe(x, y, z, alpha=alpha,
                                          color=self.colors['field_m'], linewidth=0.6)
        
        # 绘制相互作用平面 (z=0平面)
        xx, yy = np.meshgrid(np.linspace(-4, 4, 20), np.linspace(-3, 3, 15))
        zz = np.zeros_like(xx)
        self.ax_main.plot_surface(xx, yy, zz, alpha=0.3, 
                                color=self.colors['interaction_plane'])
        
        # 绘制发散矢量 (动态显示)
        vectors_M = self.create_field_vectors(self.mass_M_pos, 30)
        progress = (frame % 100) / 100.0
        n_visible = int(len(vectors_M) * progress)
        
        for vec in vectors_M[:n_visible]:
            self.ax_main.quiver(vec['start'][0], vec['start'][1], vec['start'][2],
                              vec['end'][0]-vec['start'][0], 
                              vec['end'][1]-vec['start'][1],
                              vec['end'][2]-vec['start'][2],
                              color=self.colors['field_lines'], alpha=0.7, arrow_length_ratio=0.1)
        
        # 标注
        self.ax_main.text(self.mass_M_pos[0], self.mass_M_pos[1], self.mass_M_pos[2]+1,
                         'M\n(大质量)', fontsize=12, color=self.colors['mass_M'], 
                         ha='center', fontweight='bold')
        self.ax_main.text(self.mass_m_pos[0], self.mass_m_pos[1], self.mass_m_pos[2]+1,
                         'm\n(小质量)', fontsize=12, color=self.colors['mass_m'],
                         ha='center', fontweight='bold')
        
        self.ax_main.set_xlabel('X')
        self.ax_main.set_ylabel('Y') 
        self.ax_main.set_zlabel('Z')
        self.ax_main.set_title('三维空间中的球对称发散场', fontsize=14, fontweight='bold')
        
        # 设置坐标轴范围
        self.ax_main.set_xlim([-5, 5])
        self.ax_main.set_ylim([-4, 4])
        self.ax_main.set_zlim([-3, 3])
    
    def draw_side_view(self, frame):
        """绘制侧视图 - 强调平面投影"""
        self.ax_side.clear()
        
        # 固定侧视角度
        self.ax_side.view_init(elev=0, azim=0)  # 从侧面看
        
        # 绘制质量
        self.ax_side.scatter([self.mass_M_pos[0]], [self.mass_M_pos[1]], [self.mass_M_pos[2]],
                           s=300, c=self.colors['mass_M'], alpha=0.8, label='质量M')
        self.ax_side.scatter([self.mass_m_pos[0]], [self.mass_m_pos[1]], [self.mass_m_pos[2]],
                           s=200, c=self.colors['mass_m'], alpha=0.8, label='质量m')
        
        # 绘制相互作用平面 (强调)
        xx, yy = np.meshgrid(np.linspace(-4, 4, 10), np.linspace(-3, 3, 8))
        zz = np.zeros_like(xx)
        self.ax_side.plot_surface(xx, yy, zz, alpha=0.5,
                                color=self.colors['interaction_plane'])
        
        # 绘制从M到平面的投影线
        projection_points = []
        for angle in np.linspace(0, 2*np.pi, 16):
            for elevation in np.linspace(-np.pi/3, np.pi/3, 8):
                # 球面上的点
                r = 2.5
                x = self.mass_M_pos[0] + r * np.cos(elevation) * np.cos(angle)
                y = self.mass_M_pos[1] + r * np.cos(elevation) * np.sin(angle)
                z = self.mass_M_pos[2] + r * np.sin(elevation)
                
                # 投影到z=0平面
                x_proj = x
                y_proj = y
                z_proj = 0
                
                # 绘制投影线
                if frame % 60 < 30:  # 闪烁效果
                    self.ax_side.plot([x, x_proj], [y, y_proj], [z, z_proj],
                                    color=self.colors['projection'], alpha=0.4, linewidth=1)
                
                projection_points.append([x_proj, y_proj, z_proj])
        
        # 在平面上显示投影点
        if len(projection_points) > 0:
            proj_array = np.array(projection_points)
            self.ax_side.scatter(proj_array[:, 0], proj_array[:, 1], proj_array[:, 2],
                               s=20, c=self.colors['projection'], alpha=0.6)
        
        self.ax_side.set_xlabel('X')
        self.ax_side.set_ylabel('Y')
        self.ax_side.set_zlabel('Z')
        self.ax_side.set_title('侧视图：三维场向二维平面的投影', fontsize=14, fontweight='bold')
        
        # 设置坐标轴范围
        self.ax_side.set_xlim([-5, 5])
        self.ax_side.set_ylim([-4, 4])
        self.ax_side.set_zlim([-3, 3])
    
    def draw_projection_analysis(self, frame):
        """绘制投影分析图"""
        self.ax_projection.clear()
        
        # 绘制圆形表示相互作用平面的截面
        circle = Circle((0, 0), 2, fill=False, color=self.colors['interaction_plane'], 
                       linewidth=3, label='相互作用平面截面')
        self.ax_projection.add_patch(circle)
        
        # 绘制质量M和m在平面上的投影
        self.ax_projection.scatter([-2], [0], s=400, c=self.colors['mass_M'], 
                                 alpha=0.8, label='质量M投影', marker='o')
        self.ax_projection.scatter([2], [0], s=300, c=self.colors['mass_m'],
                                 alpha=0.8, label='质量m投影', marker='o')
        
        # 动态显示场强分布
        progress = (frame % 120) / 120.0
        
        # 创建场强分布
        x = np.linspace(-3, 3, 50)
        y = np.linspace(-3, 3, 50)
        X, Y = np.meshgrid(x, y)
        
        # M的场强 (1/r^2分布)
        r_M = np.sqrt((X + 2)**2 + Y**2) + 0.1
        field_M = 1 / r_M**2
        
        # m的场强
        r_m = np.sqrt((X - 2)**2 + Y**2) + 0.1
        field_m = 0.5 / r_m**2
        
        # 总场强
        total_field = field_M + field_m
        
        # 绘制场强等高线
        levels = np.linspace(0, np.max(total_field)*0.8, 10)
        contour = self.ax_projection.contour(X, Y, total_field, levels=levels, 
                                           colors=self.colors['field_lines'], alpha=0.6)
        
        # 绘制相互作用区域 (动态高亮)
        interaction_x = np.linspace(-1, 1, 20)
        interaction_y = np.linspace(-0.5, 0.5, 10)
        IX, IY = np.meshgrid(interaction_x, interaction_y)
        
        if frame % 80 < 40:  # 闪烁效果
            self.ax_projection.contourf(IX, IY, np.ones_like(IX), levels=[0, 1],
                                      colors=[self.colors['projection']], alpha=0.3)
        
        # 添加箭头表示相互作用
        self.ax_projection.annotate('', xy=(1, 0), xytext=(-1, 0),
                                  arrowprops=dict(arrowstyle='<->', 
                                                color=self.colors['projection'],
                                                lw=3))
        self.ax_projection.text(0, -0.3, '相互作用', ha='center', fontsize=12,
                              color=self.colors['projection'], fontweight='bold')
        
        self.ax_projection.set_xlim(-3.5, 3.5)
        self.ax_projection.set_ylim(-3.5, 3.5)
        self.ax_projection.set_aspect('equal')
        self.ax_projection.set_title('二维平面上的场相互作用', fontsize=14, fontweight='bold')
        self.ax_projection.legend(loc='upper right')
        self.ax_projection.grid(True, alpha=0.3)
    
    def draw_explanation(self, frame):
        """绘制原理解释"""
        self.ax_explanation.clear()
        self.ax_explanation.axis('off')
        
        # 动态显示解释文本
        explanations = [
            "物理原理解释:",
            "",
            "1. 质量M产生球对称空间发散场",
            "   • 场向所有方向以光速c发散",
            "   • 三维空间中的球面波",
            "",
            "2. 质量m也产生类似的发散场",
            "   • 两个场在空间中重叠",
            "",
            "3. 相互作用发生在二维平面上",
            "   • 三维球面场投影到二维平面",
            "   • 需要几何修正因子",
            "",
            "4. 几何因子的来源:",
            "   • 球面积: 4πr^2 (三维总量)",
            "   • 平面截面: πr^2 (二维有效量)",
            "   • 比值: 4πr^2/πr^2 = 4",
            "",
            "5. 考虑对称性和投影效应",
            "   • 实际几何因子 ≈ 2",
            "",
            "核心思想: 三维→二维的几何约化"
        ]
        
        progress = frame / self.total_frames
        n_lines = min(len(explanations), int(progress * len(explanations) * 1.5))
        
        y_start = 0.95
        line_height = 0.04
        
        for i in range(n_lines):
            line = explanations[i]
            y_pos = y_start - i * line_height
            
            # 设置不同的文本样式
            if line.endswith(":"):
                color = self.colors['mass_M']
                weight = 'bold'
                size = 13
            elif line.startswith("   •"):
                color = self.colors['field_M']
                weight = 'normal'
                size = 11
            elif line.startswith("核心思想:"):
                color = self.colors['projection']
                weight = 'bold'
                size = 14
            elif line.strip().isdigit() or line.strip().startswith(tuple('12345')):
                color = self.colors['mass_m']
                weight = 'bold'
                size = 12
            else:
                color = self.colors['text']
                weight = 'normal'
                size = 11
            
            self.ax_explanation.text(0.05, y_pos, line, fontsize=size, color=color,
                                   weight=weight, transform=self.ax_explanation.transAxes)
        
        # 添加边框
        bbox = dict(boxstyle="round,pad=0.02", facecolor='lightyellow', alpha=0.8)
        self.ax_explanation.text(0.5, 0.02, 
                               f'帧数: {frame}/{self.total_frames}',
                               ha='center', fontsize=10, color='gray',
                               transform=self.ax_explanation.transAxes, bbox=bbox)
    
    def animate(self, frame):
        """主动画函数"""
        # 清除之前的内容并重绘
        self.draw_main_3d_view(frame)
        self.draw_side_view(frame)
        self.draw_projection_analysis(frame)
        self.draw_explanation(frame)
        
        plt.tight_layout()
    
    def create_animation(self):
        """创建动画"""
        self.setup_figure()
        
        anim = animation.FuncAnimation(
            self.fig, self.animate, frames=self.total_frames,
            interval=80, blit=False, repeat=True
        )
        
        return anim

def main():
    """主函数"""
    print("正在创建三维空间发散场与二维平面相互作用动画...")
    print("这将展示几何因子产生的物理原理")
    
    animator = SpaceFieldInteractionAnimator()
    anim = animator.create_animation()
    
    # 显示动画
    plt.show()
    
    # 询问是否保存
    save_option = input("\n选择保存选项:\n1. 保存为GIF\n2. 保存为MP4\n3. 不保存\n请输入选项 (1/2/3): ").strip()
    
    if save_option == '1':
        print("正在保存为GIF文件...")
        anim.save('三维发散场二维投影动画.gif', writer='pillow', fps=12, dpi=150)
        print("GIF文件已保存!")
    elif save_option == '2':
        print("正在保存为MP4文件...")
        try:
            anim.save('三维发散场二维投影动画.mp4', writer='ffmpeg', fps=15, dpi=200)
            print("MP4文件已保存!")
        except:
            print("MP4保存失败，请确保安装了ffmpeg")
    
    print("\n动画展示了:")
    print("• 质量M和m产生的球对称空间发散场")
    print("• 三维场如何投影到二维相互作用平面")
    print("• 几何因子产生的物理原理")
    print("• 从三维到二维的几何约化过程")

if __name__ == "__main__":
    main()