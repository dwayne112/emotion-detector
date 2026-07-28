"""
Flask Web Server for Emotion Detection Application
With error handling for blank input
"""
from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotion-detector', methods=['POST'])
def emotion_detector_api():
    """
    Emotion Detection API endpoint
    Handles blank input errors with status code 400
    """
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({
            'error': 'Invalid JSON format',
            'status_code': 400
        }), 400

    text = data['text']

    # Handle blank input - returns 400
    if text is None or str(text).strip() == "":
        return jsonify({
            'error': 'No text provided',
            'status_code': 400
        }), 400

    result = emotion_detector(text)

    if 'error' in result:
        return jsonify(result), result.get('status_code', 400)

    return jsonify(result), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
