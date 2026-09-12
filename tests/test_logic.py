import os
import sys

# Add the 'src' directory to the front of Python's path because it isnt seeing the logic.py and models.py files
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pandas as pd
from logic import DataHandler
from models import ThreatAnalyzer


def test_data_handler_cleaning():
    handler = DataHandler("data/sample_data.csv")
    df = handler.load_data()
    df = handler.clean_data()
    assert not df.empty
    assert "DnsAnswer" in df.columns


def test_threat_analyzer_stats():
    data = {
        "SourceIP": ["10.0.0.1", "10.0.0.2"],
        "DnsQuery": ["example.com", "malicious.com"],
        "sus": [0, 1],
        "evil": [0, 1],
    }
    df = pd.DataFrame(data)
    analyzer = ThreatAnalyzer(df)
    stats = analyzer.get_summary_stats()

    assert stats["total"] == 2
    assert stats["suspicious"] == 1
    assert stats["malicious"] == 1