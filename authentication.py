from dotenv import load_dotenv
import openai
import os


# load the environment variables from the .env file
load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("API_KEY")


def response(model, user_prompt,temperature, max_token):
    response = openai.Completion.create(model=model, prompt=user_prompt, temperature=temperature, max_tokens=max_token)
    return response

