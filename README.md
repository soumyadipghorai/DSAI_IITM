# DSAI — IIT M

A personal collection of data science, machine learning, deep learning, and NLP projects, experiments, and course notebooks. The workspace gathers coursework, example datasets, model checkpoints, and small apps used for learning and demonstration.

## Contents

- **computer_vision/** — Notebooks and datasets for image tasks (example: [week4.ipynb](computer_vision/week4.ipynb)).
- **deep_learning/** — Deep learning notebooks and the `PlantVillage` dataset used for classification experiments.
- **LM_finetuning/** — Checkpoints and tokenizer for language-model fine-tuning experiments.
- **docker_kubernetes/** — Small Flask app and deployment notes; includes a saved model `model.joblib`.
- **machine_learning/** — Classic ML datasets and notebooks (e.g., `mnist_train_small.csv`).
- **Data_visualization/**, **time_series_forecasting/**, **prompt_engineering/**, **RAG/**, **LangGraph/** — Additional topic-focused notebooks and resources.

## Quickstart

1. Install Python (3.9+ recommended) and create a virtual environment:

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install --upgrade pip
```

2. Install common dependencies used across notebooks:

```bash
pip install jupyterlab numpy pandas matplotlib scikit-learn torch torchvision transformers seaborn opencv-python
```

3. Start JupyterLab and open the notebooks:

```bash
jupyter lab
```

Notes:
- Not every folder has a centralized `requirements.txt`. Install additional packages shown at the top of each notebook as needed.
- Large model checkpoints (under `LM_finetuning/`) may require GPU and sufficient disk space.

## Notable Files

- [computer_vision/week4.ipynb](computer_vision/week4.ipynb) — Example CV notebook using the hymenoptera dataset.
- [docker_kubernetes/app.py](docker_kubernetes/app.py) — Small FastAPI demo and notes in [docker_kubernetes/commands.md](docker_kubernetes/commands.md).

## Suggested Workflow

- Use a virtual environment per project or a shared environment for quick experiments.
- For reproducible experiments, add a `requirements.txt` in the folder containing a notebook or create an isolated conda environment and export it.
- When working with large models, move checkpoints to external storage or mount a drive to avoid filling the workspace.

## License & Contact

This collection is for educational use. If you want help turning any notebook into a reproducible script or packaging a model, tell me which folder to start with.

---
Updated: February 11, 2026
