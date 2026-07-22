# Mine Microgrid Simulator

**Streamlit + Plotly microgrid planning demo for mining scenarios.**

[English](README.md) | [中文](README.zh-CN.md)

[![CI](https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator/actions/workflows/ci.yml/badge.svg)](https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Interactive charts and scenario modules for engineering study.

## Preview

![Mine Microgrid Simulator](docs/screenshots/preview.png)

## Features

- Microgrid planning oriented modules
- Plotly interactive charts
- Streamlit app entry
- CI smoke + tests

## Get started

### Install

```bash
git clone https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator.git
cd Mine_Microgrid_Simulator
pip install -r requirements.txt
```

### Usage

```bash
streamlit run app.py
pytest tests/
```

## Project layout

```
modules/  scripts/
tests/  docs/
```

## Notes

Engineering study demo, not a grid-code compliance product.

## License

MIT. Free for commercial use with attribution where applicable. See [LICENSE](LICENSE).
