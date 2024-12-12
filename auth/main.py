import json
from flask import render_template

def user(username : str):
    with open('db.json', '+r') as file:
        contents = json.load(file)
        try:
            if (not contents["data"][username]):
                return False
        except:
            return False
    return True

def authenticate(username : str, password : str):
    if (not user(username=username)):
        return False
    with open('db.json', '+r') as file:
        contents = json.load(file)
        password_ = contents["data"][username]
        if (password_==password):
            return True
        else:
            return False

def create_account(username : str, password : str):
    try:
        if (not user(username=username)):
            with open('db.json', '+r') as file:
                contents = json.load(file)
            contents["data"][username] = password
            with open('db.json', 'w') as file:
                json.dump(contents, file, indent=4)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error creating account: {str(e)}")
        return False
    
def serve(query : str, templates_folder="templates"):
    return render_template(f"{query}.html", template_folder=templates_folder)


def handler(query : dict):
    """
    if user has to register, then they'll do:
    

    "type" : "register"

    if user has to authenticate, then they'll do:
    
    "type" : "authenticate"
    
    """
    print(query["type"])

    match (query["type"]):
        case "register":
            print("the user wants to register")
            if "username" not in query or "password" not in query:
                return {"success" : False}
            if query["username"] is None or query["password"] is None:
                return {"success" : False}
            if  (create_account(username=str(query["username"]), password=str(query["password"]))):
                return {"success" : True}
            else:
                return {"success" : False}
        case "authenticate":
            print("let's authenticate the user")
            if "username" not in query or "password" not in query:
                return {"success" : False}
            if query["username"] is None or query["password"] is None:
                return {"success" : False}
            if (authenticate(username=str(query["username"]), password=str(query["password"]))):
                return {"success" : True}
            else:
                return {"success" : False}
