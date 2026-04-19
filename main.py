import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from config import SYSTEM_PROMPT
from functions.get_file_content import schema_get_files_content
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from call_function import call_function

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


    tools_function = []
    tools_function.append(schema_write_file)
    tools_function.append(schema_get_files_content)
    tools_function.append(schema_get_files_info)
    tools_function.append(schema_run_python_file)
    tools_function = types.Tool(function_declarations=tools_function)


    # Schaut ob der api_key erkannt wurde
    if not api_key:
        raise RuntimeError("API_KEY ist fehlerhaft")
    
    # Holt mithilfe des API keys den client den wir brauchen
    client = genai.Client(api_key=api_key)


    for i in range(20):

        # Erstellt eine Antwort basierend auf Message, welche basierend auf dem "user_prompt" in der Konsole ist / Gibt einen Fehler aus wenn keine Tokens verwendet wurden. Gibt außerdem ein System/Verhaltens - Prompt an
        response = client.models.generate_content(
                            model="gemini-2.5-flash",
                            contents=messages,
                            config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT, temperature=0, tools=[tools_function]))
        

        if response.usage_metadata.prompt_token_count is None or response.usage_metadata.candidates_token_count is None:
            raise RuntimeError("Keine Tokens vergeben")
        
        if response.candidates is None:
            raise Exception("ERROR: no candidates")
        
        for cand in response.candidates:
            messages.append(cand.content)


        if response.function_calls is None:
            if args.verbose:
                print(f"User prompt: {args.user_prompt}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
                print()
            print(f"Gemini: {response.text}")
            return
        
        function_call_result = call_function(response.function_calls[0])
        if function_call_result.parts is not None:
            function_part_0 = function_call_result.parts[0].function_response
            if function_part_0 is None:
                raise Exception("EROOR: function result part [0] is None")
            if function_part_0.response is None:
                raise Exception("EROOR: function result is None")
        else:
            raise Exception("ERROR: function call has no Parts")
        
        new_function_message = types.Content(
            role="tool", # Oder "user", je nach SDK Version, meist "tool" für Responses
            parts=[function_call_result.parts[0]]
        )
        
        messages.append(new_function_message)
        

        if i == 19:
            print("Nicht gescahfft in Anzahl von iterationen")
            sys.exit(1)



    


if __name__ == "__main__":
    main()
