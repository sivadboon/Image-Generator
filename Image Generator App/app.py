from flask import Flask, render_template, request, redirect, url_for
from openai import OpenAI
import os
from dotenv import load_dotenv  # Import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")

client = OpenAI(api_key=api_key)

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    description = request.form.get('description')
    image_count = int(request.form.get('image_count', 1))

    generated_images = []
    for _ in range(image_count):
        response = client.images.generate(
            model="dall-e-3",
            prompt=description,
            size="1024x1024",
            n=1
        )
        image_url = response.data[0].url
        generated_images.append(image_url)

    return render_template('result.html', image_urls=generated_images)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
