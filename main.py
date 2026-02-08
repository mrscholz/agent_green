import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function


def handle_function_responses(response, args):
    function_call_results = []
    for function_call in response.function_calls:
        # print(f"Calling function: {function_call.name}({function_call.args})")
        function_call_result = call_function(function_call, args.verbose)
        if function_call_result.parts == None or len(function_call_result.parts) == 0:
            raise Exception("Error: The parts list appears empty")
        elif function_call_result.parts[0] == None:
            raise Exception("Error: First element of parts is None")
        elif function_call_result.parts[0].function_response == None:
            raise Exception("Error: The function_response is None")
        elif function_call_result.parts[0].function_response.response == None:
            raise Exception("Error: The response element is None")
        else:
            function_call_results.append(function_call_result.parts[0])
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    return function_call_results


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise Exception("api key is None")
    else:
        client = genai.Client(api_key=api_key)
        parser = argparse.ArgumentParser(description="AgentGreen")
        parser.add_argument("user_prompt", type=str, help="User prompt")
        parser.add_argument(
            "--verbose", action="store_true", help="Enable verbose output"
        )
        args = parser.parse_args()

        messages = [
            types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
        ]

        for _ in range(20):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt,
                    temperature=0,
                ),
            )

            # add response messages to messages
            if response.candidates != None:
                for candidate in response.candidates:
                    if candidate.content is not None:
                        messages.append(candidate.content)

            if response.usage_metadata == None:
                raise RuntimeError("no respnse from LLM")
            else:
                if args.verbose:
                    print(f"User prompt: {messages}")
                    print(
                        f"Prompt tokens: {response.usage_metadata.prompt_token_count}"
                    )
                    print(
                        f"Response tokens: {response.usage_metadata.candidates_token_count}"
                    )
                if response.function_calls != None:
                    function_call_results = handle_function_responses(response, args)
                    messages.append(
                        types.Content(role="user", parts=function_call_results)
                    )
                else:
                    print(f"Response: {response.text}")
                    return
        sys.exit("Error: Maximum agent iterations reached without result.")


if __name__ == "__main__":
    main()
