from flask import Flask, request
from flask_cors import CORS
from auth import serve, handler

app = Flask(__name__)

@app.route('/page/<filename>')
def page(filename):
    return serve(filename)


@app.route('/auth', methods=['POST'])
def auth():
    
    data = request.get_json()
    print(data)

    return handler(data)
    


if __name__=='__main__':
    app.run('0.0.0.0', debug=True, port=8080)