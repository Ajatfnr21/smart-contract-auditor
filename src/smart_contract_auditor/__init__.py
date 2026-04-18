"""Smart Contract Auditor - AI-powered security analysis tool."""

__version__ = "0.1.0"
__author__ = "Drajat Sukma"

from .core.analyzer import Auditor
from .core.engine import AuditEngine

__all__ = ["Auditor", "AuditEngine"]
