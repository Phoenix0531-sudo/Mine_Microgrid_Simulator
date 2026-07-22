# Mine Microgrid Simulator

**矿区可再生 + 微电网情景的 Streamlit 规划器**

[English](README.md) | [中文](README.zh-CN.md)

![CI](https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

交互式 **Streamlit** 应用：对矿区可再生发电与微电网调度做粗规划——负荷曲线、风光功率估算、仿真运行与结果面板。

## 为什么做这个

矿区能源规划在上完整电力系统软件前，需要快速情景工具。本应用把负荷/气象辅助与仿真引擎收进浏览器 UI。

## 功能

- 侧栏情景输入与校验  
- 光伏 / 风电估算模块  
- 异步任务与进度 UI 钩子  
- 结果分析视图  

## 安装

```bash
git clone https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator.git
cd Mine_Microgrid_Simulator
pip install -r requirements.txt
```

## 使用

```bash
streamlit run app.py
# Windows 也可用 start.bat
```

## 目录结构

```
app.py
modules/
tests/
```

## 明确不做

- 非认证电网研究软件  
- 非实时 EMS / SCADA  

## 许可证

MIT。可在署名前提下商用。见 [LICENSE](LICENSE)。
