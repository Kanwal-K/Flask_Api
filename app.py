import os
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# --- Arithmetic Services (Using Query Parameters) ---

@app.route("/")
def hello():
    # How to call: http://127.0.0.1:5000/
    return "Hello, CI/CD! This is a simple REST API."


@app.route("/add", methods=["GET"])
def add_numbers():
    """Calculates a + b using query parameters."""
    # How to call: http://127.0.0.1:5000/add?a=7&b=6
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"result": a + b})
    except ValueError:
        return jsonify({"error": "Invalid input: 'a' and 'b' must be integers"}), 400


@app.route("/subtract", methods=["GET"])
def subtract_numbers():
    """Calculates a - b using query parameters."""
    # How to call: http://127.0.0.1:5000/subtract?a=7&b=78
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"result": a - b})
    except ValueError:
        return jsonify({"error": "Invalid input: 'a' and 'b' must be integers"}), 400


@app.route("/multiply", methods=["GET"])
def multiply_numbers():
    """Calculates a * b using query parameters."""
    # How to call: http://127.0.0.1:5000/multiply?a=4&b=11
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"result": a * b})
    except ValueError:
        return jsonify({"error": "Invalid input: 'a' and 'b' must be integers"}), 400


# ✅ NEW: division route
@app.route("/divide", methods=["GET"])
def divide_numbers():
    """Calculates a / b using query parameters, handling division by zero."""
    # How to call: http://127.0.0.1:5000/divide?a=100&b=4
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        
        if b == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 400
        
        # Use floating-point division
        return jsonify({"result": a / b})
    except ValueError:
        return jsonify({"error": "Invalid input: 'a' and 'b' must be integers"}), 400

# --- General Service (Using Path Parameters) ---

# ✅ NEW: path parameter route
@app.route("/greet_user/<name>", methods=["GET"])
def greet_user(name):
    """Greets a user, using the name directly from the URL path."""
    # How to call: http://127.0.0.1:5000/greet_user/Alex
    return jsonify({"message": f"Hello, {name}! Welcome to the calculator service."})


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False,
        use_reloader=False,
    )