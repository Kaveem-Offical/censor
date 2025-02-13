from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Censorship dictionary
censor_dict = {
    # General profanity
    "fuck": "f**k",
    "shit": "s**t",
    "ass": "a*s",
    "bitch": "b***h",
    "damn": "d**n",
    "hell": "h**l",
    "piss": "p**s",
    "dick": "d**k",
    "cock": "c**k",
    "pussy": "p***y",
    
    # Sexual terms
    "sex": "s*x",
    "nude": "n*de",
    "naked": "n***d",
    "orgasm": "o****m",
    "masturbate": "m********e",
    
    # Body parts
    "penis": "p***s",
    "vagina": "v****a",
    "boobs": "b**bs",
    "breasts": "b*****s",
    "clitoris": "c******s",
    "testicles": "t*******s",
    
    # Derogatory terms
    "slut": "s**t",
    "whore": "w****e",
    "rape": "r**e",
    "pedophile": "p*******e",
    
    # Slang/variations
    "fag": "f*g",
    "dyke": "d**e",
    "tranny": "t****y",
    "fucking": "f*****g",
    "fucker": "f*****r",
    "sexy": "s**xy",
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

if __name__ == '__main__':
    app.run(debug=False)