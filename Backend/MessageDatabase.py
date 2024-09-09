import json
from Backend.SessionManager import SessionManager

class DB:

    def get_messageDB():
        db = json.load(open("Databases/messages.json", 'r'))
        return db
    

    def get_html():
        db = DB.get_messageDB()
        html = open("HTML/home.html", 'r').read()

        msg = """<div class="message">
                <span class="user" style="color: [COLOR];">[USER]:</span> [CONTENT]
            </div>"""

        msgs = ""

        for message in db:
            new_msg = msg.replace("[USER]", message["User"]).replace("[CONTENT]", message["content"]).replace("[COLOR]", message["color"])

            msgs += new_msg


        return html.replace("<!--[MSGS]-->", msgs)
    
    def Send_Message(user, content, color):
        db = DB.get_messageDB()

        
        last_msg = db[len(db) - 1]

        id = last_msg["ID"] + 1
        new_msg = {'ID': id, "User": user, "content": content, "color": color}
        if content == "":
            return
        db.append(new_msg)
        json.dump(db, open("Databases/messages.json", 'w'))







