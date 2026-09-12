from collections import Counter
import pandas as pd


class ThreatAnalyzer:
    """Contains the code for analyzing security data."""

    def __init__(self, df):
        self.df = df

    def get_top_offending_ips(self, top_n=3):
        if self.df.empty:
            return []
        threat_df = self.df[(self.df["sus"] == 1) | (self.df["evil"] == 1)]
        return Counter(threat_df["SourceIP"].tolist()).most_common(top_n)

    def get_malicious_queries(self, top_n=3):
        if self.df.empty:
            return []
        evil_df = self.df[self.df["evil"] == 1]
        return Counter(evil_df["DnsQuery"].tolist()).most_common(top_n)

    def get_summary_stats(self):
        if self.df.empty:
            return {}
        return {
            "total": len(self.df),
            "suspicious": int(self.df["sus"].sum()),
            "malicious": int(self.df["evil"].sum()),
        }