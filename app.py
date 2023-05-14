from flask import Flask, jsonify


app = Flask(__name__)


id1 = {
    "name": "Cholera",
    "chapter": "Certain infectious and parasitic diseases",
    "block": "Certain intestinal infectious diseases"
}
id2 = {
    "name": "Typhoid and paratyphoid fevers",
    "chapter": "Certain infectious and parasitic diseases",
    "block": "Typhoid and paratyphoid fevers"
}


codex = {
    "id1": id1,
    "id2": id2
}


@app.route('/')
def get_codex():
    return jsonify(codex)


if __name__ == '__main__':
    app.run(debug=True)
