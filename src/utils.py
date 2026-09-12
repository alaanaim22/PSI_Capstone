import hashlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class SecurityUtils:
    """Utility class for hashing and visualization reporting."""

    def compute_file_hash(self, filepath):
        try:
            with open(filepath, "rb") as f:
                return hashlib.sha256(f.read()).hexdigest()
        except FileNotFoundError:
            return "File not found for hashing."

    def generate_visual_report(self, df, output_path):
        if df.empty:
            print("No data available to plot.")
            return

        sns.set_theme(style="whitegrid")
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        query_types = df["DnsQueryType"].value_counts()
        sns.barplot(
            x=query_types.index,
            y=query_types.values,
            ax=axes[0],
            hue=query_types.index,
            palette="viridis",
            legend=False,
        )
        axes[0].set_title("Distribution of DNS Query Types")

        threat_counts = pd.Series(
            {
                "Benign": len(df[(df["sus"] == 0) & (df["evil"] == 0)]),
                "Suspicious": int(df["sus"].sum()),
                "Malicious": int(df["evil"].sum()),
            }
        )
        sns.barplot(
            x=threat_counts.index,
            y=threat_counts.values,
            ax=axes[1],
            hue=threat_counts.index,
            palette="magma",
            legend=False,
        )
        axes[1].set_title("Dataset Threat Classification")

        plt.tight_layout()
        plt.savefig(output_path)
        print(f"Visual report saved successfully to {output_path}.")