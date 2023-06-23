import requests
from pdfminer.high_level import extract_text
import json

def convert_pdf_to_json(pdf_path):
    # Extract text from PDF
    text = extract_text(pdf_path)

    # Define the API endpoint
    api_endpoint = 'https://api.openai.com/v1/engines/text-davinci-002/completions'

    # Define the headers for the API request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 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'
    }

    # Define the data for the API request
    data = {
        'prompt': text,
        'max_tokens': 1000
    }

    # Make the API request
    response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))

    # Get the JSON response
    response_json = response.json()

    # Extract the generated text from the JSON response
    generated_text = response_json['choices'][0]['text']
    print(generated_text)
    # Convert the generated text to JSON
    resume_json = json.loads(generated_text)

    return resume_json
    
json = convert_pdf_to_json('./resume.pdf')
print(json)
