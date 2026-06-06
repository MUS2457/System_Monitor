#  System Monitor (CLI)  
A real‑time system metrics monitor built with Python, designed for Unix-like environments.  
This tool collects, displays, analyzes, stores, and visualizes CPU, RAM, and Disk usage using a fully modular backend architecture.

---

##  Features

### 🔹 Real-Time Metrics Display
- Live CPU, RAM, and Disk usage
- Smooth terminal UI using Unix raw mode
- Non-blocking keyboard input
- Auto-refreshing metrics buffer
- stop it by **q**

### 🔹 Graph Visualization
- CPU / RAM / Disk usage graphs
- Live updates
- Stop the graph anytime using **q**, **s**, or **x**

### 🔹 Metrics Analysis Engine
Includes:
- Threshold detection  
- Averages  
- Min/Max  
- Trend detection  
- Volatility analysis  
- and more check the (metrics_analysis.py ) for full picture

All powered by a dedicated `MetricsAnalysis` class.

### 🔹 History System
- View collected metrics history  
- Export history to a `.log` file  
- Read history back from file  

### 🔹 Database Integration
- SQLite backend  
- Save metrics after each display session  
- Query last metrics  
- Query metrics by date range  

### 🔹 Modular Architecture
The project is split into clean, reusable modules:

## project structure

```
CORE/
├── display.py
├── history.py
├── storage.py
├── collector.py
└── scheduler


ANALYSIS/
├── metrics_analysis.py
└── graph.py


DATA/
├── database.py
└── models.py
UTILS/
└── tool.py

main.py

```

## Requirements

- Python 3.10+
- psutil
- matplotlib
- SQLite (built-in)

Install dependencies:

```bash
pip install -r requirements.txt
```
## platform compatibility

 This project works ONLY on Unix-like systems:

Linux

macOS

Windows (WSL2 only)

Not supported on native Windows CMD or PowerShell. (reaseons below)

## The project uses Unix-specific terminal APIs such as: 

termios

tty

select

raw/cbreak terminal modes 