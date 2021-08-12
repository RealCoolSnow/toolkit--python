# 将文字转语音mp3
import base64

import requests
from pathlib import Path

OUTPUT_DIR = 'output'


def text2audio(text, filename):
    url = "https://cloud.baidu.com/aidemo"
    data = {
        "type": "tns",
        "per": 5118,
        "spd": 5,
        "pit": 5,
        "vol": 5,
        "aue": 6,
        "tex": text
    }
    resp = requests.post(url, data=data).json()
    base64_text = resp["data"]
    p = Path(OUTPUT_DIR)
    p.mkdir(exist_ok=True)
    with open(OUTPUT_DIR + '/' + filename, "wb") as fp:
        content = base64_text.split(",")[1]
        fp.write(base64.b64decode(content))
