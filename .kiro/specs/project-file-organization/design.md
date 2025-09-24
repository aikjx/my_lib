# Design Document

## Overview

The project file organization system will consolidate the scattered files in the root directory with the existing well-structured `utf` directory, creating a unified and maintainable project structure. The design leverages the existing 9-category organization system while addressing current issues of file dispersion, inconsistent naming, and lack of clear navigation.

## Architecture

### Current State Analysis

**Existing Assets:**
- Well-organized `utf` directory with 9 main categories (01-核心论文 through 09-归档备份)
- Comprehensive subdirectory structure already in place
- Scattered files in root directory including core papers, verification scripts, and visualization files
- Mixed language naming (Chinese/English) and inconsistent formats
- Historical files in `.history` directory needing archival

**Target Architecture:**
- Consolidate root-level files into the existing `utf` structure
- Standardize naming conventions across all files
- Create navigation indices and documentation
- Establish clear migration paths and maintenance procedures

### Directory Structure Design

**Optimized Structure - Consolidating to Root Level:**

```
Project Root/
├── 01-核心论文/                   # Core research papers
│   ├── 引力光速统一方程/           # Main unified field theory papers
│   ├── 统一场论核心公式/           # Core formula derivations
│   ├── LaTeX源码/                 # LaTeX source files
│   └── 投稿版本/                  # Submission versions
├── 02-数学验证/                   # Mathematical verification
│   ├── 几何因子验证/              # Geometric factor proofs
│   ├── Z值计算/                   # Z-value calculations
│   ├── 公式验证/                  # Formula verification scripts
│   ├── 数值实验/                  # Numerical experiments
│   └── 数学基础/                  # Mathematical foundations (from math/)
├── 03-可视化系统/                 # Visualization system
│   ├── 交互式演示/                # Interactive demonstrations
│   ├── 静态图表/                  # Static charts and graphs
│   ├── 动画文件/                  # Animation files
│   └── 源代码/                    # Source code for visualizations
├── 04-分析报告/                   # Analysis reports
│   ├── 验证报告/                  # Verification reports
│   ├── 理论分析/                  # Theoretical analysis
│   └── 项目总结/                  # Project summaries
├── 05-发表准备/                   # Publication preparation
│   ├── Nature投稿/                # Nature journal submission
│   ├── 其他期刊/                  # Other journals
│   ├── 会议论文/                  # Conference papers
│   └── 媒体材料/                  # Media materials
├── 06-工具脚本/                   # Utility scripts
│   ├── 计算工具/                  # Calculation tools
│   ├── 格式转换/                  # Format conversion
│   └── 自动化脚本/                # Automation scripts
├── 07-参考资料/                   # Reference materials
│   ├── 理论背景/                  # Theoretical background (from 资料与说明/)
│   ├── 数学基础/                  # Mathematical foundations
│   ├── 实验数据/                  # Experimental data
│   └── 相关研究/                  # Related research
├── 08-项目管理/                   # Project management
│   ├── 版本控制/                  # Version control
│   ├── 协作管理/                  # Collaboration management
│   ├── 质量控制/                  # Quality control
│   └── 配置文件/                  # Configuration files
├── 09-归档备份/                   # Archive and backup
│   ├── 历史版本/                  # Historical versions (from .history/)
│   ├── 废弃文件/                  # Deprecated files (from 未命名/)
│   ├── 备份数据/                  # Backup data
│   └── 迁移备份/                  # Migration backups
├── .kiro/                         # Kiro configuration (preserved)
├── .obsidian/                     # Obsidian configuration (preserved)
├── .vscode/                       # VSCode configuration (preserved)
├── .git/                          # Git repository (preserved)
├── .gitignore                     # Git ignore file (updated)
└── README.md                      # Main project navigation index
```

