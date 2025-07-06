# ModernCard.py – Simplified and elegant card UI

import tkinter as tk
from tkX.tkx import ModernLabel, ModernRoundedButton


class ModernCard(tk.Frame):
    def __init__(self, master=None, title="Card Title", description="A clean and modern card component.", button_text="Try it", command=None, **kwargs):
        super().__init__(master, bg="#1e1e1e", highlightthickness=0, **kwargs)

        self.title_label = ModernLabel(self, text=title, font=("Orbitron", 16, "bold"), fg="white", bg="#1e1e1e")
        self.desc_label = ModernLabel(self, text=description, font=("Poppins", 10), fg="#ccc", bg="#1e1e1e", wraplength=220, justify="left")
        self.action_button = ModernRoundedButton(self, text=button_text, command=command, font=("Orbitron", 10, "bold"), fg="#1e1e1e", bg="#7cfc00", padx=12, pady=6)

        self.title_label.pack(anchor="w", pady=(5, 2), padx=10)
        self.desc_label.pack(anchor="w", pady=(0, 10), padx=10)
        self.action_button.pack(anchor="e", padx=10, pady=(0, 10))

        self.bind("<Enter>", lambda e: self._hover(True))
        self.bind("<Leave>", lambda e: self._hover(False))

    def _hover(self, on):
        bg_color = "#252525" if on else "#1e1e1e"
        self.configure(bg=bg_color)
        self.title_label.configure(bg=bg_color)
        self.desc_label.configure(bg=bg_color)

