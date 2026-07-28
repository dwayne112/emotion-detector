from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector, format_result

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze or text_to_analyze.strip() == "":
        return jsonify({
            'error': 'No text provided',
            'status_code': 400
        }), 400

    response = emotion_detector(text_to_analyze)
    response_text = (
        f"anger: {response['anger']}, "
        f"disgust: {response['disgust']}, "
        f"fear: {response['fear']}, "
        f"joy: {response['joy']}, "
        f"sadness: {response['sadness']}, "
        f"dominant_emotion: {response['dominant_emotion']}"
    )
    return jsonify({'response': response_text})


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    print('Starting Emotion Detection Server...')
    print('API endpoint: http://127.0.0.1:5000/emotionDetector')
    app.run(host='0.0.0.0', port=5000, debug=True)
