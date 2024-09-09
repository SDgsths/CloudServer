import json
import random

colors = ["red", "blue", "purple", "pink", "orange", "yellow", "green"]

class SessionManager:

    def get_sessions():
        db = json.load(open("Databases/sessions.json", 'r'))
        return db
    
    def find_userSession(ip):
        db = SessionManager.get_sessions()
        
        for session in db:
            if session["ip"] == ip:
                return session["user"]
            
        return SessionManager.create_session(ip)
    
    def get_UserColor(user):
        db = SessionManager.get_sessions()
        
        for session in db:
            if session["user"] == user:
                return session["color"]
            
        
    
    def create_session(ip):
        db = SessionManager.get_sessions()

        username = f"user{random.randint(100000,9999999)}"
        new_session = {"ip": ip, "user": username, "color": random.choice(colors)}

        db.append(new_session)
        json.dump(db, open("Databases/sessions.json", 'w'))

        return username