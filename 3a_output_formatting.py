import requests
import json


def emotion_detector(text):
    if text is None or text.strip() == "":
        return None
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text}}
    response = requests.post(url, headers=header, json=payload, timeout=30)
    return response.text


def format_result(emotion_dict):
    if emotion_dict is None:
        return "Invalid input!"
    lines = []
    for emotion in ['joy', 'sadness', 'anger', 'fear', 'disgust', 'surprise']:
        if emotion in emotion_dict and emotion_dict[emotion] is not None:
            lines.append(f"'{emotion}': {emotion_dict[emotion]}")
    if 'dominant_emotion' in emotion_dict:
        lines.append(f"'dominant_emotion': '{emotion_dict['dominant_emotion']}'")
    return "{" + ", ".join(lines) + "}"


if __name__ == "__main__":
    test_text = "I am so happy today!"
    result = emotion_detector(test_text)
    result_dict = json.loads(result)
    emotions = result_dict['emotion_pred']
    formatted = format_result(emotions)
    print("Emotion Detection Result:")
    print(f"Input: {test_text}")
    print(formatted)
