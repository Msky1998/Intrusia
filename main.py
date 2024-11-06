import customtkinter as ctk
from sidebar import Sidebar
from home_page import HomePage
from real_time_analysis import RealTimeAnalysis
from simulation import Simulation
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Intrusia App")
        self.geometry("800x600")
        image_path = os.path.join(os.path.dirname(__file__), 'images', 'cadenas.ico')
        self.iconbitmap(image_path)  # Choix de thème de couleur


        self.sidebar = Sidebar(self, self.show_page,self.toggle_theme)
        self.sidebar.pack(side="left", fill="y")

        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.home_page = HomePage(self.content_frame)
        self.real_time_analysis_page = RealTimeAnalysis(self.content_frame)
        self.simulation_page = Simulation(self.content_frame)

        self.show_page("home")
    def show_page(self, page_name):
        for page in [self.home_page, self.real_time_analysis_page, self.simulation_page]:
            page.pack_forget()

        if page_name == "home":
            self.home_page.pack(fill="both", expand=True)
        elif page_name == "real_time_analysis":
            self.real_time_analysis_page.pack(fill="both", expand=True)
        elif page_name == "simulation":
            self.simulation_page.pack(fill="both", expand=True)
    def toggle_theme(self):
        current_theme = ctk.get_appearance_mode()
        if current_theme == "Light":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

if __name__ == "__main__":
    app = App()
    app.mainloop()
