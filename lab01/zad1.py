from flask import Flask, request, Response

app = Flask(__name__)

def check_auth(username, password):
    return username == 'admin' and password == 'funny'

def authenticate():
    return Response(
        'Brak dostępu. Podaj poprawne dane logowania.\n', 401,
        {'WWW-Authenticate': 'Basic realm="Zabezpieczone API"'}
    )

@app.route('/api/secret')
def secret_data():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    return "Sukces! Masz dostep do chronionych danych.\n"

if __name__ == '__main__':
    app.run(port=5000)