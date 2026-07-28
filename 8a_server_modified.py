"""
Flask Web Server for Emotion Detection Application
Running static code analysis with pylint
"""
# pylint: disable=ungrouped-imports
from flask import Flask, request, jsonify  # noqa: F401
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotion-detector', methods=['POST'])
def emotion_detector_api():
    """
    Emotion Detection API endpoint
    """
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({
            'error': 'Invalid JSON format',
            'status_code': 400
        }), 400

    text = data['text']

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
