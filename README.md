````markdown
# 🎬 Sentiment Analysis – MLOps Capstone Project
**End-to-end development, deployment, scalable inference, and observability of model performance**

- Status: Production-ready
- Python: 3.11
- DVC: Pipeline & Versioning
- MLFlow: Experiment Tracking
- Docker: Containerization
- Kubernetes: EKS (Orchestration)

---

## 🚀 Project Description

This project addresses a **text classification problem** under supervised machine learning. The goal is to predict the **sentiment of movie reviews**, classifying them as **positive** or **negative**.

It demonstrates an **end-to-end MLOps pipeline** including:

- Data ingestion, preprocessing, feature engineering
- Model training, evaluation, and registration
- Deployment with Docker and Flask
- Scalable deployment on AWS EKS
- CI/CD pipeline automation
- Observability and predictive autoscaling

---

## 🏗 Project Setup & Structure

### 1️⃣ Environment Setup

1. Clone repository on Ubuntu 24.04
2. Install dependencies and setup Python 3.11 virtual environment:

```bash
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-dev -y

python3.11 -m venv venv
source venv/bin/activate
python --version
````

3. Install `cookiecutter` and create project structure:

```bash
pip install cookiecutter
cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
mv src.models src.model
git add . && git commit -m "Initial project structure" && git push
```

---

### 2️⃣ MLFlow Setup

1. Install MLFlow & Dagshub:

```bash
pip install mlflow dagshub
```

2. Run experiment notebooks, commit changes
3. Copy experiment tracking URL for MLFlow
4. Register models in MLFlow

---

### 3️⃣ DVC Setup

1. Initialize DVC:

```bash
dvc init
mkdir local_s3
dvc remote add -d mylocal local_s3
pip install -r requirements.txt
```

2. Add pipeline files:

* `dvc.yaml`
* `params.yaml`

3. Track project data & models with DVC:

```bash
dvc repro
dvc status
git add . && git commit -m "DVC pipeline ready" && git push
```

4. Setup AWS S3 as remote storage:

```bash
pip install dvc[s3] awscli
aws configure
dvc remote add -d myremote s3://<bucket-name>
```

---

### 4️⃣ Flask App & Docker

1. Create `flask_app` directory and setup REST API
2. Install dependencies:

```bash
pip install flask
pip freeze > requirements.txt
```

3. Dockerize application:

```bash
cd flask_app
pipreqs . --force
docker build -t capstone-app:latest .
docker run -p 8888:5000 -e CAPSTONE_TEST=<token> capstone-app:latest
```

4. Push Docker image to AWS ECR
5. CI/CD pipeline via GitHub Actions (`.github/workflows/ci.yaml`)

---

### 5️⃣ AWS EKS Deployment

1. Setup AWS CLI, kubectl, eksctl on Ubuntu 24.04
2. Create EKS cluster:

```bash
eksctl create cluster --name flask-app-cluster --region us-east-1 --nodegroup-name flask-app-nodes --node-type t3.small --nodes 1 --nodes-min 2 --nodes-max 8 --managed
aws eks --region us-east-1 update-kubeconfig --name flask-app-cluster
kubectl get nodes
```

3. Deploy Flask app on EKS
4. Configure LoadBalancer service, security group for port 5000
5. Verify deployment:

```bash
kubectl get pods
kubectl get svc
curl http://<external-ip>:5000
```

---

### 6️⃣ Observability & Autoscaling

1. Setup Prometheus & Grafana via Helm
2. Collect metrics:

* App-level: `app_request_count_total`, `app_request_latency_seconds`, `model_prediction_count_total`
* Infrastructure-level: Istio sidecar metrics

3. Configure KEDA for reactive scaling
4. Integrate PredictKube for predictive scaling using historical metrics
5. Visualize scaling & metrics in Grafana dashboards

---

### 7️⃣ Key Scripts & Modules

* `logger/` – Logging utility
* `data_ingestion.py` – Load & validate datasets
* `data_preprocessing.py` – Clean & preprocess text
* `feature_engineering.py` – Feature creation
* `model_building.py` – Train ML models
* `model_evaluation.py` – Evaluate & log metrics
* `register_model.py` – Register models in MLFlow
* `tests/` – CI testing scripts
* `scripts/` – Helper scripts for automation

---

## 🛠 Technologies Used

| Category               | Tools & Services                       |
| ---------------------- | -------------------------------------- |
| Programming            | Python 3.11, Flask                     |
| ML & Data Science      | scikit-learn, pandas, numpy, MLFlow    |
| Versioning & Pipelines | DVC, GitHub Actions                    |
| Containerization       | Docker                                 |
| Cloud & Orchestration  | AWS EKS, IAM, S3, ECR, kubectl, eksctl |
| Autoscaling            | KEDA, PredictKube                      |
| Observability          | Prometheus, Grafana, Istio             |

---

## References

* MLFlow Documentation
* DVC Docs
* AWS EKS Docs
* KEDA Docs
* PredictKube
* Prometheus
* Grafana

---

## 💬 Connect
If you found this project helpful or have any questions, feel free to reach out!


📱 Phone: (+91) 7008-62-6663

📧 Email: sandeepdashmlops@gmail.com

💻 GitHub: https://github.com/sandeepdash-mlops

---

This capstone demonstrates the ability to build, deploy, monitor, and scale ML applications in a production environment, combining modern MLOps practices with cloud-native deployment, autoscaling, and ML no. of inference/prediction with observability solutions. It involves building a supervised machine learning model to classify reviews as positive or negative and deploying it in a production-ready, scalable environment.
