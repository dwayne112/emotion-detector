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


if __name__ == "__main__":
    test_text = "I am so happy today!"
    result = emotion_detector(test_text)
    print("Emotion Detection Result:")
    print(f"Input: {test_text}")
    print(f"Result: {result}")
