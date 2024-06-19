# Risk Evaluation Prediction API using PyCaret and Flask

This repository contains a machine learning prediction API built using Flask and PyCaret. The API loads a pre-trained model, accepts input data via POST requests, and returns predictions.

## Context

The objective is to create a proof-of-concept (POC) for providing risk evaluation as a service for retail banks. This involves downloading and analyzing a dataset from Home Credit Group, performing exploratory data analysis (EDA), applying statistical inference, and building multiple machine learning models to predict loan default risk. These models are then deployed to Google Cloud Platform for easy access via HTTP requests.

## Objectives

- Translate business requirements into data science tasks.
- Perform exploratory data analysis (EDA).
- Apply statistical inference procedures.
- Use machine learning to solve business problems.
- Deploy machine learning model.

## Getting Started

### Prerequisites

- Python 3.10
- pip (Python package installer)
- Docker (optional, for containerization)

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/prediction-api.git
    cd app
    ```

2. **Create and activate a virtual environment:**

    - On Windows:
    
        ```sh
        python -m venv myenv
        myenv\Scripts\activate
        ```

    - On MacOS/Linux:
    
        ```sh
        python3 -m venv myenv
        source myenv/bin/activate
        ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Place your model files in the project directory:**

    Ensure you have the `best_model_pycaret.pkl` file in the root directory of the project.

### Running the Application

1. **Start the Flask application:**

    ```sh
    python app.py
    ```

2. **The API will be available at:**

    ```
    http://127.0.0.1:8000
    ```

### Using the API

#### Root Endpoint

- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns a welcome message.

    ```sh
    curl http://127.0.0.1:8000/
    ```

#### Prediction Endpoint

- **URL:** `/predict`
- **Method:** `POST`
- **Description:** Accepts input data and returns predictions.

- **Request Body Example contains in `input.json` file.**   

- **Example Request:**

    ```sh
    curl -X POST -H "Content-Type: application/json" -d @input.json http://127.0.0.1:8000/predict
    ```

- **Example Response:**

    ```json
    [
        {
            "prediction_label": 0,
            "prediction_score": 0.9238
        }
    ]
    ```
### Deployed Model

The model has been deployed to Google Cloud Run and is accessible at the following URL:

```
https://predict-khkn75yyfq-lm.a.run.app
```

You can test the deployed model using the same `input.json` file and the following `curl` command:

```sh
curl -X POST -H "Content-Type: application/json" -d @input.json https://predict-khkn75yyfq-lm.a.run.app/predict
```

Or by running prepared python scrypt in `api_test.py` file.
