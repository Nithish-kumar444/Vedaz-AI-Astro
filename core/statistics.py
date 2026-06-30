"""
statistics.py
-------------
Calculates dataset statistics.
"""

from typing import List, Dict, Any


def calculate_statistics(chats: List[Dict[str, Any]]) -> dict:
    """
    Calculate statistics for the dataset.
    """

    total_conversations = len(chats)

    # Handle empty dataset
    if total_conversations == 0:
        return {
            "total_conversations": 0,
            "total_messages": 0,
            "average_messages": 0,
            "average_words": 0,
            "shortest_chat": 0,
            "longest_chat": 0,
        }

    total_messages = 0
    word_counts = []

    for chat in chats:
        total_messages += len(chat["messages"])

        words = 0
        for message in chat["messages"]:
            words += len(message["content"].split())

        word_counts.append(words)

    return {
        "total_conversations": total_conversations,
        "total_messages": total_messages,
        "average_messages": round(total_messages / total_conversations, 2),
        "average_words": round(sum(word_counts) / total_conversations, 2),
        "shortest_chat": min(word_counts),
        "longest_chat": max(word_counts),
    }