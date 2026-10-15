

import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key .env file मध्ये सापडली नाही!")

client = genai.Client(api_key=api_key)
chat_history = []

print("🤖 Starting chatbot...")
print("type [exit] when you want to stop.\n")


while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Chatbot stopped. Thank you!")
        break

    # Save the user's question
    chat_history.append({
        "role": "user",
        "content": question
    })

    # Build conversation context
    conversation = ""

    for message in chat_history:
        if message["role"] == "user":
            conversation += f"User: {message['content']}\n"
        else:
            conversation += f"Assistant: {message['content']}\n"

    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            
            contents=(
                "Answer in the same language as the user. "
                "Be helpful, clear, and accurate. "
                "For current or latest information, do not guess "
                "or confidently provide outdated facts. "
                "If you cannot verify current information, "
                "clearly tell the user that you cannot verify it. "
                "Distinguish known facts from uncertain information.\n\n"
                f"Conversation history:\n{conversation}"
            )

        )

        answer = response.text
        print("Bot:", answer, "\n")

        # Save the bot's answer
        chat_history.append({
            "role": "assistant",
            "content": answer
        })

    
    except Exception as e:
        if chat_history and chat_history[-1]["role"] == "user":
            chat_history.pop()

        error_message = str(e)

        if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
            print("API quota limit zali aahe. Quota reset hoiparyant wait kar.\n")
        elif "503" in error_message or "UNAVAILABLE" in error_message:
            print("Gemini server busy aahe. Thodya velane try kar.\n")
        else:
            print("Error:", error_message, "\n")

