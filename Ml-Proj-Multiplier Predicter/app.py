from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved best regression model
model = joblib.load("best_aviator_regressor.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            # Get inputs from form and convert to proper types
            color = int(request.form.get("color"))
            mean = float(request.form.get("mean"))
            var = float(request.form.get("var"))
            next_approximate = float(request.form.get("next_approximate"))

            # Prepare input array for prediction
            input_features = np.array([[color, mean, var, next_approximate]])

            # Predict multiplier
            pred = model.predict(input_features)[0]
            prediction = round(pred, 3)

        except Exception as e:
            error = f"Invalid input or error during prediction: {e}"

    return render_template("index.html", prediction=prediction, error=error)

if __name__ == "__main__":
    app.run(debug=True)
