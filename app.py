from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_input = request.form["msg"].lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! Welcome to VTU College Chatbot 👋"

    elif "placement" in user_input:
        return "VTU colleges provide placement opportunities with top companies."

    elif "course" in user_input:
        return "VTU offers BE, BTech, MTech, MBA and other courses."

    elif "fee" in user_input:
        return "Fees depend on the course and Branch    ."

    elif "exam" in user_input:
        return "VTU exams are conducted semester-wise."

    elif "result" in user_input:
        return "You can check VTU results on the official website."

    else:
        return 'For more info 👉 <a href="https://vtu.ac.in" target="_blank" style="color:blue; font-weight:bold;">VTU Official Website</a>'

if __name__ == "__main__":
    app.run(debug=True)