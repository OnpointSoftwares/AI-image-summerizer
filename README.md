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

A powerful AI chatbot web application built with Django and Google's Gemini AI. DartMan provides intelligent conversation capabilities across various domains including:

- **Education & Learning:** Get explanations, solve problems, and learn new concepts
- **Programming Help:** Code assistance, debugging help, and programming concepts
- **General Knowledge:** Answers to questions across all subjects
- **Task Assistance:** Help with daily tasks and problem-solving
- **Creative Writing:** Story generation, writing assistance, and creative prompts
- **Technical Support:** Troubleshooting and technical explanations
- **Language Learning:** Practice conversations and language skills
- **Productivity:** Task management, scheduling, and organization
- **Entertainment:** Games, quizzes, and fun interactions

DartMan uses advanced natural language processing to provide accurate, helpful, and context-aware responses in real-time.

## 🎯 Key Features

- 💬 **Intelligent Chat:** Natural language processing powered by Gemini AI
- 🌟 **Multi-purpose:** Handles a wide range of topics and tasks
- 🚀 **Fast Responses:** Quick and accurate answers
- 🌐 **Web-Based:** Accessible from any device with a modern web browser
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
DartMan-AI-Chat/
├── manage.py            # Django management script
├── requirements.txt     # Project dependencies
├── static/              # Static files
│   ├── css/            # Stylesheets
│   └── js/             # JavaScript files
├── templates/           # HTML templates
├── chatbot/            # Django app directory
│   ├── views.py        # View functions
│   ├── models.py       # Database models
│   ├── urls.py         # URL configurations
│   └── gemini_api.py   # Gemini API integration
└── screenshots/        # Application screenshots
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
   > Note: This is a web application, no GUI dependencies are required.

3. **Set Up Gemini API Key**
   - Open `chatbot/gemini_api.py` and set your Gemini API key in the `GEMINI_API_KEY` variable.

4. **Run the Application**
   ```bash
   python manage.py runserver
   ```
   - Open your web browser and navigate to `http://localhost:8000` to access the chatbot

## 📚 Usage Guide

1. **Start the Application:**
   - Open your web browser and navigate to the deployed URL or `http://localhost:8000` if running locally
   - The web interface will load with a clean, modern chat interface

2. **Begin Chatting:**
   - Type your question or request in the text input area
   - Press Enter or click the send button to submit your message
   - DartMan will process your request and provide a response

3. **Features Available:**
   - **Natural Language Understanding:** Process and understand complex queries
   - **Context Awareness:** Maintain context across conversations
   - **Multi-turn Conversations:** Engage in detailed discussions
   - **Code Generation:** Write and explain code snippets
   - **Problem Solving:** Analyze and solve complex problems
   - **Learning Mode:** Get step-by-step explanations
   - **Multilingual Support:** Communicate in multiple languages
   - **Real-time Responses:** Quick and accurate answers
   - **Persistent Chat History:** Maintain conversation context
   - **Customizable Interface:** Personalize your chat experience

4. **View Responses:**
   - Responses appear in the chat window
   - Previous conversations are saved in the chat history
   - Clear the chat history when needed

## 🛠️ Customization Options

- **UI Customization:**
  - Modify templates in the `templates` directory
  - Customize CSS in `static/css`
  - Add custom JavaScript in `static/js`

- **API Configuration:**
  - Update `chatbot/gemini_api.py` for advanced API settings
  - Configure response parameters in `settings.py`
  - Add custom API endpoints in `chatbot/views.py`

- **Feature Enhancement:**
  - Add new chat features or capabilities
  - Integrate additional AI models or services
  - Customize response formatting and presentation



