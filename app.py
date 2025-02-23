from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({"error": "Missing parameters"}), 400
    return jsonify({"result": a + b})

if __name__ == '__main__':
    app.run(debug=True)
