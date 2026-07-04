# python-for-ai

Foundational Python work from a focused fundamentals course — the groundwork for building AI tooling. Kept public as an honest record of learning in progress.

## Contents

- **`python/`** — core Python: classes and OOP (`hello.py`), standard-library modules and a creatinine-clearance calculator (`interactive_demo.py`), and a live API + data-viz script that pulls weather data from the free Open-Meteo API and charts it with pandas + matplotlib (`working_api.py`).
- **`sales_analysis/`** — a small pandas ETL exercise: read a CSV, compute totals, and export to JSON, Excel, and CSV.

## Running

```bash
pip install pandas matplotlib requests openpyxl
python python/working_api.py
python sales_analysis/analyzer.py
```

No API keys required — the weather API is open access.