**Migration Strategy:**
1. **Promote utf/ contents to root level** - Move all organized content from utf/ to project root
2. **Integrate scattered files** - Categorize and move root-level files into appropriate directories
3. **Archive legacy directories** - Move .history/, 未命名/, 资料与说明/ to archive
4. **Preserve system directories** - Keep .kiro/, .obsidian/, .vscode/, .git/ unchanged

## Components and Interfaces

### File Migration Engine

**Component:** `FileOrganizer`
- **Purpose:** Systematically move and rename files from root to appropriate utf subdirectories
- **Interface:** 
  - `categorize_file(filename) -> category_path`
  - `standardize_name(filename) -> standardized_name`
  - `migrate_file(source, destination)`

**Component:** `NamingStandardizer`
- **Purpose:** Apply consistent naming conventions
- **Interface:**
  - `generate_standard_name(file_type, content_type, version) -> filename`
  - `validate_naming_convention(filename) -> boolean`

### Navigation System

**Component:** `IndexGenerator`
- **Purpose:** Create comprehensive navigation and documentation
- **Interface:**
  - `generate_main_index() -> README.md`
  - `generate_category_index(category) -> category/README.md`
  - `update_cross_references()`

**Component:** `LinkValidator`
- **Purpose:** Ensure all internal links remain functional after reorganization
- **Interface:**
  - `scan_markdown_links(file_path) -> [links]`
  - `validate_link(link) -> status`
  - `update_broken_links(file_path, link_map)`

## Data Models

### File Classification Schema

```python
class FileCategory:
    CORE_PAPERS = "01-核心论文"
    MATH_VERIFICATION = "02-数学验证"
    VISUALIZATION = "03-可视化系统"
    ANALYSIS_REPORTS = "04-分析报告"
    PUBLICATION_PREP = "05-发表准备"
    UTILITY_SCRIPTS = "06-工具脚本"
    REFERENCE_MATERIALS = "07-参考资料"
    PROJECT_MANAGEMENT = "08-项目管理"
    ARCHIVE_BACKUP = "09-归档备份"

class FileType:
    PAPER = "论文"
    VERIFICATION = "验证"
    VISUALIZATION = "可视化"
    REPORT = "报告"
    SCRIPT = "脚本"
    REFERENCE = "参考"
    CONFIG = "配置"
    ARCHIVE = "归档"

class NamingConvention:
    format = "{序号}-{类型}-{主题}-{版本}.{扩展名}"
    # Example: "01-论文-引力光速统一方程-v3.0.md"
```

### Migration Mapping

```python
migration_rules = {
    # Phase 1: Promote utf/ structure to root level
    "utf/01-核心论文/*": "01-核心论文/",
    "utf/02-数学验证/*": "02-数学验证/",
    "utf/03-可视化系统/*": "03-可视化系统/",
    "utf/04-分析报告/*": "04-分析报告/",
    "utf/05-发表准备/*": "05-发表准备/",
    "utf/06-工具脚本/*": "06-工具脚本/",
    "utf/07-参考资料/*": "07-参考资料/",
    "utf/08-项目管理/*": "08-项目管理/",
    "utf/09-归档备份/*": "09-归档备份/",
    
    # Phase 2: Integrate scattered root files
    "引力光速统一方程*.md": "01-核心论文/引力光速统一方程/",
    "统一场论*.md": "01-核心论文/统一场论核心公式/",
    "基于张祥前*.md": "01-核心论文/引力光速统一方程/",
    "优化后的*.md": "01-核心论文/投稿版本/",
    
    # Verification and calculation scripts
    "verify_*.py": "02-数学验证/公式验证/",
    "*verification*.py": "02-数学验证/几何因子验证/",
    "detailed_z_*.py": "02-数学验证/Z值计算/",
    "fix_md_format*.py": "06-工具脚本/格式转换/",
    
    # Visualization files
    "几何因子*.html": "03-可视化系统/交互式演示/",
    "张祥前统一场论*.html": "03-可视化系统/交互式演示/",
    "index.html": "03-可视化系统/交互式演示/",
    "*.png": "03-可视化系统/静态图表/",
    "*.svg": "03-可视化系统/动画文件/",
    
    # Reports and analysis documents
    "*报告*.md": "04-分析报告/验证报告/",
    "*分析*.md": "04-分析报告/理论分析/",
    "*证明*.md": "04-分析报告/理论分析/",
    
    # Reference and documentation
    "资料与说明/*": "07-参考资料/理论背景/",
    "Nature*.md": "05-发表准备/Nature投稿/",
    "全球最强论文*.md": "05-发表准备/其他期刊/",
    "项目文件整理方案.md": "08-项目管理/协作管理/",
    
    # Mathematical foundations
    "math/*": "02-数学验证/数学基础/",
    
    # Archive and cleanup
    ".history/*": "09-归档备份/历史版本/",
    "未命名/*": "09-归档备份/废弃文件/",
    ".trash/*": "09-归档备份/废弃文件/",
    
    # Markdown guide (special case)
    "Markdown（简称 MD）*.md": "07-参考资料/理论背景/"
}
```

