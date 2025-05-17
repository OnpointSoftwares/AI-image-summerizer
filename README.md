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
  <img src="https://github-readme-stats.vercel.app/api?username=OnpointSoftwares&show_icons=true&theme=radical" alt="GitHub Stats">
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=OnpointSoftwares&layout=compact&theme=radical" alt="Top Languages">
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
   git clone https://github.com/OnpointSoftwares/AI-image-summerizer.git
   cd AI-image-summerizer
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

## Usage Guide
1. **Launch the App:** The main window will appear with a clean interface.
2. **Select an Image:** Click "Select Image" and choose any image file (JPG, PNG, BMP).
3. **Describe the Image:** Enter a brief description or context in the text box.
4. **Summarize:** Click "Summarize with Gemini" to get a concise summary.
5. **View Results:** The summary will appear below the description box.

## Customization
- **UI Enhancements:** Modify `src/app.py` to adjust layout, colors, or add features.
- **API Integration:** Update `src/gemini_api.py` for advanced Gemini API options.
- **Add Image Analysis:** Integrate local or cloud-based AI models as needed.

