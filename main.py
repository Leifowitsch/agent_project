import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from config import SYSTEM_PROMPT

def main():

    load_dotenv()
    # Holt den api_key aus der .env datei
    api_key = os.environ.get("GEMINI_API_KEY")

    # erstellt einen Parser (Eine maschine die sich die Eingaben aus dem Terminal holt), das erste was hinter main.py steht ist dann der "user_prompt", danach wird geschaut ob "--verbose" vorkommt, wenn ja dann setzte es auf True
    # dieser Arguemnte werden dann einer varibale namens args hinzugeordnet
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Sind bishereige Nachrichten
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Schaut ob der api_key erkannt wurde
    if not api_key:
        raise RuntimeError("API_KEY ist fehlerhaft")
    
    # Holt mithilfe des API keys den client den wir brauchen
    client = genai.Client(api_key=api_key)

    # Erstellt eine Antwort basierend auf Message, welche basierend auf dem "user_prompt" in der Konsole ist / Gibt einen Fehler aus wenn keine Tokens verwendet wurden. Gibt außerdem ein System/Verhaltens - Prompt an
    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=messages,
                        config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT))
    

    if response.usage_metadata.prompt_token_count is None or response.usage_metadata.candidates_token_count is None:
        raise RuntimeError("Keine Tokens vergeben")
    
    # Wenn --verbose angegeben wird drucke Metadaten dazu
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print()

    print(response.text)

    


if __name__ == "__main__":
    main()
