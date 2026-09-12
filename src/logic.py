import pandas as pd


class DataHandler:
    """Handles data loading, cleaning, and persistence with error handling."""

    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.filepath)
            print(f"Successfully loaded {self.filepath} ({len(self.df)} rows).")
        except FileNotFoundError:
            print(
                f"Error: The file '{self.filepath}' was not found. Please verify the path."
            )
            self.df = pd.DataFrame()
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            self.df = pd.DataFrame()
        return self.df

    def clean_data(self):
        if self.df is not None and not self.df.empty:
            self.df["DnsAnswer"] = self.df["DnsAnswer"].fillna("None")
            self.df["DnsAnswerTTL"] = self.df["DnsAnswerTTL"].fillna("0")
            self.df["Timestamp"] = pd.to_datetime(self.df["Timestamp"])
        return self.df