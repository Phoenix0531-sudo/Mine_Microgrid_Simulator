# Mine Microgrid Simulator

**Streamlit planner for mine renewable + microgrid scenarios**

[English](README.md) | [中文](README.zh-CN.md)

![CI](https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Interactive **Streamlit** app for rough planning of mine-site renewable generation and microgrid dispatch: load profiles, solar/wind power estimates, simulation run, and result panels.

## Why this exists

Mining-site energy planning needs a quick scenario tool before full power-system software. This app packages load/weather helpers and a simulation engine behind a single browser UI.

## Features

- Sidebar-driven scenario inputs with validation
- Solar / wind power estimation modules
- Async-friendly task helper + progress UI hooks
- Results analyzer views for energy balance style outputs

## Install

```bash
git clone https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator.git
cd Mine_Microgrid_Simulator
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
# or Windows: start.bat
```

## Project layout

```
app.py
modules/          # ui, validation, data_handler, simulation_engine, results_analyzer, ...
tests/
```

## What this is not

- Not a certified grid study tool
- Not a real-time EMS / SCADA replacement

## License

MIT. Free for commercial use with attribution. See [LICENSE](LICENSE).
