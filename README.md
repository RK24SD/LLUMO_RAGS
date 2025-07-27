# LLUMO_RAGS
# LLUMO AI Assignment – RAGAS Integration by Raj k 
This project was built as part of the **LLUMO AI assignment**, and I’ve kept it clean, modular, and reproducible for future adaptation.

##  Files Included

| File Name             | Purpose |
|----------------------|--------|
| `logs.json`           | Original LLM logs with system/user prompts and generated outputs |
| `rags_preprocess.py` | Extracts relevant inputs and prepares `ragas_input.json` for scoring |
| `rags_evaluate.py`   | Simulates RAGAS evaluation; computes faithfulness, relevance, and precision |
| `ragas_integration.py` | The pipeline script that ties everything together |
| `ragas_input.json`   | Reformatted entries that act as context-query-prediction triples |
| `ragas_scores.json`  | Final JSON output showing scored metrics per item |
| `README.md`          | This documentation file explaining the whole process |

____________________________________

## ⚙ What Does It Do?

This project:
1. **Loads LLM logs** from JSON.
2. **Transforms input** using system prompts as context, user prompts as query, and LLM response as prediction.
3. **Evaluates entries** (simulated scoring due to model constraints).
4. **Outputs scores** for each item using key metrics.

Sample output:
'''json
{
  "id": "item-007",
  "faithfulness": 0.89,
  "answer_relevancy": 0.85,
  "context_precision": 0.91
}
These scores are saved inside ragas_scores.json.

==How to Run It
Install dependencies (if needed): 
#bash
pip install pandas json tqdm random

==Run the pipeline:
#bash
python ragas_integration.py

_________
That will:

Load logs.json

Generate ragas_input.json

Create output scores in ragas_scores.json
Each stage prints clean logs so you can track progress step by step.
__________________

Assumptions I Made
The system role serves as context for the query
The user role acts as the actual query
Model predictions are evaluated without hard ground truth (given the constraints)
Focused on logic clarity and reproducibility over cosmetic perfection

___________________


---
Conatct  - raghavrajk24@gmail.com 
