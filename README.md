<div align="center">

# 🚀 AutoEDA - Automated Exploratory Data Analysis

**One function call for comprehensive data analysis and visualization**

[![PyPI version](https://badge.fury.io/py/autoeda-sujay.svg)](https://badge.fury.io/py/autoeda-sujay)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/autoeda-sujay)](https://pepy.tech/project/autoeda-sujay)

[Installation](#installation) • [Quick Start](#quick-start) • [Features](#features) • [Examples](#examples) • [Contributing](#contributing)

</div>

---

## 📋 Overview

AutoEDA is a Python library that automates the entire exploratory data analysis process with a single function call. Perfect for data scientists, analysts, and researchers who want comprehensive insights without writing repetitive analysis code.

## ✨ Features

- 📊 **Dataset Overview** - Shape, data types, memory usage analysis
- ❌ **Missing Data Analysis** - Comprehensive missing value detection and visualization
- 📈 **Statistical Summary** - Descriptive statistics for all numerical columns
- 📊 **Distribution Analysis** - Automated histograms and distribution plots
- 🔗 **Correlation Matrix** - Interactive correlation heatmaps
- 🎯 **Outlier Detection** - Automatic identification of data anomalies
- 📝 **Categorical Analysis** - Value counts and frequency analysis
- 🚀 **One-Line Usage** - Complete analysis with `autoeda.analyze(df)`

## 🛠️ Installation

### From PyPI (Recommended)
\`\`\`bash
pip install autoeda-sujay
\`\`\`

### From Source
\`\`\`bash
git clone https://github.com/yourusername/autoeda.git
cd autoeda
pip install -e .
\`\`\`

## 🚀 Quick Start

```python
import pandas as pd
import autoeda

# Load your data
df = pd.read_csv('your_data.csv')

# One function call does everything!
report = autoeda.analyze(df)

# View comprehensive summary
report.show_summary()

# Generate visualizations
report.plot_missing_data()
report.plot_distributions()
report.plot_correlation_matrix()
