# courseware_agent 📚

courseware_agent is a Telegram-based chatbot that helps university students generate a calendar of assignments or exam deadlines from their course outlines. The project uses LangChain with OpenAI's API to process the course outline PDF and generate a `.ics` calendar file, which users can easily integrate into their preferred calendar application.

## Features ✨

- **PDF Processing**: Upload a course outline PDF to the chatbot.
- **Deadline Extraction**: Automatically identifies assignments and exam deadlines.
- **Calendar Generation**: Generates an `.ics` file for seamless integration into calendar apps.
- **User-Friendly Interaction**: Operates entirely through Telegram via `@raven_agent_bot`.

## Requirements 📋

- Python 3.8+
- Telegram bot token
- OpenAI API key

## Installation 🛠️

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/courseware_agent.git
   cd courseware_agent
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the root directory and add the following:

   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Run the Project**

   ```bash
   python app.py
   ```

## Usage 🚀

1. Start a chat with the Telegram bot `@raven_agent_bot`.
2. Upload your course outline as a PDF file.
3. Wait for the bot to process the file and generate a `.ics` calendar file.
4. Download the `.ics` file and import it into your calendar application.

## Project Structure 🗂️

```plaintext
courseware_agent/
├── app.py               # Main application logic
├── requirements.txt     # Python dependencies
├── utils/               # Helper functions and utilities
├── templates/           # Predefined templates for processing
├── .env.example         # Example environment file
└── README.md            # Project documentation
```

## Contributing 🤝

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact 📬

For any questions or feedback, feel free to reach out via the issues section or directly contact me on Telegram.
