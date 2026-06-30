from core.dataset import load_dataset
from core.validator import validate_dataset
from core.statistics import calculate_statistics
from core.duplicate_detector import find_duplicates
from core.safety_checker import check_dataset
from core.splitter import split_and_save
from core.report_generator import generate_report


def main():

    # Load dataset
    chats = load_dataset()

    # Validate dataset
    validation = validate_dataset(chats)

    # Calculate statistics
    stats = calculate_statistics(chats)

    # Detect duplicates
    duplicates = find_duplicates(chats)

    # Safety check
    safety = check_dataset(chats)

    # Split dataset
    split = split_and_save(chats)

    # Generate report
    report_file = generate_report(
        validation,
        stats,
        duplicates,
        safety,
        split,
    )

    print("=" * 60)
    print("VEDAZ DATASET CHECKER")
    print("=" * 60)

    print("\n✅ Dataset Loaded Successfully")
    print(f"Total Conversations : {len(chats)}")

    print("\nValidation Report")
    print("-" * 30)
    print(f"Valid Conversations   : {validation['valid']}")
    print(f"Invalid Conversations : {validation['invalid']}")

    if validation["errors"]:
        print("\nValidation Errors:")
        for error in validation["errors"]:
            print("-", error)
    else:
        print("No validation errors found.")

    print("\nDataset Statistics")
    print("-" * 30)

    for key, value in stats.items():
        print(f"{key:22}: {value}")

    print("\nDuplicate Detection")
    print("-" * 30)

    if duplicates:
        for duplicate in duplicates:
            print(
                f"Conversation {duplicate['conversation_1']} "
                f"and Conversation {duplicate['conversation_2']} "
                f"(Similarity: {duplicate['similarity']})"
            )
    else:
        print("No duplicate conversations found.")

    print("\nSafety Check")
    print("-" * 30)

    if safety:
        for issue in safety:
            print(
                f"Conversation {issue['conversation']} "
                f"-> {', '.join(issue['issues'])}"
            )
    else:
        print("No unsafe conversations found.")

    print("\nTrain/Test Split")
    print("-" * 30)
    print(f"Training Chats : {split['train_size']}")
    print(f"Testing Chats  : {split['test_size']}")

    print("\nReport Generated")
    print("-" * 30)
    print(report_file)


if __name__ == "__main__":
    main()