## Error Handling

### File Conflict Resolution

**Strategy:** Safe Migration with Backup
- Before any file move, create backup in `utf/09-归档备份/迁移备份/`
- If destination file exists, append timestamp to new file
- Maintain migration log for rollback capability

**Conflict Types:**
1. **Duplicate Names:** Append incremental suffix (-1, -2, etc.)
2. **Path Length Limits:** Truncate long names while preserving meaning
3. **Special Characters:** Replace with safe alternatives
4. **Encoding Issues:** Ensure UTF-8 compatibility

### Validation Checks

**Pre-Migration Validation:**
- Verify source file exists and is readable
- Check destination directory exists or can be created
- Validate sufficient disk space
- Ensure no critical system files are affected

**Post-Migration Validation:**
- Confirm file integrity (size, checksum)
- Validate all internal links still function
- Verify no orphaned references remain
- Test key functionality still works

## Testing Strategy

### Unit Testing

**File Operations Testing:**
```python
def test_file_categorization():
    # Test correct categorization of different file types
    assert categorize_file("verify_formula.py") == "utf/02-数学验证/公式验证/"
    assert categorize_file("几何因子.html") == "utf/03-可视化系统/交互式演示/"

def test_naming_standardization():
    # Test naming convention application
    result = standardize_name("引力光速统一方程：从空间动力学原理.md")
    assert result.startswith("01-论文-")
    assert result.endswith(".md")
```

**Integration Testing:**
- Test complete migration workflow from utf/ promotion to root level
- Test scattered file integration into organized structure
- Verify navigation index generation across all categories
- Test link validation and updating after restructuring

### Validation Testing

**Structure Validation:**
- Verify all expected directories exist
- Check README files are created in each category
- Validate naming conventions are applied consistently

**Content Integrity:**
- Compare file checksums before and after migration
- Test that all markdown links resolve correctly
- Verify no content is lost or corrupted

**User Acceptance Testing:**
- Test navigation efficiency with reorganized structure
- Verify research workflow is improved
- Confirm collaboration features work as expected

### Performance Testing

**Migration Performance:**
- Measure time to migrate different file sizes
- Test batch processing efficiency
- Monitor memory usage during large migrations

**Navigation Performance:**
- Test index generation speed
- Measure search and discovery time improvements
- Validate responsive navigation with large file counts

## Implementation Phases

### Phase 1: Preparation and Backup
- Create comprehensive backup of current state
- Generate migration plan and file mapping
- Set up logging and monitoring systems

### Phase 2: Core Migration
- Move and rename files according to classification rules
- Update internal links and references
- Generate category-specific README files

### Phase 3: Navigation and Documentation
- Create main project navigation index
- Generate cross-reference documentation
- Implement search and discovery aids

### Phase 4: Validation and Optimization
- Comprehensive testing of reorganized structure
- Performance optimization and cleanup
- User training and documentation updates