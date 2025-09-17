# 时空同一化方程可视化系统

张祥前统一场论中时空同一化方程的3D可视化实现

## 项目概述

本项目基于张祥前统一场论中的核心方程 `r⃗(t) = C⃗t` 创建先进的3D可视化系统，旨在直观展示时间与空间的统一关系。

## 核心方程

**时空同一化方程：**
```
r⃗(t) = C⃗t = x⃗i + y⃗j + z⃗k
```

其中：
- `r⃗(t)` - 时空位置矢量
- `C⃗` - 光速矢量（空间运动速度）
- `t` - 时间参数
- `x, y, z` - 空间坐标分量

## 技术栈

- **TypeScript** - 类型安全的JavaScript超集
- **Three.js** - 3D图形渲染库
- **WebGL 2.0** - 硬件加速图形API
- **MathJax** - 数学公式渲染
- **Webpack** - 模块打包工具
- **Jest** - 测试框架

## 项目结构

```
src/
├── core/                 # 核心应用逻辑
│   └── SpacetimeVisualizationApp.ts
├── physics/              # 物理引擎
│   └── PhysicsEngine.ts
├── rendering/            # 渲染系统
│   └── VisualizationRenderer.ts
├── ui/                   # 用户界面
│   └── UIManager.ts
├── types/                # 类型定义
│   └── PhysicsTypes.ts
├── utils/                # 工具类
│   └── Logger.ts
├── styles/               # 样式文件
│   └── main.css
├── index.html            # HTML模板
└── index.ts              # 应用入口
```

## 开发环境设置

### 安装依赖

```bash
npm install
```

### 开发模式

```bash
npm run dev
```

访问 http://localhost:3000 查看应用

### 生产构建

```bash
npm run build
```

### 运行测试

```bash
npm test
```

### 代码检查

```bash
npm run lint
```

## 功能特性

### 已实现功能

- ✅ 项目基础架构
- ✅ TypeScript配置
- ✅ Webpack构建系统
- ✅ 基础UI框架
- ✅ 日志系统
- ✅ 测试环境

### 计划功能

- 🔄 时空同一化方程求解器
- 🔄 3D轨迹可视化
- 🔄 实时参数控制
- 🔄 数学公式显示
- 🔄 物理概念解释
- 🔄 数据导出功能
- 🔄 教育模式
- 🔄 性能优化

## 物理背景

时空同一化方程是张祥前统一场论的核心组成部分，它揭示了：

1. **时空统一性** - 时间和空间不是独立的，而是统一的时空结构
2. **空间运动** - 空间本身以光速运动
3. **位置关系** - 物体的空间位置与时间成线性关系

## 开发指南

### 添加新功能

1. 在相应目录下创建新的TypeScript文件
2. 实现必要的接口和类型
3. 添加单元测试
4. 更新文档

### 代码规范

- 使用TypeScript严格模式
- 遵循ESLint规则
- 添加适当的注释和文档
- 保持代码简洁和可读性

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 联系方式

如有问题或建议，请通过GitHub Issues联系我们。