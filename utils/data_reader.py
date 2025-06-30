import json
import csv
from typing import Any, Dict, List

class DataReader:
    """Utility class for reading test data from JSON and CSV files."""

    @staticmethod
    def read_json(file_path: str) -> Any:
        """Read and return data from a JSON file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def read_csv(file_path: str) -> List[Dict[str, Any]]:
        """Read and return data from a CSV file as a list of dictionaries."""
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)