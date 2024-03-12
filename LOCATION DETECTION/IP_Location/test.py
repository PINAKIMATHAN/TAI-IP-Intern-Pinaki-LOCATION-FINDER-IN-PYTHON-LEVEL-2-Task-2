import tkinter as tk
from tkinter import ttk, font
import geo
import random
import string

class GeoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hacker-like Geo Information")
        self.geometry("600x600")
        self.configure(bg="cornflower blue")

        self.create_widgets()

    def create_widgets(self):
        self.font = font=('Arial', 15, "bold")

        self.ip_button = ttk.Button(self, text="Get IP", command=self.animate_display_ip)
        self.ip_button.pack(pady=20)

        self.country_button = ttk.Button(self, text="Get Country", command=self.animate_display_country)
        self.country_button.pack(pady=20)

        self.geo_data_button = ttk.Button(self, text="Get Geo Data", command=self.animate_display_geodata)
        self.geo_data_button.pack(pady=20)

        self.ptr_button = ttk.Button(self, text="Get PTR Data", command=self.animate_display_ptr)
        self.ptr_button.pack(pady=20)

        self.output_text = tk.Text(self, width=70, height=20, bg="blue4", fg="yellow", font=self.font)
        self.output_text.pack(pady=20)

    def random_string(self, length=40):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

    def animate_effect(self, display_function):
        self.output_text.delete(1.0, tk.END)
        for _ in range(10):
            self.output_text.insert(tk.END, self.random_string() + '\n')
            self.update_idletasks()
            self.after(50, self.output_text.delete(1.0, tk.END))
        display_function()

    def animate_display_ip(self):
        self.animate_effect(self.display_ip)

    def animate_display_country(self):
        self.animate_effect(self.display_country)

    def animate_display_geodata(self):
        self.animate_effect(self.display_geodata)

    def animate_display_ptr(self):
        self.animate_effect(self.display_ptr)

    def display_ip(self):
        ip = geo.getIP()
        self.output_text.insert(tk.END, f"IP Address: {ip}")

    def display_country(self):
        ip = geo.getIP()
        country_plain = geo.getCountry(ip, 'plain')
        country_json = geo.getCountry(ip, 'json')
        self.output_text.insert(tk.END, f"Country (Plain): {country_plain}\n")
        self.output_text.insert(tk.END, f"Country (JSON): {country_json}")

    def display_geodata(self):
        ip = geo.getIP()
        geodata = geo.getGeoData(ip)
        for key, value in geodata.items():
            self.output_text.insert(tk.END, f"{key.capitalize()}: {value}\n")

    def display_ptr(self):
        ip = geo.getIP()
        ptr = geo.getPTR(ip)
        self.output_text.insert(tk.END, f"PTR Data: {ptr}")


if __name__ == "__main__":
    app = GeoApp()
    app.mainloop()
