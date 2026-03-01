"""
Sub-package for small analyst agents.

Avoid importing the parent `agent` module here to prevent a circular
import when `financial_advisor.agent` imports these sub-agents.

Expose the sub-agent objects for convenience.
"""

from .data_analyst import data_analyst
from .financial_analyst import financial_analyst
from .news_analyst import news_analyst