# Apache Log Analyzer

This is a command-line tool that reads Apache log files in **Combined Log Format** and outputs useful web traffic statistics.

---

## 📊 Features

- ✅ Total number of requests
- ✅ Total data transmitted (bytes)
- ✅ Most requested resource (and its percentage)
- ✅ Top remote host (and its percentage)
- ✅ Status code class percentages (1xx, 2xx, 3xx, 4xx, 5xx)
- ✅ Ignores unparseable lines gracefully

---

## 🛠 Requirements

- Python 3.6+
- Only uses standard libraries:
  - `argparse`
  - `logging`
  - `re`
  - `collections`

> ✅ No external packages needed

---

## 🚀 Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/priyesh2912/onclusive_assessment.git

2. cd to project directory: 
   cd apache-log-stats

3. Install requirements:
   pip install -r requirements.txt

4. Generate a test log file (if not exist)
   python scripts/generate-logs.py -f logs/generated.log

5. Run tool:
   python log_stats.py logs/generated.log

