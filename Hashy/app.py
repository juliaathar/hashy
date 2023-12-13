from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

@app.route('/breakHash', methods=['GET'])
def break_hash():
    hash_value = request.args.get('hash')
    url = f"https://md5decrypt.net/Api/api.php?hash={hash_value}&hash_type=md5&email=cybercroc@protonmail.com&code=c5ddc9bbd5b07c45"

    try:
        response = requests.get(url)
        data = response.text
        return data
    except Exception as e:
        print(e)
        return jsonify(error='Internal Server Error'), 500

if __name__ == '__main__':
    app.run(port=5000)
