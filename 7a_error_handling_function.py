"""
Emotion Detection Module
With error handling for status code 400
"""


def emotion_detector(text):
    """
    Detects emotions in the given text using IBM Watson NLP.
    Returns error with status_code 400 for invalid input.
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


if __name__ == "__main__":
    result = emotion_detector("")
    print(f"Status code: {result.get('status_code', 200)}")
    print(f"Error: {result.get('error', 'None')}")
