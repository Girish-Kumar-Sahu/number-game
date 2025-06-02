from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def guess_game():
    result = ""
    answer = None
    if request.method == "POST":
        try:
            num1 = int(request.form["num1"])
            num2 = int(request.form["num2"])
            guess = int(request.form["guess"])
            answer = random.randint(min(num1, num2), max(num1, num2))

            if guess == answer:
                result = "🎉 Correct!"
            elif guess > answer:
                result = "📈 Too high!"
            else:
                result = "📉 Too low!"
        except ValueError:
            result = "❗ Invalid input. Please enter valid numbers."
    
    return render_template("index.html", result=result, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
