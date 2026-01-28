import os
import argparse
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise Exception("api key is None")
else:
    client = genai.Client(api_key=api_key)
    parser = argparse.ArgumentParser(description="AgentGreen")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    prompt = args.user_prompt
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    if response.usage_metadata == None:
        raise RuntimeError("no respnse from LLM")
    else:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"Response: {response.text}")
    
