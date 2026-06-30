"""
duplicate_detector.py
----------------------
Finds duplicate or near-duplicate conversations.
"""

from typing import List, Dict, Any
from difflib import SequenceMatcher


SIMILARITY_THRESHOLD = 0.90


def conversation_to_text(chat: Dict[str, Any]) -> str:
    """
    Convert a conversation into a single string.
    """

    messages = []

    for message in chat["messages"]:
        messages.append(message["content"])

    return " ".join(messages)


def similarity(text1: str, text2: str) -> float:
    """
    Return similarity score between two strings.
    """

    return SequenceMatcher(None, text1, text2).ratio()


def find_duplicates(chats: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Find duplicate or near-duplicate conversations.

    Returns:
        List of duplicate pairs.
    """

    duplicates = []

    for i in range(len(chats)):

        text1 = conversation_to_text(chats[i])

        for j in range(i + 1, len(chats)):

            text2 = conversation_to_text(chats[j])

            score = similarity(text1, text2)

            if score >= SIMILARITY_THRESHOLD:

                duplicates.append(
                    {
                        "conversation_1": i + 1,
                        "conversation_2": j + 1,
                        "similarity": round(score, 2)
                    }
                )

    return duplicates