# bad API maxxxer onekey app

A minimal Python desktop app that serves random content at the press of the space key key. Long press to change the mode : 4 mode, 4 API.

## Modes

| Mode | Color | Content |
|------|-------|-------------------------------|
| Joke | Purple | Random dad jokes |
| Space | Blue | NASA Astronomy Picture of the Day |
| Tech | Green | Top story from Hacker News |
| Fact | Red | Random useless fact |

## Controls

- Short press  - fetch new content
- Long press  (> 0.5s) - switch mode

## Setup

Requirements: 
- Python 3.12+

- NASA API key (optional but useful if you wanna test this mode) --> Get a free key at https://api.nasa.gov


Clone the repo and set up the environment:


```bash
git clone https://github.com/Gabouin/reddit-random
cd reddit-random
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install customtkinter requests
```

<br>

Optionally add a NASA API key in a .env file (a demo key is used by default):

```bash
echo "NASA_API_KEY=your_key_here" > .env
```

<br>

Run the app:


```bash
python main.py
```

## Run



## APIs

- icanhazdadjoke.com - jokes
- api.nasa.gov - space
- hacker-news.firebaseio.com - tech
- uselessfacts.jsph.pl - facts



