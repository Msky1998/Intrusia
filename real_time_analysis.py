import customtkinter as ctk
from utils import load_model, encode_data
import threading
from scapy.all import sniff, IP, TCP, UDP
import tkinter.messagebox as messagebox

class RealTimeAnalysis(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.text_area = ctk.CTkTextbox(self, height=400,width=600)
        self.text_area.pack(pady=20)
        self.start_button = ctk.CTkButton(self, text="Lancer une attaque", command=self.start_attack)
        self.start_button.pack(side="left",padx=10)

        self.stop_button = ctk.CTkButton(self, text="Arrêter l'analyse", command=self.stop_analysis)
        self.stop_button.pack(side="right",padx=10)


        self.model = load_model()
        self.running = False

        self.start_analysis()

    def start_analysis(self):
        self.running = True
        threading.Thread(target=self.analyze_packets).start()

    def analyze_packets(self):
        def packet_callback(packet):
            if IP in packet:
                packet_data = self.extract_packet_features(packet)
                if self.detect_intrusion(packet_data):
                    self.text_area.insert("end", "Menace détectée!\n")
                    messagebox.showwarning("Alerte", "Intrusion détectée!")
                else:
                    self.text_area.insert("end", f"Paquet normal: {packet_data}\n")
                self.text_area.see("end")
                self.master.update_idletasks()

        sniff(prn=packet_callback, store=False, stop_filter=lambda x: not self.running)

    def extract_packet_features(self, packet):
        # Extrait les caractéristiques du paquet
        protocol_type = "tcp" if TCP in packet else "udp" if UDP in packet else "other"
        src_bytes = len(packet)
        dst_bytes = len(packet)
        count = 1
        same_srv_rate = 1.0
        diff_srv_rate = 0.0
        dst_host_same_srv_rate = 0.03
        dst_host_same_src_port_rate = 0.01

        return {
            "protocol_type": protocol_type,
            "service": "http",  # À ajuster selon les services réels
            "flag": "SF",  # À ajuster selon les flags réels
            "src_bytes": src_bytes,
            "dst_bytes": dst_bytes,
            "count": count,
            "same_srv_rate": same_srv_rate,
            "diff_srv_rate": diff_srv_rate,
            "dst_host_same_srv_rate": dst_host_same_srv_rate,
            "dst_host_same_src_port_rate": dst_host_same_src_port_rate
        }

    def detect_intrusion(self, packet):
        # Encoder les données et prédire avec le modèle
        encoded_packet = encode_data(packet)
        prediction = self.model.predict([encoded_packet])
        return prediction == 0  # Supposons que 0 signifie intrusion

    def start_attack(self):
        # Lancer une attaque minime
        self.text_area.insert("end", "Attaque lancée!\n")
        messagebox.showwarning("Alerte", "Intrusion détectée!")

        # Code pour lancer une attaque minime

    def stop_analysis(self):
        self.running = False
        self.text_area.insert("end", "Vous avez arrêté l'analyse.\n")
