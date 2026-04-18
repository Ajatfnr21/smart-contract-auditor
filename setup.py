from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="smart-contract-auditor",
    version="0.1.0",
    author="Drajat Sukma",
    author_email="drajatsukmacareer@gmail.com",
    description="AI-powered smart contract security auditor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ajatfnr21/smart-contract-auditor",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Security",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=[
        "web3>=6.0.0",
        "eth-account>=0.8.0",
        "slither-analyzer>=0.9.0",
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "pandas>=2.0.0",
        "pyyaml>=6.0",
        "requests>=2.28.0",
        "rich>=13.0.0",
        "typer>=0.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.3.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "smart-contract-auditor=smart_contract_auditor.cli:main",
        ],
    },
)
