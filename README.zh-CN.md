# Mine Microgrid Simulator

**面向矿山场景的微电网规划演示（Streamlit + Plotly）。**

[English](README.md) | [中文](README.zh-CN.md)

[![CI](https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator/actions/workflows/ci.yml/badge.svg)](https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

交互图表与场景模块，用于工程研究。

## 预览

![Mine Microgrid Simulator](docs/screenshots/preview.png)

## 功能

- 微电网规划向模块
- Plotly 交互图
- Streamlit 入口
- CI 冒烟 + 测试

## 快速开始

### 安装

```bash
git clone https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator.git
cd Mine_Microgrid_Simulator
pip install -r requirements.txt
```

### 使用

```bash
streamlit run app.py
pytest tests/
```

## 项目结构

```
modules/  scripts/
tests/  docs/
```

## 说明

工程研究演示，非并网规范合规产品。

## 许可证

MIT。在注明出处的前提下可商业使用（以 LICENSE 为准）。详见 [LICENSE](LICENSE)。
