import json
import requests


def emotion_detector(text_to_analyze):
    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_object = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, timeout=10, json=json_object, headers=header)

    if response.status_code == 200:
        response_dict = json.loads(response.text)
        anger = response_dict["emotionPredictions"][0]["emotion"]["anger"]
        disgust = response_dict["emotionPredictions"][0]["emotion"]["disgust"]
        fear = response_dict["emotionPredictions"][0]["emotion"]["fear"]
        joy = response_dict["emotionPredictions"][0]["emotion"]["joy"]
        sadness = response_dict["emotionPredictions"][0]["emotion"]["sadness"]
        emotion_scores = {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness}
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }


if __name__ == "__main__":
    test_text = "I am so happy today!"
    result = emotion_detector(test_text)
    print("Emotion Detection Result:")
    print(f"Input: {test_text}")
    print(f"Result: {result}")