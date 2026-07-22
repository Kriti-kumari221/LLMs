from flask import Flask, render_template, request, jsonify

from chatbot import (
    load_video,
    ask_question
)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/load_video", methods=["POST"])
def load():

    try:

        data = request.get_json()

        url = data["url"]

        load_video(url)

        return jsonify(
            {
                "message": "Video Loaded Successfully"
            }
        )

    except Exception as e:

        return jsonify(
            {
                "error": str(e)
            }
        )


@app.route("/ask", methods=["POST"])
def ask():

    try:

        data = request.get_json()

        question = data["question"]

        answer = ask_question(question)

        return jsonify(
            {
                "answer": answer
            }
        )

    except Exception as e:

        return jsonify(
            {
                "answer": str(e)
            }
        )


if __name__ == "__main__":

    app.run(
        debug=True,
        use_reloader=False
    )