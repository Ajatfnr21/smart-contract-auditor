<div align="center">

# 🔍 Smart Contract Auditor

**AI-powered smart contract security auditor with automated vulnerability detection and risk analysis**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

</div>

---

## 🚀 Overview

Smart Contract Auditor is an advanced security analysis engine that uses AI and static analysis to detect vulnerabilities in Ethereum smart contracts. Inspired by industry-leading tools like Slither and Mythril, with enhanced pattern recognition and automated exploit generation.

### Key Features

- 🔍 **Multi-Scanner Architecture**: Taint analysis, hypothesis testing, and invariant detection
- 🤖 **AI-Powered Detection**: Machine learning models for vulnerability pattern recognition
- 📝 **Automated Reports**: Generate detailed security reports with risk ratings
- ⚡ **High Performance**: Parallel processing for large codebases
- 🎯 **Exploit Generation**: Proof-of-concept generation for detected vulnerabilities

---

## 📁 Project Structure

```
smart-contract-auditor/
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── analyzer.py          # Main analysis engine
│   │   ├── detector.py          # Vulnerability detectors
│   │   └── engine.py            # Core audit engine
│   ├── scanners/
│   │   ├── __init__.py
│   │   ├── taint_scanner.py     # Taint analysis
│   │   ├── hypothesis_scanner.py # Hypothesis testing
│   │   └── invariant_scanner.py  # Invariant detection
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── model.py             # ML models
│   │   └── trainer.py           # Model training
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   └── test_vulnerabilities/
├── docs/
│   └── ARCHITECTURE.md
├── examples/
│   └── sample_contracts/
├── requirements.txt
├── setup.py
└── README.md
```

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/Ajatfnr21/smart-contract-auditor.git
cd smart-contract-auditor

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

---

## 💻 Usage

### Basic Usage

```python
from smart_contract_auditor import Auditor

# Initialize auditor
auditor = Auditor()

# Analyze contract
result = auditor.analyze("path/to/contract.sol")

# Generate report
report = auditor.generate_report(result)
print(report)
```

### Command Line Interface

```bash
# Analyze a single contract
python -m smart_contract_auditor analyze contract.sol

# Analyze with specific detectors
python -m smart_contract_auditor analyze contract.sol --detectors reentrancy,overflow

# Generate detailed report
python -m smart_contract_auditor analyze contract.sol --output report.json
```

---

## 🔍 Detected Vulnerabilities

| Severity | Vulnerability | Description |
|----------|---------------|-------------|
| 🔴 Critical | Reentrancy | External calls before state updates |
| 🔴 Critical | Integer Overflow | Arithmetic overflow/underflow |
| 🟠 High | Unchecked External Calls | Return values not checked |
| 🟠 High | Timestamp Dependence | Block.timestamp reliance |
| 🟡 Medium | Tx.origin Auth | Authentication using tx.origin |
| 🟡 Medium | Block Hash Dependence | Predictable randomness |
| 🟢 Low | Floating Pragma | Non-strict version pragma |
| 🟢 Low | Unused Variables | Dead code elimination |

---

## 🤖 AI Components

- **Pattern Recognition**: Transformer-based model for vulnerability patterns
- **Risk Scoring**: Gradient boosting for risk assessment  
- **Exploit Generation**: Seq2Seq model for PoC generation

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">

**Made with ❤️ by [Drajat Sukma](https://github.com/Ajatfnr21)**

</div>
