"""Command-line interface for Smart Contract Auditor."""

import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table

from .core.analyzer import Auditor

app = typer.Typer(help="Smart Contract Auditor CLI")
console = Console()


@app.command()
def analyze(
    contract: Path = typer.Argument(..., help="Path to Solidity contract"),
    output: Path = typer.Option(None, "--output", "-o", help="Output file path"),
    detectors: str = typer.Option(None, "--detectors", "-d", help="Comma-separated detector list")
):
    """Analyze a smart contract for vulnerabilities."""
    console.print(f"[bold blue]Analyzing {contract}...[/bold blue]")
    
    auditor = Auditor()
    results = auditor.analyze(str(contract))
    report = auditor.generate_report(results)
    
    if output:
        output.write_text(report)
        console.print(f"[bold green]Report saved to {output}[/bold green]")
    else:
        console.print(report)


@app.command()
def version():
    """Show version information."""
    console.print("[bold]Smart Contract Auditor v0.1.0[/bold]")


def main():
    """Entry point for CLI."""
    app()


if __name__ == "__main__":
    main()
