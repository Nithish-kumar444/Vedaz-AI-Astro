"""
validator.py
-------------
Validates the dataset structure.
"""

from typing import List, Dict, Any

ALLOWED_ROLES = {"system", "user", "assistant"}


def validate_dataset(chats: List[Dict[str, Any]]) -> dict:
    """
    Validate all conversations in the dataset.

    Returns:
        dict: Validation summary.
    """

    valid = 0
    invalid = 0
    errors = []

    for conversation_number, chat in enumerate(chats, start=1):

        # Check if "messages" key exists
        if "messages" not in chat:
            invalid += 1
            errors.append(
                f"Conversation {conversation_number}: Missing 'messages'"
            )
            continue

        messages = chat["messages"]

        # Check if messages is a list
        if not isinstance(messages, list):
            invalid += 1
            errors.append(
                f"Conversation {conversation_number}: 'messages' should be a list"
            )
            continue

        # Check if messages list is empty
        if len(messages) == 0:
            invalid += 1
            errors.append(
                f"Conversation {conversation_number}: Empty messages list"
            )
            continue

        conversation_ok = True

        # Check each message has role/content and valid role
        for message_number, message in enumerate(messages, start=1):

            if "role" not in message:
                conversation_ok = False
                errors.append(
                    f"Conversation {conversation_number}, Message {message_number}: Missing role"
                )
                break

            if "content" not in message:
                conversation_ok = False
                errors.append(
                    f"Conversation {conversation_number}, Message {message_number}: Missing content"
                )
                break

            if message["role"] not in ALLOWED_ROLES:
                conversation_ok = False
                errors.append(
                    f"Conversation {conversation_number}, Message {message_number}: Invalid role '{message['role']}'"
                )
                break

        # Skip further checks if already invalid
        if not conversation_ok:
            invalid += 1
            continue

        # First message must be system
        if messages[0]["role"] != "system":
            invalid += 1
            errors.append(
                f"Conversation {conversation_number}: First message must be 'system'"
            )
            continue

        # Check alternating user -> assistant pattern
        expected_role = "user"

        for index in range(1, len(messages)):
            current_role = messages[index]["role"]

            if current_role != expected_role:
                invalid += 1
                errors.append(
                    f"Conversation {conversation_number}: Expected '{expected_role}' "
                    f"at message {index + 1}, found '{current_role}'"
                )
                conversation_ok = False
                break

            # Toggle expected role
            expected_role = (
                "assistant"
                if expected_role == "user"
                else "user"
            )

        if conversation_ok:
            valid += 1

    return {
        "valid": valid,
        "invalid": invalid,
        "errors": errors,
    }