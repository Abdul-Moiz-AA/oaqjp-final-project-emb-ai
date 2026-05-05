import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion of the given text using the Watson NLP Emotion Predict function.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status() # Raise an exception for HTTP errors

        # Parse the JSON response
        response_json = response.json()

        # Extract emotion scores
        # Assuming the structure is response_json['document']['emotion']
        emotions = response_json.get('document', {}).get('emotion', {})
        
        anger_score = emotions.get('anger', 0.0)
        disgust_score = emotions.get('disgust', 0.0)
        fear_score = emotions.get('fear', 0.0)
        joy_score = emotions.get('joy', 0.0)
        sadness_score = emotions.get('sadness', 0.0)

        # Find the dominant emotion
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        print(f"Error during API request: {e}")
        return None
