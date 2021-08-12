# 将文字转语音mp3
import base64

import requests
from pathlib import Path

output_dir = 'output'


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
    p = Path(output_dir)
    p.mkdir(exist_ok=True)
    with open(output_dir + '/' + filename, "wb") as fp:
        content = base64_text.split(",")[1]
        fp.write(base64.b64decode(content))
