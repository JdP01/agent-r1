import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from .env file
load_dotenv()

# Initialize the client
# The OpenAI library automatically looks for OPENAI_API_KEY in the environment
client = OpenAI()

def get_completion(prompt):

    prompt = input("send something")
    try:
        response = client.chat.completions.create(
            model="gpt-5.4-nano",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            #max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

result = get_completion("Hello, how are you today?")
print(result)