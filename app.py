from flask import Flask, request, jsonify, render_template
import random
app = Flask(__name__)


greetings = [
    "Hello there!",
    "Hi! How can I help?",
    "Hey"
]


@app.route("/")
def home():
    return render_template("index.html")

# What is methods=["POST"]?

# Web requests have types.

# The two important ones:

# GET	Asking for page  When browser loads homepage:It sends GET request.
# POST	Sending data When JavaScript sends message:It sends POST request.


@app.route("/chat", methods=["POST"])
def chat():
    # read input, normalize and trim whitespace : .strip()
    user_input = request.json["message"].lower().strip()

    if user_input == "":
        response = "Please type something"

    if user_input == "hi" or user_input == "hello":
        response = random.choice(greetings)
    elif "course" in user_input:
        response = "We offer BCA, BSc CS, and BCom."
    elif user_input == "faculty":
        response = "HOD - Dr. Kumar, CS Faculty - Ms. Anjali"
    elif user_input == "bye" or user_input == "exit":
        response = "See you later."
    else:
        response = "I don't understand that."
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
