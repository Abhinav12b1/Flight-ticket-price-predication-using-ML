import pickle
import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model
model_path = os.path.join(os.getcwd(), "model1.pkl")
if os.path.exists(model_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
else:
    model = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            # Extract input features
            features = [float(request.form[key]) for key in request.form.keys()]
            input_data = [features]

            if model:
                prediction = model.predict(input_data)[0]
                return render_template("result.html", price=prediction)
            else:
                return "Model not loaded. Train and save 'model1.pkl'."

        except Exception as e:
            return f"Error: {e}"

    return render_template("predict.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
