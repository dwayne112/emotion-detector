"""
Emotion Detection Module
Uses IBM Watson NLP library to detect emotions in text
"""
import requests
import json


def emotion_detector(text):
    """
    Detects emotions in the given text using IBM Watson NLP.

    Args:
        text (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing emotion scores for:
              joy, sadness, anger, fear, disgust, surprise
              and a dominant_emotion key, and status_code.
              Returns None if input is invalid.
    """
    if text is None or text.strip() == "":
        return None

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text}}

    response = requests.post(url, headers=header, json=payload, timeout=30)

    response_json = json.loads(response.text)
    emotions = response_json["emotion_pred"]
    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]
    surprise = emotions.get("surprise", 0.0)

    emotion_scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "surprise": surprise
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "surprise": surprise,
        "dominant_emotion": dominant_emotion,
        "status_code": 200
    }


def format_result(emotion_dict):
    """
    Formats the emotion detection result for display.
    Returns a string representation of emotion scores.
    """
    if emotion_dict is None:
        return "Invalid input!"

    lines = []
    for emotion in ["joy", "sadness", "anger", "fear", "disgust", "surprise"]:
        if emotion in emotion_dict and emotion_dict[emotion] is not None:
            lines.append(f"'{emotion}': {emotion_dict[emotion]}")

    if "dominant_emotion" in emotion_dict:
        lines.append(f"'dominant_emotion': '{emotion_dict['dominant_emotion']}'")

    return "{" + ", ".join(lines) + "}"


if __name__ == "__main__":
    test_text = "I am so happy today!"
    result = emotion_detector(test_text)
    formatted = format_result(result)
    print("Emotion Detection Result:")
    print(f"Input: {test_text}")
    print(formatted)
