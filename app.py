from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Simple Python Calculator! Use /add or /multiply endpoints."

@app.route('/add')
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a + b
        return jsonify({"operation": "addition", "a": a, "b": b, "result": result})
    except:
        return jsonify({"error": "Please provide valid query parameters a and b"}), 400

@app.route('/multiply')
def multiply():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a * b
        return jsonify({"operation": "multiplication", "a": a, "b": b, "result": result})
    except:
        return jsonify({"error": "Please provide valid query parameters a and b"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
