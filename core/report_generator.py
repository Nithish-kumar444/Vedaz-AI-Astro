"""
report_generator.py
-------------------
Generates a summary report for the dataset.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "outputs"
REPORT_FILE = OUTPUT_DIR / "report.txt"


def generate_report(
    validation_result,
    statistics_result,
    duplicate_result,
    safety_result,
    split_result,
):
    """
    Generate a text report summarizing the dataset.
    """

    OUTPUT_DIR.mkdir(exist_ok=True)

    with open(REPORT_FILE, "w", encoding="utf-8") as file:

        file.write("VEDAZ AI ENGINEER - DATASET REPORT\n")
        file.write("=" * 50 + "\n\n")

        # Validation
        file.write("VALIDATION\n")
        file.write("-" * 20 + "\n")
        file.write(f"Valid Chats   : {validation_result['valid']}\n")
        file.write(f"Invalid Chats : {validation_result['invalid']}\n\n")

        # Statistics
        file.write("STATISTICS\n")
        file.write("-" * 20 + "\n")
        file.write(f"Total Conversations : {statistics_result['total_conversations']}\n")
        file.write(f"Total Messages      : {statistics_result['total_messages']}\n")
        file.write(f"Average Messages    : {statistics_result['average_messages']}\n")
        file.write(f"Average Words       : {statistics_result['average_words']}\n")
        file.write(f"Shortest Chat       : {statistics_result['shortest_chat']} words\n")
        file.write(f"Longest Chat        : {statistics_result['longest_chat']} words\n\n")

        # Duplicates
        file.write("DUPLICATES\n")
        file.write("-" * 20 + "\n")
        file.write(f"Duplicate Pairs Found : {len(duplicate_result)}\n\n")

        # Safety
        file.write("SAFETY CHECK\n")
        file.write("-" * 20 + "\n")
        file.write(f"Unsafe Conversations : {len(safety_result)}\n\n")

        # Split
        file.write("TRAIN / TEST SPLIT\n")
        file.write("-" * 20 + "\n")
        file.write(f"Training Chats : {split_result['train_size']}\n")
        file.write(f"Testing Chats  : {split_result['test_size']}\n")

    return REPORT_FILE