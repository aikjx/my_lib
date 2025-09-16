#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
张祥前统一场论17个核心公式HTML5可视化自动生成器
Automatic Generator for Zhang Xiangqian's Unified Field Theory Visualizations

为每个核心公式生成完整的HTML5可视化系统
Author: Unified Field Theory Visualization Team
Date: 2025-09-16
"""

import os
import json
from pathlib import Path

class UnifiedFieldVisualizationGenerator:
    """统一场论可视化生成器"""
    
    def __init__(self):
        self.base_path = Path("utf/张祥前统一场论可视化")
        self.formulas = self.load_formula_database()
        
    def load_formula_database(self):
        """加载公式数据库"""
        return [
            {
                "id": "01",
                "name": "时空同一化方程",
                "formula": r"\vec{R} = \vec{C}t",
                "description": "揭示时间与空间的统一本质",
                "category": "基础时空",
                "color_scheme": "green",
                "visualization_type": "3d_vector_field"
            },
            {
                "id": "02", 
                "name": "三维螺旋时空方程",
                "formula": r"\nabla \times \vec{C} = \vec{S}",
                "description": "描述空间的圆柱螺旋式运动",
                "category": "基础时空",
                "color_scheme": "green",
                "visualization_type": "3d_spiral_field"
            },
            # ... 其他15个公式将在完整版本中添加
        ]
    
    def generate_all_visualizations(self):
        """生成所有公式的可视化"""
        print("🚀 开始生成张祥前统一场论17个核心公式可视化...")
        
        for formula in self.formulas:
            self.generate_formula_visualization(formula)
        
        self.generate_universe_visualization()
        print("✅ 所有可视化生成完成！")
    
    def generate_formula_visualization(self, formula):
        """为单个公式生成可视化"""
        folder_name = f"{formula['id']}-{formula['name']}"
        folder_path = self.base_path / folder_name
        
        # 创建文件夹
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # 生成主要文件
        self.create_visualization_html(folder_path, formula)
        self.create_theory_md(folder_path, formula)
        self.create_interactive_demo(folder_path, formula)
        
        print(f"✅ 已生成: {formula['name']}")

if __name__ == "__main__":
    generator = UnifiedFieldVisualizationGenerator()
    generator.generate_all_visualizations()