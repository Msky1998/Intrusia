import customtkinter as ctk
from utils import load_model, encode_data
import random
import matplotlib.pyplot as plt

class Simulation(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.start_button = ctk.CTkButton(self, text="Lancer 1000 paquets pour analyse", command=self.start_simulation)
        self.start_button.pack(expand=True,fill=None)

        self.model = load_model()

    def start_simulation(self):
        normal_count = 0
        intrusion_count = 0

        for _ in range(1000):
            packet = self.generate_random_packet()
            if self.detect_intrusion(packet):
                intrusion_count += 1
            else:
                normal_count += 1

        self.plot_results(normal_count, intrusion_count)

    def generate_random_packet(self):
        # Générer un paquet de données aléatoire
        return {
            "protocol_type": random.choice(["tcp", "udp","icmp"]),
            "service": random.choice(["http", "ftp_data", "other","private","remote_job","name","mtp","eco_i","netbios_ns","telnet"]),
            "flag": random.choice(["SF", "S0","REJ","RSTR","SH"]),
            "src_bytes": random.randint(0, 1024),
            "dst_bytes": random.randint(0, 1024),
            "count": random.randint(0, 300),
            "same_srv_rate": random.uniform(0, 1),
            "diff_srv_rate": random.uniform(0, 1),
            "dst_host_same_srv_rate": random.uniform(0, 1),
            "dst_host_same_src_port_rate": random.uniform(0, 1)
        }

    def detect_intrusion(self, packet):
        # Encoder les données et prédire avec le modèle
        encoded_packet = encode_data(packet)
        prediction = self.model.predict([encoded_packet])
        return prediction == 0  # Supposons que 0 signifie intrusion

    def plot_results(self, normal_count, intrusion_count):
        labels = ["Normal", "Intrusion"]
        sizes = [normal_count, intrusion_count]
        colors = ["#4CAF50", "#FF5733"]

        plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%")
        plt.title("Proportion des paquets")
        plt.show()
