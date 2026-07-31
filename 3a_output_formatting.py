import requests
import json


def emotion_detector(text_to_analyze):
    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_object = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, timeout=10, json=json_object, headers=header)
    response_dict = json.loads(response.text)
    emotions = response_dict["emotionPredictions"][0]["emotion"]
    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]
    emotion_scores = {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness}
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }


if __name__ == "__main__":
    test_text = "I am so happy today!"
    result = emotion_detector(test_text)
    print("Emotion Detection Result:")
    print(f"Input: {test_text}")
    print(f"Result: {result}")