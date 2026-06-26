import tkinter as tk
import requests
import time
import random

MODES = ["joke", "space", "tech", "fact"]
MODE_COLORS = {
    "joke": "#2d1b4e",
    "space": "#0d1b2a",
    "tech": "#1a2e1a",
    "fact": "#2e1a1a"
}

MODE_LABELS = {
    "joke": "some jokes",
    "space": "some space facts",
    "tech": "some tech news",
    "fact": "just fully random fact lol"
}

current_mode_index = 0
press_time = 0

def get_content():
    mode = MODES[current_mode_index]

    if mode == "joke":
        response = requests.get(
            "https://icanhazdadjoke.com/",
            headers={"Accept": "application/json"}
        )
        return response.json()["joke"]
    