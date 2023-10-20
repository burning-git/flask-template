from flask import Flask
import os
import json
import requests

import DingdingHelp

import time
import sched

app = Flask(__name__)
scheduler = sched.scheduler(time.time, time.sleep)


def run_scheduler():
    # 30s 1 优先级
    scheduler.enter(30, 1, checkApp)
    print_time()
def checkApp():
    urls = "https://mini.9191pow.com/ocr/textServicesRuning"
    end = requests.get(urls)
    print(end.status_code)
    if (end.status_code == 404) | (end.status_code == 502):
        DingdingHelp.sendDingdingMsg("服务器异常了，ocr")
        print("服务器异常了，ocr")
    else:
        print("正常")
    return 'hello world'
@app.route('/')
def index():
    print("GET /")
    return "Welcome, this is a Flask app deployed on Zeabur"

if __name__ == '__main__':
    run_scheduler()
    app.run(debug=True, port=os.getenv("PORT", default=5000), host='0.0.0.0')

