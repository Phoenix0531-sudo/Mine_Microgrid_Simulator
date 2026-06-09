# Mine Microgrid Simulator

<div align="center">

Professional microgrid planning and analysis platform with interactive dashboards.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![Plotly](https://img.shields.io/badge/Plotly-5.0%2B-purple)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>

## Overview

A comprehensive microgrid planning and analysis platform built with Streamlit and Plotly. Designed for mine-site renewable energy systems, providing end-to-end solutions from system modeling to economic analysis.

## Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open http://localhost:8501 in your browser.

## Docker

```bash
docker build -t mine-microgrid .
docker run -p 8501:8501 mine-microgrid python -m streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

## Repository

<https://github.com/Phoenix0531-sudo/Mine_Microgrid_Simulator>

## License

MIT License
