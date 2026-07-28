from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector, format_result

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    text_to_analyze = request.args.get("textToAnalyze")
    if not text_to_analyze or text_to_analyze.strip() == "":
        return jsonify({
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "surprise": None,
            "dominant_emotion": None,
            "status_code": 400
        }), 400

    result = emotion_detector(text_to_analyze)
    if result is None:
        return jsonify({
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "surprise": None,
            "dominant_emotion": None,
            "status_code": 400
        }), 400

    formatted = format_result(result)
    return jsonify({"formatted_response": formatted})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
