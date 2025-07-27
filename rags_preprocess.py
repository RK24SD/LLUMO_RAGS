import json
from typing import List, Dict


def load_logs(file_path: str) -> List[Dict]:
    """Load and parse the JSON log file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(f"Loaded {len(data)} entries from {file_path}")
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in {file_path}")


def transform_for_ragas(logs: List[Dict]) -> List[Dict]:
    """Extract context, query, and response for RAGAs evaluation."""
    transformed = []
    for entry in logs:
        transformed.append({
            "id": entry.get("id", "unknown"),
            "context": entry.get("input", {}).get("system", "").strip(),
            "query": entry.get("input", {}).get("user", "").strip(),
            "response": entry.get("expected_output", "").strip()
        })
    print(f"Transformed {len(transformed)} entries for RAGAs processing")
    return transformed


def save_transformed(data: List[Dict], output_path: str) -> None:
    """Save the transformed data into a new JSON file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)
            print(f"Saved RAGAs-ready data to {output_path}")
    except IOError:
        raise IOError(f"Failed to write data to {output_path}")


def main():
    input_path = "logs.json"
    output_path = "ragas_input.json"

    logs = load_logs(input_path)
    ragas_ready = transform_for_ragas(logs)
    save_transformed(ragas_ready, output_path)


if __name__ == "__main__":
    main()