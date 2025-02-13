from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Censorship dictionary
censor_dict = {
    "fuck": "f**k", "shit": "s**t", "ass": "a*s", "bitch": "b***h",
    "sex": "s*x", "nude": "n*de", "penis": "p***s", "vagina": "v****a",
    "boobs": "b**bs", "cock": "c**k", "pussy": "p***y", "dick": "d**k",
    # Add more words as needed
}

def censor_text(text):
    pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in censor_dict.keys()) + r')\b', re.IGNORECASE)
    return pattern.sub(lambda match: censor_dict[match.group().lower()], text)

@app.route('/censor', methods=['POST'])
def censor():
    data = request.json
    if 'text' not in data:
        return jsonify({"error": "Missing 'text' parameter"}), 400
    
    original_text = data['text']
    censored_text = censor_text(original_text)
    return jsonify({"original": original_text, "censored": censored_text})

# Required for Netlify Functions
def handler(event, context):
    return app(event, context)