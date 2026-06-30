"""
dataset.py
-----------
Loads the astrology dataset from a JSONL file.
"""

import json
from pathlib import Path
from typing import List, Dict, Any


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "data" / "vedaz_astrologer_finetune.jsonl"


def load_dataset() -> List[Dict[str, Any]]:
    """
    Load all conversations from the dataset.

    Returns:
        List of conversation dictionaries.
    """

    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found:\n{DATASET_PATH}"
        )

    chats = []

    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):

            line = line.strip()

            if not line:
                continue

            try:
                chats.append(json.loads(line))

            except json.JSONDecodeError as e:
                print(
                    f"Skipping invalid JSON "
                    f"(Line {line_number}) : {e}"
                )

    return chats