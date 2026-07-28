"""
Flask Web Server for Emotion Detection Application
Deploys the emotion detection model as a web service
"""
from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        "message": "Welcome to the Emotion Detection API",
        "usage": "POST /emotion-detector with JSON body {'text': 'your text here'}"
    })


@app.route('/emotion-detector', methods=['POST'])
def emotion_detector_api():
    """
    Emotion Detection API endpoint
    Accepts JSON with 'text' field and returns emotion analysis
    """
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({
            'error': 'Invalid JSON format',
            'status_code': 400
        }), 400

    text = data['text']

    # Handle blank input
    if text is None or str(text).strip() == "":
        return jsonify({
            'error': 'No text provided',
            'status_code': 400
        }), 400

    result = emotion_detector(text)

    if 'error' in result:
        return jsonify(result), result.get('status_code', 400)

    return jsonify(result), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    print("Starting Emotion Detection Server...")
    print("API endpoint: http://127.0.0.1:5000/emotion-detector")
    app.run(host='0.0.0.0', port=5000, debug=True)
