import time
import os 
import threading
import requests
from dotenv import load_dotenv
from songs import get_recent_playing, parse_album_image

load_dotenv()
def main():
    if not ("SCREEN_X" in os.environ or "SCREEN_Y" in os.environ):
        x, y = 8, 8
    song = get_recent_playing(os.environ["LASTFM_USERNAME"], os.environ["LASTFM_API"])
    payload = {
        "on": True,
        "bri": 80,
        "seg": {
            "id": 0,
            "i": parse_album_image(song['recenttracks']['track'][0]['image'][2]['#text'], x, y)
        }
    }
    response = requests.post(f"{os.environ["CLIENT_IP"]}/json", json=payload)
    threading.Timer(25, main).start()

main()