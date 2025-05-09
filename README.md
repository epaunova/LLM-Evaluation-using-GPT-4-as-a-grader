# 📊 LLM-Eval-Playbook

This repository contains tools and templates for evaluating prompt responses from Large Language Models (LLMs) using structured rubrics and automated graders like GPT-4 or Claude.

## 🎯 Goals
- Assess LLM output quality across clarity, correctness, and helpfulness
- Use GPT-4 as a grading assistant for scalable evaluation
- Analyze response consistency across prompt variants and model versions

## 📁 Contents
- `notebooks/` — Run evaluation scripts with OpenAI API
- `rubrics/` — Scoring criteria definitions
- `datasets/` — Optional: prompts + model responses for batch eval
- `outputs/` — GPT-graded results for analysis

## ✅ Scoring Dimensions
| Dimension   | Description |
|-------------|-------------|
| Clarity     | Is the response clearly worded and well-structured? |
| Correctness | Are the facts or logic accurate and appropriate? |
| Helpfulness | Does the response address the user's intent effectively? |

