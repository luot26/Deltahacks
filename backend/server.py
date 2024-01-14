import os
from flask_cors import CORS
from flask import Flask, render_template, request, jsonify
import main
import chatbot
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def index():
    try:
        sentence = request.get_json()
        message = sentence.get('message')
        print(f"Received request with sentence: {sentence}")

        json_data = {'reply': 'Your reply here'}
        response = jsonify(json_data)

        main.CVLoop()
        response = chatbot.emotion_message(main.compute_dominant_emotion())
        print(main.compute_dominant_emotion())
        print(response)

        return jsonify({'response': response})
    
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/get_response')
def get_response():
    main.CVLoop()
    response = chatbot.emotion_message(main.compute_dominant_emotion())
    print(response)

    # if request.headers.get('Accept') == 'application/json':
    return jsonify({'response': response})
    # else:
    #     return render_template('index.html', response=response)

@app.route('/display_json')
def display_json():
    json_file_path = 'data.json'

    try:
        with open(json_file_path, 'r') as json_file:
            json_data = json.load(json_file)

        print(json_data)
        return jsonify({'data': json_data})

    except FileNotFoundError:
        return jsonify({'error': 'JSON file not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0')

