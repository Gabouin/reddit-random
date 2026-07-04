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

## Setup and run

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



## APIs

- icanhazdadjoke.com - jokes
- api.nasa.gov - space
- hacker-news.firebaseio.com - tech
- uselessfacts.jsph.pl - facts

## Pictures

<img width="590" height="421" alt="Screenshot 2026-07-04 at 10 00 59 pm" src="https://github.com/user-attachments/assets/c3602256-f807-466a-a537-025c818f61b2" />
<img width="594" height="421" alt="Screenshot 2026-07-04 at 9 56 39 pm" src="https://github.com/user-attachments/assets/654dd359-180f-48a6-b2ad-d5238a60033f" />
<img width="589" height="424" alt="Screenshot 2026-07-04 at 9 57 42 pm" src="https://github.com/user-attachments/assets/cbfe063b-654c-46ae-aa69-f379341cfc8c" />
<img width="598" height="423" alt="Screenshot 2026-07-04 at 9 57 53 pm" src="https://github.com/user-attachments/assets/c1d7cf97-0689-441f-a3db-ba3afe52df61" />



