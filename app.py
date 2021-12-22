# FLASK
from flask import Flask
app = Flask(__name__)

# Speedtest
import speedtest

@app.route('/')
def get():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res_dict = s.results.dict()
    result = {
            "download": res_dict["download"] / 1048576, # from bits/s to megabits/s
            "upload": res_dict["upload"] / 1048576, # from bits/s to megabits/s
            "ping": res_dict["ping"] # in ms
            }
    return result
