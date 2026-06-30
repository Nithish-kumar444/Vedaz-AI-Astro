import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def get_dataset_path():
    """Return the dataset path."""
    return BASE_DIR / "data" / "vedaz_astrologer_finetune.jsonl"


def load_dataset():
    """Load all conversations from the JSONL dataset."""

    dataset_path = get_dataset_path()

    chats = []

    with open(dataset_path, "r", encoding="utf-8") as file:
        for line in file:
            chats.append(json.loads(line))

    return chats