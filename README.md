# 🌟 Vedaz-AI-Astro - AI Dataset Engineering Pipeline

## 📌 Overview

Vedaz AI Astrologer is a complete **AI dataset engineering and evaluation pipeline** designed to generate, validate, clean, analyze, and evaluate conversational AI datasets for an astrology-based assistant.

The project focuses on producing **safe, structured, and high-quality training data** that can be used for AI model fine-tuning while encouraging responsible AI behavior through automated validation and safety checks.

---

# 🚀 Features

## 🧠 1. Dataset Generation

- Generates synthetic astrology conversations using the OpenRouter API.
- Uses prompt engineering to create structured conversations.
- Produces JSONL datasets suitable for LLM fine-tuning.
- Encourages safe and responsible AI responses.

---

## ✅ 2. Dataset Validation

- Validates JSONL formatting.
- Checks conversation structure.
- Ensures proper:
  - `system`
  - `user`
  - `assistant`
  message flow.
- Detects corrupted or incomplete records.

---

## ⚠️ 3. Safety Checker

Automatically detects unsafe astrology responses including:

- Death predictions
- Serious illness claims
- Guaranteed future outcomes
- Fear-based remedies
- Harmful deterministic advice

Uses a rule-based Regex filtering system for safety enforcement.

---

## 🔍 4. Duplicate Detection

- Detects exact duplicates.
- Finds near-duplicate conversations.
- Uses Python's `SequenceMatcher` similarity scoring.
- Removes redundant training samples.

---

## 📊 5. Dataset Statistics

Automatically computes:

- Total conversations
- Total messages
- Average conversation length
- Average words per conversation
- Shortest conversation
- Longest conversation

---

## ✂️ 6. Train-Test Split

Automatically splits the cleaned dataset into:

- **80% Training**
- **20% Testing**

Exports:

- `train.jsonl`
- `test.jsonl`

---

## 🤖 7. AI Evaluation System

Evaluates AI-generated responses using an LLM Judge.

Scores responses based on:

- Safety
- Helpfulness
- Honesty
- Warmth

Outputs evaluation results in CSV format.

---

## 📄 8. Report Generator

Generates a complete dataset report including:

- Validation summary
- Safety analysis
- Duplicate analysis
- Dataset statistics
- Overall dataset quality

---

# 🏗️ Project Structure

```text
Vedaz-AI-Engineer/
│
├── core/
│   ├── dataset.py
│   ├── validator.py
│   ├── statistics.py
│   ├── duplicate_detector.py
│   ├── safety_checker.py
│   ├── splitter.py
│   ├── report_generator.py
│
├── scripts/
│   ├── generator.py
│   ├── evaluator.py
│   ├── checker.py
│
├── data/
│   ├── vedaz_astrologer_finetune.jsonl
│   ├── topics.txt
│   ├── test_questions.txt
│
├── outputs/
│   ├── generated_chats.jsonl
│   ├── train.jsonl
│   ├── test.jsonl
│   ├── report.txt
│   ├── evaluation.csv
│
├── requirements.txt
├── .env
├── LICENSE
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Nithish-kumar444/vedaz-ai-engineer.git
cd vedaz-ai-engineer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Setup

Create a `.env` file in the project root.

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

# ▶️ How to Run

## 1️⃣ Generate Dataset

```bash
python -m scripts.generator
```

---

## 2️⃣ Validate Dataset

```bash
python -m scripts.checker
```

---

## 3️⃣ Evaluate AI Responses

```bash
python -m scripts.evaluator
```

---

# 📊 Output Files

| File | Description |
|------|-------------|
| `outputs/generated_chats.jsonl` | Generated conversations |
| `outputs/train.jsonl` | Training dataset |
| `outputs/test.jsonl` | Testing dataset |
| `outputs/report.txt` | Dataset quality report |
| `outputs/evaluation.csv` | AI evaluation scores |

---

# 🧠 Tech Stack

- Python
- OpenRouter API
- OpenAI-compatible APIs
- JSONL
- Regular Expressions (Regex)
- SequenceMatcher
- NLP Prompt Engineering

---

# 🎯 Project Goal

The objective of this project is to build a **production-style AI dataset engineering pipeline** capable of generating, validating, cleaning, and evaluating conversational datasets for an AI astrologer while ensuring safety, consistency, and high-quality training data.

The pipeline is designed to:

- Generate structured conversational datasets
- Prevent harmful astrology advice
- Detect unsafe responses automatically
- Remove duplicate conversations
- Split datasets for machine learning
- Evaluate AI responses using an LLM Judge
- Produce detailed analytical reports

---

# ⚠️ Limitations

Although this project demonstrates a complete AI dataset engineering workflow, it has several limitations due to infrastructure, API, and implementation constraints.

## 🔑 1. API Rate Limits

- Uses OpenRouter free-tier models.
- Free-tier APIs enforce strict request-per-minute and daily request limits.
- Large-scale dataset generation or evaluation may trigger **HTTP 429 (Rate Limit Exceeded)** errors.

---

## ⏳ 2. Processing Speed

- Dataset generation and evaluation rely on external LLM API calls.
- Overall execution speed depends on network latency and model response time.
- Processing large datasets can therefore take considerable time.

---

## 🤖 3. Model Dependency

- Output quality depends on the selected OpenRouter model (e.g., `openai/gpt-oss-20b:free`).
- Different models may generate responses with varying quality, consistency, and evaluation scores.

---

## 🧠 4. Rule-Based Safety System

- The safety checker primarily uses Regex-based pattern matching.
- It may fail to detect cleverly paraphrased unsafe responses or indirect harmful intent.
- Future versions could incorporate LLM-based safety classification for improved detection accuracy.

---

## 📊 5. Evaluation Subjectivity

- Response evaluation is performed by another LLM rather than human experts.
- Scores for Safety, Helpfulness, Honesty, and Warmth are approximate and may vary slightly across different runs.

---

## 💾 6. Local File-Based Storage

- The project stores datasets locally using JSONL and CSV files.
- It does not currently support relational databases or cloud storage platforms.
- Collaborative dataset management is therefore limited.

---

## 🔄 7. Non-Deterministic Outputs

- LLM generation uses temperature-based sampling.
- The same prompt may produce different conversations in different executions.
- Complete reproducibility cannot always be guaranteed.

---

# 📌 Highlights

- ✅ End-to-End AI Dataset Pipeline
- ✅ Production-Style Modular Architecture
- ✅ Automated Dataset Generation
- ✅ JSONL Validation
- ✅ Safety-First AI Design
- ✅ Duplicate Conversation Detection
- ✅ Dataset Analytics
- ✅ Automated Train/Test Split
- ✅ LLM-Based Evaluation System
- ✅ Report Generation
- ✅ Fine-Tuning Ready Dataset

---

# 👨‍💻 Author

**Nithish Kumar**

B.Tech – Computer Science Engineering (AI & ML)

CMR University

---

# 📜 License

This project is licensed under the **MIT License**.

```text
MIT License

Copyright (c) 2026 Nithish Kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
