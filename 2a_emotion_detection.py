import requests
import json

def emotion_detector(text):
    if text is None or text.strip() == "":
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'surprise': None,
            'dominant_emotion': None, 'status_code': 400
        }
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text}}
    response = requests.post(url, headers=header, json=payload, timeout=30)
    response_json = json.loads(response.text)
    emotions = response_json['emotion_pred']
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    surprise = emotions.get('surprise', 0.0)
    emotion_scores = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'surprise': surprise}
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    return response.text

if __name__ == "__main__":
    test_text = "I am so happy today!"
    result = emotion_detector(test_text)
    print("Emotion Detection Result:")
    print(f"Input: {test_text}")
    print(f"Result: {result}")
