from flask import Flask, render_template_string
import random

app = Flask(__name__)

# List of quotes
quotes = [
    "Believe in yourself!",
    "Every day is a second chance.",
    "Dream big, work hard, stay humble.",
    "You are capable of amazing things.",
    "Success starts with self-belief."
]

@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template_string('''
        <html>
        <head><title>Quote of the Day</title></head>
        <body style="text-align:center; margin-top:100px; font-family:sans-serif;">
            <h1>🌟 Quote of the Day 🌟</h1>
            <h2>{{ quote }}</h2>
        </body>
        </html>
    ''', quote=quote)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

