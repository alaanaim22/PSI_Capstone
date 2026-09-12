from logic import DataHandler
from models import ThreatAnalyzer
from utils import SecurityUtils


def main():
    filename = "data/sample_data.csv"

    # 1. Initialize data handling with error management
    handler = DataHandler(filename)
    df = handler.load_data()
    if df.empty:
        return
    df = handler.clean_data()

    # 2. Execute OOP logic
    analyzer = ThreatAnalyzer(df)
    print("Top Offending Source IPs:", analyzer.get_top_offending_ips())
    print("Malicious DNS Queries:", analyzer.get_malicious_queries())
    print("Threat Summary:", analyzer.get_summary_stats())

    # 3. Utilities & Reporting
    utils = SecurityUtils()
    file_hash = utils.compute_file_hash(filename)
    utils.generate_visual_report(df, "dns_security_report.png")
    print(f"SHA-256 Digest: {file_hash}")


if __name__ == "__main__":
    main()