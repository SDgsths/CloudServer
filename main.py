from Backend.MessageDatabase import DB
from Backend.SessionManager import SessionManager
from flask import *



app = Flask(__name__)

@app.route("/")
def base_route():

    return DB.get_html()


@app.route("/post_message", methods=["POST"])
def post_route():
    data = request.form

    ip = request.environ["REMOTE_ADDR"]

    user = SessionManager.find_userSession(ip)

    if user == None:
        return redirect("/")
    else:
        color = SessionManager.get_UserColor(user)
        DB.Send_Message(user, data["content"], color)
    
    return redirect("/")

app.run("0.0.0.0", 80, debug=True)