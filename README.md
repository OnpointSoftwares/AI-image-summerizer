# DartMan AI Chat

[![GitHub stars](https://img.shields.io/github/stars/OnpointSoftwares/DartMan-AI-Chat?style=social)](https://github.com/OnpointSoftwares/DartMan-AI-Chat/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/OnpointSoftwares/DartMan-AI-Chat?style=social)](https://github.com/OnpointSoftwares/DartMan-AI-Chat/network/members)
[![GitHub license](https://img.shields.io/github/license/OnpointSoftwares/DartMan-AI-Chat)](https://github.com/OnpointSoftwares/DartMan-AI-Chat/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/OnpointSoftwares/DartMan-AI-Chat)](https://github.com/OnpointSoftwares/DartMan-AI-Chat/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/OnpointSoftwares/DartMan-AI-Chat)](https://github.com/OnpointSoftwares/DartMan-AI-Chat/pulls)

<p align="center">
  <img src="screenshots/dartmanchat.png" alt="Application Screenshot" width="600">
</p>

## 🚀 Project Overview

A powerful AI chatbot desktop application built with Google's Gemini AI. DartMan provides intelligent conversation capabilities, answering questions, assisting with tasks, and providing helpful insights across various domains.

## 🎯 Key Features

- 💬 **Intelligent Chat:** Natural language processing powered by Gemini AI
- 🌟 **Multi-purpose:** Handles a wide range of topics and tasks
- 🚀 **Fast Responses:** Quick and accurate answers
- 🌐 **Cross-Platform:** Works on Linux, Windows, and macOS
- 🔐 **Secure:** Private and secure chat sessions
- 📚 **Easy Setup:** Simple configuration and usage

## 📈 Project Statistics

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=OnpointSoftwares&repo=DartMan-AI-Chat&show_icons=true&theme=radical" alt="GitHub Stats">
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=OnpointSoftwares&repo=DartMan-AI-Chat&layout=compact&theme=radical" alt="Top Languages">
</p>

## 📋 Project Structure

```
AI-image-summerizer/
├── src/
│   ├── app.py           # Main application code
│   ├── gemini_api.py    # Gemini API integration
│   └── views.py         # UI components
├── data/
│   └── raw/            # Raw data files
├── screenshots/         # Application screenshots
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/OnpointSoftwares/DartMan-AI-Chat.git
   cd DartMan-AI-Chat
   ```
2. **Install Dependencies**
   Ensure you have Python 3.8+ and pip installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```
   > If you encounter issues with `python3-tk`, install it via your OS package manager (e.g., `sudo apt install python3-tk` on Ubuntu).

3. **Set Up Gemini API Key**
   - Open `src/gemini_api.py` and set your Gemini API key in the `GEMINI_API_KEY` variable.

4. **Run the Application**
   ```bash
   python3 src/app.py
   ```

## 📚 Usage Guide

1. **Start the Application:**
   - Open the main window with a clean, intuitive interface
   - The chat interface will appear with a text input area

2. **Begin Chatting:**
   - Type your question or request in the text input area
   - Press Enter or click the send button to submit your message
   - DartMan will process your request and provide a response

3. **Features Available:**
   - Ask questions on any topic
   - Get explanations and insights
   - Receive recommendations
   - Perform calculations and analyses
   - Get help with tasks and problems

4. **View Responses:**
   - Responses appear in the chat window
   - Previous conversations are saved in the chat history
   - Clear the chat history when needed

## 🛠️ Customization Options

- **UI Customization:**
  - Modify `src/app.py` to adjust layout, colors, and styling
  - Customize the chat interface appearance
  - Add custom UI elements or features

- **API Configuration:**
  - Update `src/gemini_api.py` for advanced API settings
  - Configure response parameters and behavior
  - Add custom API endpoints or integrations

- **Feature Enhancement:**
  - Add new chat features or capabilities
  - Integrate additional AI models or services
  - Customize response formatting and presentation



