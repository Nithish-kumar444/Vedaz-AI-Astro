"""
generator.py
-------------
Generate Vedaz AI training conversations using OpenRouter.
"""

import json
import os
import time

from dotenv import load_dotenv
from openai import OpenAI, RateLimitError

from core.validator import validate_dataset
from core.safety_checker import check_dataset

# ---------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in .env")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

OUTPUT_FILE = "outputs/generated_chats.jsonl"
TOPIC_FILE = "data/topics.txt"

MODEL_NAME = "openai/gpt-oss-20b:free"

TARGET_CONVERSATIONS = 25


# ---------------------------------------------------
# Prompt Builder
# ---------------------------------------------------

def build_prompt(topic):

    return f"""
You are creating training data for Vedaz AI Astrologer.

Generate ONLY ONE conversation.

Topic:
{topic}

Return ONLY valid JSON.

Format:

{{
  "messages":[
    {{
      "role":"system",
      "content":"..."
    }},
    {{
      "role":"user",
      "content":"..."
    }},
    {{
      "role":"assistant",
      "content":"..."
    }}
  ]
}}

Rules:

1. Never predict death.
2. Never predict serious illness.
3. Never guarantee marriage, job, money or success.
4. Never scare the user.
5. Never pressure users to purchase remedies.
6. If health is discussed, recommend consulting a doctor.
7. Astrology gives guidance, not certainty.
8. Be warm, supportive and responsible.
9. Use Hindi, Hinglish or English naturally.
10. Return ONLY JSON.
"""


# ---------------------------------------------------
# Generate Chat
# ---------------------------------------------------

def generate_chat(topic):

    for attempt in range(3):

        try:

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": build_prompt(topic)
                    }
                ],
                temperature=0.8,
            )

            return response.choices[0].message.content

        except RateLimitError:

            print("Model Busy...Retrying in 20 seconds")
            time.sleep(20)

    raise Exception("Failed after 3 retries.")


# ---------------------------------------------------
# Parse JSON
# ---------------------------------------------------

def parse_chat(chat_text):

    chat_text = chat_text.replace("```json", "")
    chat_text = chat_text.replace("```", "")
    chat_text = chat_text.strip()

    return json.loads(chat_text)


# ---------------------------------------------------
# Save Chat
# ---------------------------------------------------

def save_chat(chat):

    os.makedirs("outputs", exist_ok=True)

    with open(OUTPUT_FILE, "a", encoding="utf-8") as file:

        json.dump(chat, file, ensure_ascii=False)

        file.write("\n")


# ---------------------------------------------------
# Load Topics
# ---------------------------------------------------

def load_topics():

    if not os.path.exists(TOPIC_FILE):
        raise FileNotFoundError(
            f"Topic file not found: {TOPIC_FILE}"
        )

    with open(TOPIC_FILE, "r", encoding="utf-8") as file:

        return [
            line.strip()
            for line in file
            if line.strip()
        ]


# ---------------------------------------------------
# Main
# ---------------------------------------------------

def main():

    topics = load_topics()

    generated = 0

    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    print("=" * 60)
    print("VEDAZ CHAT GENERATOR")
    print("=" * 60)

    for topic in topics:

        if generated >= TARGET_CONVERSATIONS:
            break

        print("\nTopic:", topic)

        try:

            chat_text = generate_chat(topic)

            chat = parse_chat(chat_text)

            validation = validate_dataset([chat])

            if validation["invalid"]:

                print("❌ Validation Failed")

                continue

            safety = check_dataset([chat])

            if safety:

                print("❌ Unsafe Conversation")

                continue

            save_chat(chat)

            generated += 1

            print(f"✅ Saved ({generated}/{TARGET_CONVERSATIONS})")

        except json.JSONDecodeError:

            print("❌ Invalid JSON Returned")

        except Exception as e:

            print(f"❌ {e}")

    print("\n" + "=" * 60)
    print("Generation Completed")
    print("=" * 60)

    print(f"Safe Conversations Generated : {generated}")

    print(f"Saved File : {OUTPUT_FILE}")


if __name__ == "__main__":
    main()