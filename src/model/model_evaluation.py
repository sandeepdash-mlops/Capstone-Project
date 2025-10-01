import os
import numpy as np
import pandas as pd
import pickle
import json
import logging
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
import mlflow
import mlflow.sklearn
import dagshub
from src.logger import logging

# ------------------- DagsHub + MLflow setup for local -------------------

# Make sure you have exported your token:
# export DAGSHUB_TOKEN=<your_personal_access_token>
DAGSHUB_TOKEN = os.environ.get("DAGSHUB_TOKEN")
if not DAGSHUB_TOKEN:
    raise ValueError("DAGSHUB_TOKEN environment variable is not set.")

# Authenticate with DagsHub using the token
dagshub.auth.add_app_token(token=DAGSHUB_TOKEN)

# Initialize DagsHub repo integration with MLflow
dagshub.init(
    repo_owner='sandeepdash-mlops',
    repo_name='Capstone-Project',
    mlflow=True
)

# Set MLflow tracking URI to DagsHub
mlflow.set_tracking_uri('https://dagshub.com/sandeepdash-mlops/Capstone-Project.mlflow')

# Below code block is for production use
# -------------------------------------------------------------------------------------
# Set up DagsHub credentials for MLflow tracking
# dagshub_token = os.getenv("CAPSTONE_TEST")
# if not dagshub_token:
#     raise EnvironmentError("CAPSTONE_TEST environment variable is not set")

# os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
# os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

# dagshub_url = "https://dagshub.com"
# repo_owner = "sandeepdash-mlops"
# repo_name = "Capstone-Project"

# # Set up MLflow tracking URI
# mlflow.set_tracking_uri(f'{dagshub_url}/{repo_owner}/{repo_name}.mlflow')
# -------------------------------------------------------------------------------------

# ------------------- Helper Functions -------------------

def load_model(file_path: str):
    try:
        with open(file_path, 'rb') as file:
            model = pickle.load(file)
        logging.info('Model loaded from %s', file_path)
        return model
    except FileNotFoundError:
        logging.error('File not found: %s', file_path)
        raise
    except Exception as e:
        logging.error('Unexpected error while loading the model: %s', e)
        raise

def load_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        logging.info('Data loaded from %s', file_path)
        return df
    except pd.errors.ParserError as e:
        logging.error('Failed to parse CSV: %s', e)
        raise
    except Exception as e:
        logging.error('Unexpected error while loading data: %s', e)
        raise

def evaluate_model(clf, X_test: np.ndarray, y_test: np.ndarray) -> dict:
    try:
        y_pred = clf.predict(X_test)
        y_pred_proba = clf.predict_proba(X_test)[:, 1]

        metrics_dict = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'auc': roc_auc_score(y_test, y_pred_proba)
        }
        logging.info('Evaluation metrics calculated')
        return metrics_dict
    except Exception as e:
        logging.error('Error during model evaluation: %s', e)
        raise

def save_metrics(metrics: dict, file_path: str) -> None:
    try:
        with open(file_path, 'w') as f:
            json.dump(metrics, f, indent=4)
        logging.info('Metrics saved to %s', file_path)
    except Exception as e:
        logging.error('Error saving metrics: %s', e)
        raise

def save_model_info(run_id: str, model_path: str, file_path: str) -> None:
    try:
        with open(file_path, 'w') as f:
            json.dump({'run_id': run_id, 'model_path': model_path}, f, indent=4)
        logging.info('Model info saved to %s', file_path)
    except Exception as e:
        logging.error('Error saving model info: %s', e)
        raise

# ------------------- Main Function -------------------

def main():
    mlflow.set_experiment("my-dvc-pipeline")
    
    with mlflow.start_run() as run:
        try:
            # Load model and test data
            clf = load_model('./models/model.pkl')
            test_data = load_data('./data/processed/test_bow.csv')
            
            X_test = test_data.iloc[:, :-1].values
            y_test = test_data.iloc[:, -1].values

            # Evaluate
            metrics = evaluate_model(clf, X_test, y_test)
            save_metrics(metrics, 'reports/metrics.json')

            # Log metrics to MLflow
            for name, value in metrics.items():
                mlflow.log_metric(name, value)

            # Log model parameters
            if hasattr(clf, 'get_params'):
                params = clf.get_params()
                for name, value in params.items():
                    mlflow.log_param(name, value)

            # Log model to MLflow
            mlflow.sklearn.log_model(clf, "model")

            # Save model info
            save_model_info(run.info.run_id, "model", 'reports/experiment_info.json')

            # Log metrics file as artifact
            mlflow.log_artifact('reports/metrics.json')

            logging.info("Model evaluation completed and logged to MLflow.")

        except Exception as e:
            logging.error('Failed to complete model evaluation: %s', e)
            print(f"Error: {e}")

if __name__ == '__main__':
    main()

