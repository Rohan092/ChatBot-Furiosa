from flask import Flask, render_template, request, jsonify
import cohere

API_KEY= "k9x8LaddShvywjdTlsn0uZtbk2XNpdCK8WES1tYn"
co = cohere.Client(API_KEY)

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("FurisoaChat.html")

@app.route("/get", methods=["GET","POST"])
def chat():
    msg = request.form["msg"]
    response = chat_with_Furiosa(msg)
    return response

def chat_with_Furiosa(text):

    response = co.generate(
        model="command",  
        prompt=text,
        max_tokens=500,
        temperature=0.7,
        stop_sequences=["END"]
    )

    if text.lower() in ["quit", "exit", "bye"]:
        return "Goodbye!"
    return response.generations[0].text.strip()


if __name__== "__main__":
    app.run()