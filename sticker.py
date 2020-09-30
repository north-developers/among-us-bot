from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from textwrap import wrap
from random import randint
import requests


def among_us(text):
    url = "https://raw.githubusercontent.com/KeyZenD/AmongUs/master/"
    random = randint(1,12)
    
    font = ImageFont.truetype(BytesIO(requests.get(url + "bold.ttf").content), 60) 
    imposter = Image.open(BytesIO(requests.get(f"{url}{random}.png").content))
    text_ = "\n".join(["\n".join(wrap(part, 30)) for part in text.split("\n")])
    w, h = ImageDraw.Draw(Image.new("RGB", (1, 1))).multiline_textsize(text_, font, stroke_width=2)
    text = Image.new("RGBA", (w + 30, h + 30))
    ImageDraw.Draw(text).multiline_text((15,15), text_, "#FFF", font, stroke_width=2, stroke_fill="#000")
    w = imposter.width + text.width + 10
    h = max(imposter.height, text.height)
    image = Image.new("RGBA", (w, h))
    image.paste(imposter, (0, h-imposter.height), imposter)
    image.paste(text, (w-text.width, 0), text)
    image.thumbnail((512, 512))
    output = BytesIO()
    output.name = "imposter.webp"
    image.save(output)
    output.seek(0)

    return output
