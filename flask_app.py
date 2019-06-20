from flask import Flask, render_template, request
import os
from habitica_app import complete_habitica_todo, update_reward
import subprocess

# Flask setup
app = Flask(__name__)
app.config['SECRET_KEY'] = "DefaultSecret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/habiticawebhook", methods=["POST"])
def habitica_webhook():
    data = request.get_json()
    type = data["task"]["type"]
    print(f"Received type {type}")

    if type == "reward":
        print("Updating reward")
        update_reward(data["task"]["id"], data["task"]["value"] * 2)

    return "", 200


# Deprecated
# @app.route("/complete", methods=["POST"])
# def complete():
#     data = request.get_json()
#     event_name = data["event_data"]["content"]
#     complete_habitica_todo(event_name)
#     return "OK"



# Run Flask if file is interpreted
if __name__ == "__main__":
    os.environ["FLASK_APP"] = "application.py"
    try:
        current = subprocess.check_output(["lsof", "-t", "-i:5000"])
        current = max(current.decode("utf-8").split("\n"))
        print(f"kill {current}")
        os.system(f"kill {current}")
    except:
        pass
    os.system("flask run")
