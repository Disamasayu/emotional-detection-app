import requests  # Library untuk mengirim permintaan HTTP
import json      # Library untuk mengolah data JSON

def emotion_detector(text_to_analyze):
    # URL endpoint dari layanan Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Header yang diperlukan oleh API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Format data (payload) yang dikirim
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Mengirim permintaan POST
    response = requests.post(url, json = myobj, headers=header)
    
    # Mengembalikan teks respons dari API
    return response.text
