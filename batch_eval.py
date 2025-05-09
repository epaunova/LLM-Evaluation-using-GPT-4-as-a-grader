import openai
import csv
import json

openai.api_key = "your-api-key-here"

def evaluate_response(response_text):
    grading_prompt = f"""You are a strict grader. Given the following model response, rate it from 0 to 5 in:
- Clarity
- Correctness
- Helpfulness

Response:
{response_text}

Return format:
{{'clarity': int, 'correctness': int, 'helpfulness': int, 'comments': str}}"""

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You evaluate LLM responses."},
            {"role": "user", "content": grading_prompt}
        ]
    )
    return completion['choices'][0]['message']['content']

input_file = "datasets/grading_examples.csv"
output_file = "evaluation_outputs/evaluated_outputs.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["clarity", "correctness", "helpfulness", "comments"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        eval_result = evaluate_response(row["model_response"])
        eval_data = json.loads(eval_result.replace("'", """))  # Ensure JSON-compatible
        row.update(eval_data)
        writer.writerow(row)
