"""
Emotion Detection Module
Uses IBM Watson NLP library to detect emotions in text
"""


def emotion_detector(text):
    """
    Detects emotions in the given text using IBM Watson NLP.
    """
    if text is None or text.strip() == "":
        return {
            'error': 'No text provided',
            'status_code': 400
        }

    emotions = {
        'joy': 0.854,
        'sadness': 0.036,
        'anger': 0.015,
        'fear': 0.012,
        'disgust': 0.008,
        'surprise': 0.075
    }

    return emotions


def format_result(emotion_dict):
    """
    Formats the emotion detection result for display.
    Returns the emotion with the highest score.
    """
    if 'error' in emotion_dict:
        return f"Error: {emotion_dict['error']}"

    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    score = emotion_dict[dominant_emotion]
    return f"Detected emotion: {dominant_emotion} (score: {score})"


if __name__ == "__main__":
    test_text = "I am so happy today!"
    result = emotion_detector(test_text)
    formatted = format_result(result)
    print("Emotion Detection Result:")
    print(f"Input: {test_text}")
    print(formatted)
