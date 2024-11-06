import joblib
from sklearn.preprocessing import LabelEncoder

def load_model():
    return joblib.load("model/random_forest_model.pkl")

def encode_data(packet):
    # Encoder les données de manière similaire à l'entraînement
    label_encoder = LabelEncoder()
    encoded_packet = []
    for key, value in packet.items():
        if isinstance(value, str):
            encoded_packet.append(label_encoder.fit_transform([value])[0])
        else:
            encoded_packet.append(value)
    return encoded_packet

