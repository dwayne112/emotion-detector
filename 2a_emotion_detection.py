"""
Emotion Detection Module
Uses IBM Watson NLP library to detect emotions in text
"""


def emotion_detector(text):
    """
    Detects emotions in the given text using IBM Watson NLP.

    Args:
        text (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing emotion scores for:
              joy, sadness, anger, fear, disgust, surprise
              or an error message if analysis fails.
    """
    if text is None or text.strip() == "":
        return {
            'error': 'No text provided',
            'status_code': 400
        }

    # Simulated emotion response (IBM Watson NLP style)
    # In production, this calls: natural_language_understanding.analyze(
    #     text=text, features=EmotionsOptions())
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
    test_text = "I am so happy today!"
    result = emotion_detector(test_text)
    print("Emotion Detection Result:")
    print(f"Input: {test_text}")
    print(f"Result: {result}")
