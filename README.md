# Courseware Agent 📚

Courseware_agent is a Telegram-based chatbot that helps university students generate a calendar of assignments or exam deadlines from their course outlines. The project uses LangChain with OpenAI's API to process the course outline PDF and generate a `.ics` calendar file, which users can easily integrate into their preferred calendar application.

## Features ✨

- **PDF Processing**: Upload a course outline PDF to the chatbot.
- **Deadline Extraction**: Automatically identifies assignments and exam deadlines.
- **Calendar Generation**: Generates an `.ics` file for seamless integration into calendar apps.
- **User-Friendly Interaction**: Operates entirely through Telegram via [@raven_agent_bot](https://t.me/raven_agent_bot).

## Requirements 📋

- Python 3.10+
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

4. **Configure the `config.py` File**

   Open the `config.py` file in the project directory and fill in the following variables:

   ```python
   TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
   TELEGRAM_CHANNEL_ID = "your_telegram_channel_id"
   OPENAI_API_KEY = "your_openai_api_key"
   ```

5. **Run the Project**

   ```bash
   chmod +x run_agent
   ./run_agent
   ```

## Usage 🚀

1. Start a chat with the Telegram bot [@raven_agent_bot](https://t.me/raven_agent_bot).
2. Upload your course outline as a PDF file.
3. Wait for the bot to process the file and generate a `.ics` calendar file.
4. Download the `.ics` file and import it into your calendar application.

## Project Structure 🗂️

```plaintext
courseware_agent/
├── cache/               # Cache files
├── working/             # Working directory for temporary files
├── README.md            # Project documentation
├── config.py            # Configuration file for API keys and tokens
├── pdf_to_ics_graph.py  # PDF to ICS processing logic
├── requirements.txt     # Python dependencies
├── run_agent            # Script to run the agent
├── telegram_bot_run.py  # Telegram bot runner
```

## Contributing 🤝

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact 📬

For any questions or feedback, feel free to reach out via the issues section, directly contact me on Telegram, or email me at [lizhaoluo@cmail.carleton.ca](mailto:lizhaoluo@cmail.carleton.ca).
