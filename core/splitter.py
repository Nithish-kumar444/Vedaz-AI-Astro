"""
splitter.py
------------
Splits dataset into training and test sets.
"""

import json
from pathlib import Path
from typing import List, Dict, Any, Tuple


PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_DIR = PROJECT_ROOT / "outputs"

TRAIN_FILE = OUTPUT_DIR / "train.jsonl"
TEST_FILE = OUTPUT_DIR / "test.jsonl"


def split_dataset(
    chats: List[Dict[str, Any]],
    train_ratio: float = 0.8
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Split dataset into train and test sets.
    """

    split_index = int(len(chats) * train_ratio)

    train_data = chats[:split_index]
    test_data = chats[split_index:]

    return train_data, test_data


def save_jsonl(
    chats: List[Dict[str, Any]],
    output_file: Path
):
    """
    Save conversations to a JSONL file.
    """

    OUTPUT_DIR.mkdir(exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:

        for chat in chats:

            json.dump(chat, file, ensure_ascii=False)

            file.write("\n")


def split_and_save(chats: List[Dict[str, Any]]):
    """
    Split dataset and save both files.
    """

    train_data, test_data = split_dataset(chats)

    save_jsonl(train_data, TRAIN_FILE)

    save_jsonl(test_data, TEST_FILE)

    return {
        "train_size": len(train_data),
        "test_size": len(test_data),
        "train_file": str(TRAIN_FILE),
        "test_file": str(TEST_FILE),
    }