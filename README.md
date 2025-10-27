# Hey Hi Lab Work 2025

This repository contains Python assignments and exercises for an AI/ML course.

## Repository Structure

### 📁 `basics/`
Basic Python learning exercises covering fundamental concepts:
- `variables_and_types.py` - Variable declarations and data types
- `data_structures.py` - Lists, dictionaries, sets, and tuples
- `loops.py` - For loops and while loops
- `recursion_factorial.py` - Recursive function example (factorial)

### 📁 `oop_examples/`
Object-oriented programming examples:
- `student_and_bank_account.py` - Student and BankAccount classes with methods

### 📁 `ai_agents/`
AI agent implementations:
- `vacuum_cleaner_agent.py` - Simple reflex agent for vacuum cleaner simulation

### 📁 `week4/`
Week 4 assignments - Natural Language Processing:
- `text_analysis_word_freq.py` - Text tokenization, stopword removal, and word frequency analysis

### 📁 `week5/`
Week 5 assignments - Sentiment Analysis:
- `sentiment_setup.py` - Setup script for sentiment analysis libraries
- `sentiment_basic_analysis.py` - Basic sentiment analysis using TextBlob
- `sentiment_interactive_analyzer.py` - Interactive sentiment analyzer
- `sentiment_article_analysis.py` - Article sentiment analysis using TextBlob
- `sentiment_vader_analysis.py` - Article sentiment analysis using VADER

### 📁 `data/`
Data files used by the scripts:
- `article1.txt` - Sample article for sentiment analysis
- `article2.txt` - Sample article for sentiment analysis
- `article3.txt` - Sample article for sentiment analysis

## Running the Scripts

Each script can be run independently from the repository root:

```bash
# Basic examples
python3 basics/variables_and_types.py
python3 basics/recursion_factorial.py

# OOP examples
python3 oop_examples/student_and_bank_account.py

# AI agents
python3 ai_agents/vacuum_cleaner_agent.py

# Week 4 assignments
python3 week4/text_analysis_word_freq.py

# Week 5 assignments (requires dependencies)
cd week5
python3 sentiment_basic_analysis.py
```

## Dependencies

Some scripts require additional Python packages:
- `textblob` - For TextBlob-based sentiment analysis
- `nltk` - For VADER sentiment analysis
- `pandas` - For data manipulation
- `matplotlib` - For data visualization

Install dependencies using:
```bash
pip install textblob nltk pandas matplotlib
```

## Notes

- Week 5 scripts are designed to be run from within the `week5/` directory as they use relative paths to access data files in `../data/`.
- The `basics/loops.py` file contains an infinite loop bug in the third loop example (pre-existing issue).
