import os
import sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    from google import genai

    user_prompt = sys.argv[1]
    
    client = genai.Client(api_key=api_key)
    messages = [genai.types.Content(role="user", parts=[genai.types.Part(text=user_prompt)])]
    
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
)
    
    prompt_token = response.usage_metadata.prompt_token_count
    canidate_token = response.usage_metadata.candidates_token_count
    
    print(response.text)

    if "--verbose" in sys.argv:
        print(f"User prompt: {user_prompt}")    
        
        print(f"Prompt tokens: {prompt_token-1}\nResponse tokens:{canidate_token}")

if __name__ == "__main__":
    main()

