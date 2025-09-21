# Calories Burnt Prediction Web App

This project is an end-to-end machine learning application that predicts the number of calories a person burns during exercise. The prediction is based on personal and exercise-specific data, such as age, gender, duration, heart rate, and body temperature.

The project starts with data exploration and model training in a Jupyter Notebook and culminates in a deployed, interactive web application built with Flask.

##  Live Demo

You can access the live, deployed web application here:

**(Replace this with your Render URL)**
`https://my-calorie-predictor.onrender.com `

---

## Features

-   **Interactive Web Interface:** A user-friendly form to input exercise and personal data.
-   **ML-Powered Predictions:** Utilizes a trained **XGBoost Regressor** model to provide accurate calorie predictions.
-   **Real-time Results:** Displays the predicted calories burnt instantly on the same page.
-   **Cloud Deployed:** The application is deployed on Render, making it publicly accessible.

---

## Tech Stack

-   **Backend:** Python, Flask, Gunicorn
-   **Data Science & ML:** Pandas, NumPy, Scikit-learn, XGBoost, Joblib
-   **Frontend:** HTML, CSS
-   **Deployment:** Render, Git & GitHub

---

## Project Structure

```
├── calories_predictor_project/
│   ├── app.py                  # The Flask application backend
│   ├── calories_model.pkl      # The pre-trained XGBoost model file
│   ├── requirements.txt        # Python dependencies for the project
│   └── templates/
│       └── index.html          # The HTML file for the user interface
├── Calories_Burnt_Prediction.ipynb # The original Colab notebook for data analysis and model training
└── README.md
```
---

## How to Run Locally

To run this project on your own machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    ```bash
    python app.py
    ```

5.  **Open your browser** and navigate to `http://127.0.0.1:5000` to see the application running.

   ## Output
   <img width="1919" height="1145" alt="image" src="https://github.com/user-attachments/assets/0d5c8f73-5e6f-4340-9c90-d9b92ecbb4b2" />


