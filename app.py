from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({"error": "Missing parameters"}), 400
    return jsonify({"result": a + b})

@app.route('/subtract')
def subtract():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({"error": "Missing parameters"}), 400
    return jsonify({"result": a - b})

@app.route('/multiply')
def multiply():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({"error": "Missing parameters"}), 400
    return jsonify({"result": a * b})

@app.route('/divide')
def divide():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({"error": "Missing Parameters"}), 400
    elif b == 0:
        return jsonify({"error": "Cannot divide by Zero"}), 400 
    return jsonify({"result": a / b})

if __name__ == '__main__':
    app.run(debug=True)



