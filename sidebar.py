import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, show_page, toggle_theme):
        super().__init__(master)
        self.master = master
        self.show_page = show_page
        self.toggle_theme = toggle_theme

        self.welcome_button = ctk.CTkButton(self, text="Bienvenue", command=lambda: self.show_page("home"))
        self.welcome_button.pack(pady=10)

        self.real_time_analysis_button = ctk.CTkButton(self, text="Analyse temps réel", command=lambda: self.show_page("real_time_analysis"))
        self.real_time_analysis_button.pack(pady=10)

        self.simulation_button = ctk.CTkButton(self, text="Lancer une simulation", command=lambda: self.show_page("simulation"))
        self.simulation_button.pack(pady=10)

        self.theme_button = ctk.CTkButton(self, text="Changer de thème", command=self.toggle_theme)
        self.theme_button.pack(pady=10)

        self.quit_button = ctk.CTkButton(self, text="Quitter", command=self.quit)
        self.quit_button.pack(pady=10)

    def quit(self):
        self.master.destroy()
