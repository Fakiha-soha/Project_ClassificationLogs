
from sentence_transformers import SentenceTransformer
import joblib

transformer_model = SentenceTransformer('all-MiniLM-L6-v2')
classifier_model=joblib.load('H:/Kudu/classification_logs/models/log_classifier.joblib')

def classify_with_bert(log_msg):

    message_embedding=transformer_model.encode(log_msg)
    probabilities=classifier_model.predict_proba([message_embedding])[0]
    if max(probabilities)<0.5:
        return "unclassified"
    predicted_clas=classifier_model.predict([message_embedding])[0]

    return predicted_clas