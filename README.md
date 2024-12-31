# muspixel

<div align = "center"> 
<p>A NeoPixel LED-powered live album cover display for your music.</p>
<img src = "https://github.com/user-attachments/assets/ded114c5-6cf0-462a-9bef-58700c014dd3" alt="The albums This is All Yours by Alt-J and Loose Friends by the Academic shown on an 8x8 LED display."/>
</div>



## About
Muspixel converts an 8x8 NeoPixel LED matrix[^2] and ESP8266 to an album cover display. Connect it to your [Last.fm](https://www.last.fm/) account and see your scrobbles on the display in real[^1] time!

## Usage and Development
### Hardware Setup 
| Component | Quantity |
| --------- | -------- |
| 8x8 neopixel (CJMCU) matrix | 1 |
| ESP8266 microcontroller | 1 |
| Male-male connecting wires | 5 |
| Breadboard | 1 |

<div align = "center" ><img src = "https://github.com/user-attachments/assets/a6115678-ae59-49d6-9ce1-e830b0b8ee7d" width = 800/></div>


1. Set up your wiring and components as shown in the image[^3] above (a better image is a work in progress)
2. Connect the ESP8266 to a laptop and install the [WLED MoonModules binary](https://mm.kno.wled.ge/basics/install-binary/).
3. Connect and modify it to work on your home Wi-Fi network, as prompted. Note the IP address provided in this step.
4. Visit the `<ipaddress>/settings/2D` page. If you're using an identical configuration as me, change the LED panel layout settings to replicate the following image. 


### Software Setup
1. Clone the repository
```
git clone https://github.com/phthallo/muspixel
```

2. Install the project's dependencies in a virtual environment.
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements
```

3. Create a Last.fm [API account](https://www.last.fm/api/account/create).

4. Fill out the `.env` file, renaming it from `.env.example` to `.env`.
```
CLIENT_IP=<Client IP from above>
LASTFM_API=<API key from Step 3>
LASTFM_USERNAME=<Your Last.fm username>
```

5. Start `main.py` and enjoy the colours of vaguely familiar but extremely pixellated album covers.


## Infrequently asked questions
**Why Last.fm and not Spotify?**

I use Navidrome too, and wanted both Spotify and Navidrome to be able to work with this.

**but like why (in general)**

why not 

[^1]: Subject to API rate limits => right now, it refreshes every 25 seconds.
[^2]: This should work with larger LED matrix sizes, although I don't have any to test it with. To accomodate for this, set the environment variables `SCREEN_X` and `SCREEN_Y` to adjust the dimensions.
[^3]: I swear the breadboard isn't dirty the lighting just makes it look bad 😭
