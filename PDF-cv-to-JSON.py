import requests
import PyPDF2

import openai

openai.api_key = "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"

def chat_with_chatgpt(prompt, model="davinci"):
    response = openai.Completion.create(
        engine=model,
        prompt=text,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    print(response)

    message = response.choices[0].text.strip()
    return message

def convert_pdf_to_text(pdf_file_path):
    # Read the PDF file and extract text
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()

    return text

def convert_text_to_json(text):
    # Make a POST request to the ChatGPT API
    response = requests.post(
        'https://api.openai.com/v1/engines/davinci/completions',
        headers={'Authorization': 'Bearer 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'},
        json={
            'prompt': f"give me the summay of this resume in json format \n \n {text}",
            'max_tokens': 1024,
            'temperature': 0.7,
            'n': 1,
            'stop': None,
        }
    )
    print(response.json())
    # Parse the JSON response
    json_output = response.json()['choices'][0]['text']

    return json_output

def save_json_to_file(json_output):
    # Save the JSON output to a file named output.json
    with open('output.json', 'w') as file:
        file.write(json_output)

# Provide the path to your PDF file
pdf_file_path = 'resume.pdf'

# Convert PDF to text
text = convert_pdf_to_text(pdf_file_path)
print(f"raw text: {text}")
# Convert text to JSON using ChatGPT
# json_output = convert_text_to_json(text)
#print(json_output)
# Save JSON to output file
# save_json_to_file(json_output)

chatgpt_answer = chat_with_chatgpt(text)
print(f"This is the response from chatgpt: {chatgpt_answer}")

