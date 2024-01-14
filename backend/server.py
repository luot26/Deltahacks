import os
import random
from flask_cors import CORS
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
CORS(app)

@app.route('/123123', methods=['POST'])
def index():
    try:
        sentence = request.get_json().get('message')
        print(f"Received request with sentence: {sentence}")

        # Process the sentence as needed

        # Respond back
        json_data = {'reply': 'Your reply here'}
        return jsonify(json_data)

    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')