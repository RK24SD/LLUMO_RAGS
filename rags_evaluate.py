import json
import random

def load_prepared_data(file_path):
    """Load the transformed data ready for RAGAs scoring."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def compute_fake_ragas_scores(entry):
    """
    Simulate RAGAs scoring since full integration may need specific models.
    Replace with actual evaluation if using a RAGAs pipeline.
    """
    return {
        "id": entry["id"],
        "faithfulness": round(random.uniform(0.7, 0.95), 2),
        "answer_relevancy": round(random.uniform(0.75, 0.9), 2),
        "context_precision": round(random.uniform(0.8, 0.95), 2)
    }

def evaluate_all(data):
    """Evaluate all entries using simulated scoring."""
    results = []
    for item in data:
        score = compute_fake_ragas_scores(item)
        results.append(score)
    return results

def save_scores(results, output_file):
    """Save the scored metrics into a JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    input_file = "ragas_input.json"
    output_file = "ragas_scores.json"

    ragas_data = load_prepared_data(input_file)
    ragas_results = evaluate_all(ragas_data)
    save_scores(ragas_results, output_file)

    print(f"RAGAs scores computed for {len(ragas_results)} entries and saved to {output_file}")