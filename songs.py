import io 
import requests
from PIL import Image
# Get currently playing track from Last.fm. Mainly because it has integration with Navidrome too.

def _rgb_to_hex(rgb: tuple) -> str:
    """Convert an RGB tuple to hex.

    Args:
        rgb (tuple): An RGB (red, green, blue) tuple representing a colour.

    Returns:
        str: The equivalent hex code *without* the beginning #
    """
    return "{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def get_recent_playing(lastfm_username: str, lastfm_api_key: str) -> object:
    """Get the most recently played song from the given Last.fm account.

    Args:
        lastfm_username (string): Username of the Last.fm account to watch.
        lastfm_api_key (string): Last.fm API key.

    Returns:
        JSON: Metadata of the most recently listened to track.
    """
    response = requests.get(f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={lastfm_username}&api_key={lastfm_api_key}&format=json&limit=1")
    return response.json()
    
def parse_album_image(image_url: str, x: int, y: int) -> list[str]:
    """Convert the currently playing song's album image into a x*y pixel format. 

    Args:
        image_url (str): URL to an album image provided by the Last.fm API
        x (int): Width of the pixel display.
        y (int): Height of the pixel display

    Returns:
        list[str]: List of coloured pixels
    """
    post_req = []
    fetch_img = requests.get(image_url)
    img = Image.open(io.BytesIO(fetch_img.content)).convert("RGB")
    resized = img.resize((x,y), resample=Image.Resampling.BILINEAR)

    for x_pixel in range(x):
        for y_pixel in range(y):
            post_req.append(
                _rgb_to_hex(resized.getpixel((x_pixel, y_pixel))))
    return post_req