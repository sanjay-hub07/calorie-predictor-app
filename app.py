import numpy as np
from flask import Flask, request, render_template
import joblib

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('calories_model.pkl')

# Define the home page route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get all the input values from the form as a list
        features = [x for x in request.form.values()]
        
        # The first feature is Gender, which is text. We handle it separately.
        gender = features[0].lower()
        if gender == 'male':
            features[0] = 0
        elif gender == 'female':
            features[0] = 1
        else:
            # If gender is invalid, return an error message
            return render_template('index.html', prediction_text='Error: Please enter a valid gender (male/female).')

        # Convert the rest of the features to float
        final_features = [np.array(features).astype(float)]

        # Make the prediction
        prediction = model.predict(final_features)
        
        output = round(prediction[0], 2)

        # Render the same page with the prediction result
        return render_template('index.html', prediction_text=f'Predicted Calories Burnt: {output} kcal')

    except Exception as e:
        # Handle potential errors like non-numeric input
        return render_template('index.html', prediction_text=f'Error during prediction: {e}')

if __name__ == "__main__":
    app.run(debug=True)