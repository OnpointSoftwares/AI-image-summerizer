# Image Recognition & Gemini Summarizer

## Overview
This project provides a modern, user-friendly desktop application for image-based summarization using the Gemini API. Users can select an image, enter a description, and instantly receive a concise summary powered by Google's Gemini large language model. No local AI model or TensorFlow installation is required—just a Gemini API key.

## Features
- **Intuitive Tkinter GUI:** Clean, modern, and easy-to-use interface.
- **Image Selection:** Quickly choose images from your computer for analysis.
- **Manual Description Input:** Enter your own description or context for any image.
- **Gemini API Summarization:** Instantly get a professional summary of your description.
- **Cross-Platform:** Works on Linux, Windows, and macOS (Python 3 required).

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

