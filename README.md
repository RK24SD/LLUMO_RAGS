# LLUMO_RAGS
# LLUMO AI Assignment – RAGAS Integration by Raj k 

Hi there! this project is my solution for integrating RAGAS metrics into a JSON log of LLM responses. The goal was to go beyond surface-level answers and measure how well the model held up in terms of **faithfulness**, **answer relevancy**, and **context precision**. Here's how I tackled it:

---

##  What's Inside
| File               | Purpose |
|--------------------|--------|
| `logs.json`         | Raw LLM logs with system/user prompts and model responses |
| `ragas_input.json`  | Reformatted entries to align with RAGAS expectations |
| `ragas_scores.json` | Output file with computed RAGAS metrics for each item |
| `rags_preprocess.py`| Script to parse, clean, and prepare data |
| `rags_evaluate.py`  | Script to run evaluation and generate scores |

______

##  Libraries I Used
- [`ragas`](https://pypi.org/project/ragas/) – the core metric engine  
- `datasets` – to build and manage evaluation examples  
- `json` – because everything talks in JSON here 
_________

##  My Approach
1. **Preprocessing**  
   - Extracted `context` from the **system prompt**
   - Treated `query` as the **user prompt**
   - Used the model’s response as `prediction`
   - Ground truth wasn't provided, so the metrics rely on the original context-query structure

2. **Evaluation**  
   - Used RAGAS to compute the three metrics per item
   - Exported everything cleanly into `ragas_scores.json` for easy consumption  

________

##  Assumptions I Made
- The **system role** serves as _context_ for the query  
- The **user role** acts as the actual _query_  
- Model predictions are evaluated without hard ground truth (given the constraints)  
- Focused on logic clarity and reproducibility over cosmetic perfection  

_______

## 🧪 How to Run This
If you'd like to test or replicate this yourself:
```bash
pip install ragas datasets
python rags_preprocess.py
python rags_evaluate.py
