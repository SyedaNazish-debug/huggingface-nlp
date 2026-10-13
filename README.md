# Hugging Face NLP Practicals

A hands-on learning project exploring Natural Language Processing (NLP) using Python and Hugging Face Transformers.

## Practicals

### 1. Tokenization

**File:** `tokenizer.py`

Uses the pretrained `bert-base-uncased` tokenizer to:
- Convert sentences into token IDs.
- Display tokens and subword units.
- Count tokens, including special tokens added by the tokenizer.

**Status:** Implemented.

### 2. Sentiment Analysis

**File:** `sentiment_analysis.py`

Uses the Hugging Face `pipeline("sentiment-analysis")` interface to classify the sentiment of three example sentences.

The script uses the pipeline's default pretrained model because no model name is explicitly specified.

**Status:** Implemented; outputs and observations will be documented as verified.

## Technologies

- Python
- Hugging Face Transformers
- PyTorch

## Project Structure

```text
huggingface-nlp/
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- tokenizer.py
|-- sentiment_analysis.py
`-- tk.py
```

`tk.py` currently duplicates the code in `tokenizer.py`. It is retained temporarily while the project structure is being organized.

## Purpose

This repository documents practical experiments, code, and learning progress while exploring NLP tools and pretrained models.

## Disclaimer

This is a learning project, not a production-ready NLP application.