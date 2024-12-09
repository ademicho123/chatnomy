# UniChat AI

UniChat AI is a Streamlit-based chatbot application powered by Together AI. It supports file uploads of various formats, including text files, code files, documents, spreadsheets, and images, to interact with and get AI-generated insights.

## Features
- Accepts file uploads (e.g., `.py`, `.html`, `.xls`, `.doc`, `.pdf`, `.png`).
- Displays file content in the app.
- Allows you to query Together AI about the content of uploaded files.
- Simple, intuitive Streamlit interface.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/streamlit_ai_chatbot.git
   cd streamlit_ai_chatbot

2. Install dependencies:
    pip install -r requirements.txt

3. Create a .env file and add your Together AI credentials:
    TOGETHER_AI_API_KEY=your_api_key_here
    TOGETHER_AI_API_URL=https://api.together.xyz/endpoint

4. Run the application:
    streamlit run app.py

5. Access the app in your browser at http://localhost:8501.

## Usage

Upload any supported file.
View the file content in the app.
Query Together AI for insights or analysis based on the file content.

## License

This project is licensed under the MIT License.

#### Instructions
- Replace `your_api_key_here` and `https://api.together.xyz/endpoint` with your actual Together AI API key and endpoint URL.
- Use the app by uploading files and interacting with the chatbot.

Let me know if you need further assistance!
