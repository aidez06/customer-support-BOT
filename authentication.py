from dotenv import load_dotenv
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
import openai
import os


# load the environment variables from the .env file
load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("API_KEY")

def policies(policy_text):
    # Preprocess policy text
    """Policies text need to be lowercase, remove stopping words, and remove punctation """
    tokens = word_tokenize(policy_text.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if not token in stop_words]
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

def response(model, user_prompt,temperature, max_token):
    """Response accordingly paramater provided"""
    response = openai.Completion.create(model=model, prompt=user_prompt, temperature=temperature, max_tokens=max_token)
    return response



