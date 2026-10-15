# My AI Chatbot 🤖

A web-based AI chatbot built using Python, Streamlit, and Google's Gemini API. It answers user questions and can search the web for current information.

## Features

- AI-powered question answering using Gemini
- Optional web search using DuckDuckGo
- Source links for web-based answers
- Interactive chat interface built with Streamlit
- Quick example prompts
- New Chat and Clear Chat controls
- Error handling for API quota and service issues

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- DuckDuckGo Search (`ddgs`)
- python-dotenv

## Project Structure

```text
AI-Chatbot/
├── app/
│   ├── web_app.py
│   └── test_gemini.py
├── .env
├── .gitignore
└── README.md
```

## Setup Instructions

1. Clone or download this repository.
2. Create and activate a Python virtual environment.
3. Install the required dependencies.
4. Create a `.env` file in the project root and add your Gemini API key:

   `GEMINI_API_KEY=your_api_key_here`

5. Run the app:

   `python -m streamlit run app/web_app.py`

## Security

- Keep API keys in `.env`.
- Never upload `.env` or other secrets to GitHub.
- Use `.gitignore` to exclude secrets and virtual environments.

## Future Improvements

- Improve response formatting
- Add support for more search options
- Add persistent conversation history
