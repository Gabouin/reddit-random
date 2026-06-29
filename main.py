import os

def load_env(path=".env"):
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key] = value

load_env()
NASA_API_KEY = os.environ.get("NASA_API_KEY", "DEMO_KEY")

import tkinter as tk
import urllib.request
import json
import time
import random

def shorten(text, limit=200):
    if len(text) > limit:
        return text[:limit].rstrip() + "..."
    return text


MODES = ["joke", "space", "tech", "fact"]
MODE_COLORS = {
    "joke": "#7b2ff7",
    "space": "#0066ff",
    "tech": "#00c853",
    "fact": "#ff3d00"
}
MODE_LABELS = {
    "joke": "some unfunny jokes because the API sucks",
    "space": "some space related news title form the NASA API",
    "tech": "some tech news (actually I don't even understand those)",
    "fact": "just fully random fact lol"
}

current_mode_index = 0
press_time = 0
release_job = None

def fetch_json(url, headers=None):
    base = {"User-Agent": "SpacePress/1.0 (https://github.com/Gabouin)"}
    if headers:
        base.update(headers)
    req = urllib.request.Request(url, headers=base)
    with urllib.request.urlopen(req, timeout=5) as response:
        return json.loads(response.read().decode())

def get_content():
    mode = MODES[current_mode_index]

    if mode == "joke":
        data = fetch_json(
            "https://icanhazdadjoke.com/",
            headers={"Accept": "application/json"}
        )
        return data["joke"]

    elif mode == "space":
        data = fetch_json(f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}&count=1")
        return shorten(data[0]["title"])

    elif mode == "tech":
        ids = fetch_json("https://hacker-news.firebaseio.com/v0/topstories.json")[:10]
        story_id = random.choice(ids)
        story = fetch_json(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json")
        return story["title"]

    elif mode == "fact":
        data = fetch_json("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
        return data["text"]

def show_content():
    global is_loading
    if is_loading:
        return
    is_loading = True
    label.config(text="loading...")
    window.update()
    try:
        content = get_content()
    except Exception as e:
        content = f"erreur : {e}"
    label.config(text=content)
    is_loading = False

def change_mode():
    global current_mode_index
    current_mode_index = (current_mode_index + 1) % len(MODES)
    mode = MODES[current_mode_index]
    window.configure(bg=MODE_COLORS[mode])
    label.configure(bg=MODE_COLORS[mode])
    mode_label.configure(bg=MODE_COLORS[mode])
    mode_label.config(text=MODE_LABELS[mode] + "  -  long press to switch modes")
    label.config(text="Press SPACE")

key_down = False
press_time = 0
release_job = None
is_loading = False

def on_key_press(event):
    global key_down, press_time, release_job
    if release_job is not None:
        window.after_cancel(release_job)
        release_job = None
    if not key_down:
        key_down = True
        press_time = time.time()

def on_key_release(event):
    global release_job
    release_job = window.after(120, finalize_release)

def finalize_release():
    global release_job, key_down
    release_job = None
    key_down = False
    duration = time.time() - press_time
    if duration < 0.5:
        show_content()
    else:
        change_mode()

window = tk.Tk()
window.title("Space Press")
window.geometry("600x400")
window.configure(bg=MODE_COLORS["joke"])

mode_label = tk.Label(
    window,
    text=MODE_LABELS["joke"] + "  -  long press to switch modes",
    font=("Arial", 12),
    fg="#ffffff",
    bg=MODE_COLORS["joke"]
)
mode_label.pack(pady=20)

label = tk.Label(
    window,
    text="Press SPACE",
    wraplength=500,
    font=("Arial", 16),
    fg="white",
    bg=MODE_COLORS["joke"]
)
label.pack(expand=True)

window.bind("<KeyPress-space>", on_key_press)
window.bind("<KeyRelease-space>", on_key_release)
window.mainloop()