# LangChain: Summarize Text From YT or Website 🦜

An AI-powered Streamlit web application that automatically extracts and summarizes content from YouTube videos and website URLs. It leverages the LangChain framework and the Groq API for lightning-fast, high-quality summarization.

## Features

- **YouTube Video Summarization**: Simply paste a YouTube URL (`youtube.com` or `youtu.be`). The app extracts the video's transcript (without needing API keys from YouTube) and generates a concise summary.
- **Website Summarization**: Paste any generic website URL, and the app will scrape the textual content and summarize it.
- **Powered by Groq & LangChain**: Uses modern LangChain Expression Language (LCEL) and Groq's high-speed inference engine (defaulting to the `openai/gpt-oss-20b` model) to provide summaries almost instantly.

## Prerequisites

- Python 3.8 or higher installed on your machine.
- A free API key from [Groq](https://console.groq.com/).

## Installation and Setup Guide

Follow these step-by-step instructions to get the project running locally.

### 1. Clone or Download the Repository
Ensure you have the project files on your local machine and navigate into the project directory in your terminal:
```bash
cd "YT Video and Web URL content Summarization"
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage project dependencies.
```bash
# On Windows
python -m venv evenv
evenv\Scripts\activate

# On macOS/Linux
python3 -m venv evenv
source evenv/bin/activate
```

### 3. Install Dependencies
Install all the required Python packages using the provided `requirements.txt` file.
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
The application requires your Groq API key to function. 
1. In the root folder of the project, create a new file named exactly `.env`.
2. Open the `.env` file in a text editor and add your Groq API key in the following format:
   ```env
   GROQ_API="your_groq_api_key_here"
   ```
   *(Note: The `.gitignore` file is already configured to prevent your `.env` file from being committed to version control.)*

### 5. Run the Application
Launch the Streamlit server to interact with the app.
```bash
streamlit run app.py
```

## How to Use the App

1. Once the app is running, your default web browser will open to `http://localhost:8501`.
2. In the main text input field labeled **"URL"**, paste a valid URL. This can be:
   - A YouTube video link (e.g., `https://www.youtube.com/watch?v=...`)
   - A general website link (e.g., `https://en.wikipedia.org/wiki/Artificial_intelligence`)
3. Click the **"Summarize the Content from YT or Website"** button.
4. The app will fetch the content, process it through the Groq LLM, and display a ~300-word summary on the screen.

## Technologies Used

- **[Streamlit](https://streamlit.io/)**: For the frontend web interface.
- **[LangChain](https://www.langchain.com/)**: For orchestrating the LLM prompts and chains.
- **[Groq](https://groq.com/)**: Fast LLM inference API.
- **`youtube-transcript-api`**: For fetching YouTube closed captions/transcripts.
- **`unstructured`**: For extracting text content from arbitrary web pages.
- **`python-dotenv`**: For securely managing environment variables.
