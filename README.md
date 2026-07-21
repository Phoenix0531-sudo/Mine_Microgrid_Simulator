<div align="center">

# Mine Microgrid Simulator

**Professional microgrid planning and analysis platform with Streamlit and Plotly**

[English](README.md) | [中文](README.zh-CN.md)

![CI](https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator/actions/workflows/ci.yml/badge.svg)

**矿区微电网规划分析平台 | Professional Microgrid Planning and Analysis Platform**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![Plotly](https://img.shields.io/badge/Plotly-5.0%2B-purple)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>

基于 Streamlit 和 Plotly 构建的专业级微电网规划分析平台，集成现代化 UI 设计、高级可视化和异步处理能力。专为矿区可再生能源系统设计，提供从系统建模到经济性分析的完整解决方案。

> A professional microgrid planning and analysis platform built with Streamlit and Plotly. Designed for mine-site renewable energy systems, providing end-to-end solutions from system modeling to economic analysis.

---

## 技术特性 | Features

| 中文特性 | English Feature | 说明 / Description |
|---------|----------------|-------------------|
| 精确仿真引擎 | Simulation Engine | 8760 小时逐时能量平衡计算 |
| 多能源支持 | Multi-Energy Support | 光伏、风电、储能系统集成建模 |
| 实时气象数据 | Live Weather Data | 基于 Open-Meteo API 的实时气象数据 |
| 智能调度算法 | Smart Dispatch | 考虑经济性和技术约束的优化调度 |
| 多维度 KPI | Multi-Dimension KPIs | 可再生能源渗透率、自消纳率、电网独立度 |
| 经济性评估 | Economic Analysis | NPV、IRR、LCOE、投资回收期分析 |
| 敏感性分析 | Sensitivity Analysis | 关键参数对系统性能的影响评估 |
| 交互可视化 | Interactive Visualization | 3D 能量流动、热力图、雷达图、瀑布图 |
| 异步计算 | Async Computing | 非阻塞用户界面，6 步骤进度显示 |
| 性能监控 | Performance Monitoring | 实时监控计算性能和系统资源使用 |

---

## 目录 | Table of Contents

- [数据准备 | Data Preparation](#数据准备--data-preparation)
- [核心原理 | Core Method](#核心原理--core-method)
- [模块文档 | Module Reference](#模块文档--module-reference)
- [快速开始 | Quick Start](#快速开始--quick-start)
- [输出说明 | Output](#输出说明--output)
- [安装与运行 | Installation](#安装与运行--installation)
- [Docker 使用 | Docker Usage](#docker-使用--docker-usage)
- [项目结构 | Project Structure](#项目结构--project-structure)
- [引用 | Citation](#引用--citation)
- [许可证 | License](#许可证--license)

---

## 数据准备 | Data Preparation

工具需要以下输入数据：

- **矿山负荷曲线**：CSV 格式的逐时用电数据
- **气象数据**：通过 Open-Meteo API 自动获取（需网络连接）
- **设备参数**：光伏板、风机、储能的配置参数

> Required inputs include mine load profiles (CSV), weather data (auto-fetched via Open-Meteo API), and equipment configuration parameters.

---

## 核心原理 | Core Method

平台基于能量平衡模型，逐小时模拟微电网的运行状态。光伏和风电出力分别通过 pvlib 和 windpowerlib 库计算。储能系统采用荷电状态（SOC）管理策略。经济性评估基于净现值（NPV）、内部收益率（IRR）和平准化能源成本（LCOE）等指标。

> The platform simulates microgrid operation on an hourly basis using energy balance modeling. Solar and wind power are calculated using pvlib and windpowerlib. Economic analysis is based on NPV, IRR, and LCOE.

---

## 模块文档 | Module Reference

| 模块 | 功能 |
|------|------|
| `app.py` | Streamlit 主应用入口，页面布局与路由 |
| `modules/simulation_engine.py` | 光伏/风电出力计算与能量平衡仿真 |
| `modules/data_handler.py` | 负荷数据加载与气象 API 调用 |
| `modules/results_analyzer.py` | 结果展示、KPI 计算与图表生成 |
| `modules/advanced_visualization.py` | 3D 图表、动画、热力图等高级可视化 |
| `modules/advanced_ui.py` | 高级 UI 组件（状态仪表板、KPI 面板） |
| `modules/config.py` | 默认配置与设备参数管理 |
| `modules/async_processor.py` | 异步任务管理与进度显示 |
| `modules/error_handler.py` | 错误捕获、自动重试与恢复 |
| `modules/memory_optimizer.py` | 大数据分块处理与缓存管理 |

---

## 快速开始 | Quick Start

```bash
# 安装依赖
pip install -r requirements.txt

# 启动应用
streamlit run app.py
```

打开浏览器访问 http://localhost:8501。

---

## 输出说明 | Output

平台输出包括：

- **系统概览仪表板**：关键指标卡片、状态监控
- **能量平衡分析**：逐时供需曲线、Sankey 能量流图
- **经济性评估**：NPV、IRR、LCOE、投资回收期
- **敏感性分析**：参数变化对系统性能的影响
- **可视化报告**：3D 能量流动、热力图、雷达图、瀑布图

---

## 安装与运行 | Installation

### 系统要求

- Python 3.8 或更高版本
- 4GB+ RAM
- 现代浏览器（Chrome 90+, Firefox 88+, Safari 14+）
- 网络连接（获取气象数据）

### 安装

```bash
pip install -r requirements.txt
```

### 运行

```bash
streamlit run app.py
```

或双击 `start.bat`（Windows）。

---

## Docker 使用 | Docker Usage

本项目是 Streamlit Web 应用，完全适合 Docker 部署。

```bash
# 构建镜像
docker build -t mine-microgrid .

# 验证导入
docker run --rm mine-microgrid

# 启动 Web 服务
docker run -p 8501:8501 mine-microgrid streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

启动后访问 http://localhost:8501。

---

## 项目结构 | Project Structure

```
Mine_Microgrid_Simulator/
├── app.py                  # Streamlit 主应用
├── requirements.txt        # Python 依赖
├── Dockerfile              # Docker 构建文件
├── LICENSE                 # MIT 许可证
├── .gitignore              # Git 忽略规则
├── .editorconfig           # 编辑器配置
├── CHANGELOG.md            # 变更日志
├── README.md               # 项目说明
├── scripts/
│   └── docker_smoke_test.py # Docker 导入验证
├── docs/
│   └── index.md            # GitHub Pages 入口
├── modules/
│   ├── __init__.py
│   ├── advanced_ui.py
│   ├── advanced_visualization.py
│   ├── async_processor.py
│   ├── config.py
│   ├── data_handler.py
│   ├── error_handler.py
│   ├── memory_optimizer.py
│   ├── performance.py
│   ├── results_analyzer.py
│   ├── simulation_engine.py
│   ├── ui_components.py
│   ├── utils.py
│   └── validation.py
└── start.bat               # Windows 启动脚本
```

---

## 引用 | Citation

```bibtex
@software{mine_microgrid2026,
  title = {Mine Microgrid Simulator},
  year = {2026},
  url = {https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator}
}
```

---

## 许可证 | License

本项目基于 MIT 许可证开源。详见 [LICENSE](LICENSE) 文件。

> This project is open-sourced under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<div align="center"><strong>Made for the renewable energy and mining community</strong></div>
