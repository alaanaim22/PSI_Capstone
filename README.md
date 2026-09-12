# DNS Intrusion Detection System (IDS) Capstone Project

A modular, object-oriented Python application designed to parse, clean, analyze, and visualize network security telemetry data from DNS logs to detect suspicious and malicious activity.

## Key Features
- **Object-Oriented Architecture**: Clean separation of concerns into distinct classes (`DataHandler`, `ThreatAnalyzer`, `SecurityUtils`).
- **Data Integrity & Management**: Robust loading, cleaning, and SHA-256 integrity hashing of telemetry datasets.
- **Threat Intelligence**: Automated identification of top offending source IPs and malicious DNS queries.
- **Visual Analytics**: Automated generation of dual-panel visual reports (`seaborn`/`matplotlib`) illustrating query distributions and threat classifications.
- **Unit Testing**: Automated test suites powered by `pytest`.

## Project Structure
capstone_project/
├── data/
│   └── sample_data.csv
├── src/
│   ├── main.py
│   ├── logic.py
│   ├── models.py
│   └── utils.py
├── tests/
│   └── test_logic.py
├── dns_security_report.png
├── requirements.txt
└── README.md


## Installation & Setup
1. Clone or download the repository to your local machine.
2. Install the required external dependencies using pip:
   pip install -r requirements.txt

Running the Application
Navigate to the source directory and execute the main pipeline entry point:

Bash
cd src
python main.py

This will parse the dataset, output threat summaries to the console, compute the SHA-256 file hash, and generate the dns_security_report.png visualization.

Running Tests
To verify individual components using the automated test suite, execute pytest from the root project directory:

Bash
pytest