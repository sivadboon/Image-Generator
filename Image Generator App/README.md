
# AI Image Generator Web Application

A user-friendly web application built with **Flask** that leverages the **OpenAI API** to generate images based on text descriptions or voice inputs. The app provides a seamless experience with a countdown timer, loading spinner, and a speech-to-text input option.

## Features

- **Text-to-Image Generation**: Users can input a description and generate images based on the text provided using OpenAI's API.
- **Speech-to-Text Integration**: 🎤 Users can also speak their description using the Web Speech API, and the app will convert it into text for generating the image.
- **Multiple Image Generation**: Users can select the number of images (up to 4) they want to generate.
- **Responsive Design**: The app is designed to work across desktop and mobile devices.

## Tech Stack

- **Python** (Flask framework)
- **HTML5/CSS3**
- **OpenAI API**
- **Web Speech API**
- **JavaScript (for speech-to-text and countdown features)**

## Prerequisites

- **Python 3.8 or later** installed on your system.
- A valid **OpenAI API Key**.

## Setup Instructions

### Step 1: Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/sivadboon/Image-Generator.git
cd Image-Generator
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

To avoid conflicts with other Python packages, it’s a good idea to create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Create a .env File

Create a `.env` file in the project’s root directory to securely store your OpenAI API key. Inside the `.env` file, add:

```
OPENAI_API_KEY=sk-your-openai-api-key
```

### Step 5: Run the Application

Once everything is set up, you can run the Flask application:

```bash
python app.py
```

This will start the Flask server, and the application will be accessible at **http://127.0.0.1:5001**.

### Step 6: Open the Application in Your Browser

Navigate to the following URL in your web browser:

```
http://127.0.0.1:5001
```
