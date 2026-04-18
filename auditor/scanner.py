"""Contract scanner with multiple analysis engines."""

import subprocess
from pathlib import Path
from typing import List, Dict

class ContractScanner:
    """Scan smart contracts with multiple tools."""
    
    def __init__(self, contract_path: str):
        self.path = Path(contract_path)
        self.findings = []
    
    def run_slither(self) -> List[Dict]:
        """Run Slither analysis."""
        try:
            result = subprocess.run(
                ['slither', str(self.path), '--json', '-'],
                capture_output=True,
                text=True
            )
            return [{'tool': 'slither', 'output': result.stdout}]
        except:
            return []
    
    def run_mythril(self) -> List[Dict]:
        """Run Mythril symbolic execution."""
        try:
            result = subprocess.run(
                ['myth', 'analyze', str(self.path), '-o', 'json'],
                capture_output=True,
                text=True,
                timeout=300
            )
            return [{'tool': 'mythril', 'output': result.stdout}]
        except:
            return []
    
    def scan(self) -> List[Dict]:
        """Run all scanners."""
        return self.run_slither() + self.run_mythril()
