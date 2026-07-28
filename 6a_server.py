from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector, format_result

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_web():
    text_to_analyze = request.args.get("textToAnalyze")
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Please provide text to analyze via ?textToAnalyze=query"
    result = emotion_detector(text_to_analyze)
    if isinstance(result, dict) and 'error' in result:
        return f"Error: {result['error']}"
    try:
        result_dict = eval(result) if isinstance(result, str) else result
        response_text = f"anger: {result_dict.get('anger', 0)}, disgust: {result_dict.get('disgust', 0)}, fear: {result_dict.get('fear', 0)}, joy: {result_dict.get('joy', 0)}, sadness: {result_dict.get('sadness', 0)}, dominant_emotion: {result_dict.get('dominant_emotion', 'N/A')}"
    except:
        response_text = str(result)
    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
