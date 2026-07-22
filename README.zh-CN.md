# Mine Microgrid Simulator

**面向矿山场景的微电网规划与分析演示（Streamlit + Plotly）。**

[English](README.md) | [中文](README.zh-CN.md)

[![CI](https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator/actions/workflows/ci.yml/badge.svg)](https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)

面向矿山场景的微电网规划与分析演示（Streamlit + Plotly）。

交互图表 · 场景模块。


## 功能

- ⚡ 微电网规划向模块
- 📊 Plotly 交互图
- 🌐 Streamlit 入口
- ✅ CI 冒烟 + 测试

## 快速开始

### 安装

```bash
git clone https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator.git
cd Mine_Microgrid_Simulator
pip install -r requirements.txt
```

### 使用

```bash
streamlit run app.py   # 或见 modules/ 文档入口
pytest tests/
```

## 项目结构

```
modules/  scripts/
tests/  docs/
```

## 说明

工程研究演示 — 非并网规范合规产品。

## 许可证

MIT。在注明出处的前提下可商业使用（以 LICENSE 为准）。详见 [LICENSE](LICENSE)。
