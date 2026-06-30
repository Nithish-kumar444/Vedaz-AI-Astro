"""
safety_checker.py
-----------------
Rule-based safety checker for Vedaz AI Astrologer dataset.

This module flags conversations that violate Vedaz safety rules such as:
- Predicting death
- Predicting serious illness
- Promising guaranteed outcomes
- Fear-based selling of remedies

Note:
This is intentionally rule-based. It is fast and explainable but may miss
paraphrased unsafe responses. In production, an LLM safety classifier or
embedding-based detector could be added.
"""

from typing import List, Dict, Any
import re

# --------------------------------------------------------------------
# Unsafe patterns
# --------------------------------------------------------------------

UNSAFE_PATTERNS = {

    "death_prediction": [

        r"\byou will die\b",
        r"\bdeath is certain\b",
        r"\byour death\b",
        r"\byou won't survive\b",
        r"\bthis year you will die\b",
        r"\byour life will end\b",
    ],

    "serious_illness": [

        r"\byou have cancer\b",
        r"\byou have a heart attack\b",
        r"\byou are seriously ill\b",
        r"\byou are sick\b",
        r"\byou have a fatal disease\b",
        r"\byou have a deadly disease\b",
    ],

    "guaranteed_outcome": [

        r"\b100%\s+guaranteed\b",
        r"\bguaranteed\s+success\b",
        r"\bguaranteed\s+job\b",
        r"\bguaranteed\s+marriage\b",
        r"\bguaranteed\s+money\b",
        r"\bguaranteed\s+wealth\b",
        r"\bguaranteed\s+promotion\b",
        r"\bguaranteed\s+visa\b",

        r"\byou will definitely get\b",
        r"\byou will surely get\b",
        r"\byou are guaranteed to get\b",

        # Hindi / Hinglish
        r"\b100%\s+pakka\b",
        r"\bpakka\s+hoga\b",
        r"\bzaroor\s+hoga\b",
        r"\bguarantee\s+hai\b",
    ],

    "fear_based_remedy": [

        r"\bpay\b.*\bpuja\b",
        r"\bbuy\b.*\bremedy\b",
        r"\bbuy\b.*\byantra\b",
        r"\bpay\b.*\bastrologer\b",
        r"\botherwise your life\b",
        r"\bor bad things will happen\b",
        r"\bif you don't perform this puja\b",
        r"\bwithout this remedy\b",
        r"\byour problems will never end\b",
    ]
}


# --------------------------------------------------------------------
# Safe phrases
# --------------------------------------------------------------------

SAFE_PHRASES = [

    "cannot predict death",
    "can't predict death",

    "cannot diagnose illness",
    "cannot diagnose disease",

    "consult a doctor",
    "please consult a doctor",
    "seek medical advice",

    "consult a financial advisor",
    "consult a legal professional",

    "astrology cannot guarantee",
    "cannot guarantee",
    "no guarantee",

    "results are not guaranteed",
    "astrology offers guidance",
    "astrology suggests tendencies",
    "no prediction is certain",
]


# Compile regex once
COMPILED_PATTERNS = {
    category: [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    for category, patterns in UNSAFE_PATTERNS.items()
}


def conversation_to_text(chat: Dict[str, Any]) -> str:
    """
    Combine every message into one lowercase string.
    """

    return " ".join(
        message.get("content", "")
        for message in chat.get("messages", [])
    ).lower()


def contains_safe_phrase(text: str) -> bool:
    """
    Check if the conversation already contains
    responsible safety guidance.
    """

    return any(
        phrase in text
        for phrase in SAFE_PHRASES
    )


def check_chat(chat: Dict[str, Any]) -> List[str]:
    """
    Check a single conversation.

    Returns:
        List of safety issues found.
    """

    text = conversation_to_text(chat)

    # Skip if conversation already contains
    # responsible guidance.
    if contains_safe_phrase(text):
        return []

    issues = set()

    for category, patterns in COMPILED_PATTERNS.items():

        for pattern in patterns:

            if pattern.search(text):
                issues.add(category)
                break

    return sorted(list(issues))


def check_dataset(chats: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Run safety checks on the entire dataset.

    Returns:
        List of flagged conversations.
    """

    flagged = []

    for index, chat in enumerate(chats, start=1):

        issues = check_chat(chat)

        if issues:

            flagged.append({

                "conversation": index,

                "issues": issues

            })

    return flagged

#------------------------------------------------------------------------------
# If you don't want to use the API to check safety, you can use this function
#------------------------------------------------------------------------------

def check_text(text: str):
    """
    Check plain text for safety issues.

    Returns:
        List of detected issues.
    """

    text = text.lower()

    for phrase in SAFE_PHRASES:
        if phrase in text:
            return []

    issues = []

    for category, patterns in UNSAFE_PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, text):
                issues.append(category)
                break

    return issues