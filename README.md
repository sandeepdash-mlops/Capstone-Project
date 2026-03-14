<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1a3a,100:7c3aed&height=220&section=header&text=Sentiment-Analysis&fontSize=75&fontColor=ffffff&fontAlignY=38&desc=End-to-End%20MLOps%20Pipeline%20%7C%20Train%20%E2%86%92%20Deploy%20%E2%86%92%20Scale%20%E2%86%92%20Observe&descAlignY=61&descSize=20&descColor=c4b5fd" alt="Sentiment MLOps Banner"/>

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)](https://mlflow.org/)
[![DVC](https://img.shields.io/badge/DVC-Pipelines-945DD6?style=for-the-badge&logo=dvc&logoColor=white)](https://dvc.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com/)
[![AWS EKS](https://img.shields.io/badge/AWS_EKS-Orchestration-FF9900?style=for-the-badge&logo=amazoneks&logoColor=white)](https://aws.amazon.com/eks/)
[![Prometheus](https://img.shields.io/badge/Prometheus-Metrics-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/Grafana-Dashboards-F46800?style=for-the-badge&logo=grafana&logoColor=white)](https://grafana.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![Status](https://img.shields.io/badge/Status-Production_Ready-16a34a?style=for-the-badge)]()

<br/>

> **End-to-end MLOps pipeline for sentiment classification — covering model training, experiment tracking, containerization, scalable cloud deployment on AWS EKS, CI/CD automation, and full observability with predictive autoscaling.**

</div>

---

## 📌 What This Project Demonstrates

This capstone covers the **complete MLOps lifecycle** that most projects stop halfway through. It goes beyond just training a model — it shows how to ship it, scale it, and observe it in production.

| Stage | What's Covered |
|---|---|
| 🧪 **Experimentation** | Tracked with MLflow + DagsHub, versioned with DVC |
| 🏗️ **Pipeline** | Reproducible `dvc.yaml` pipeline with `params.yaml` config |
| 🐳 **Packaging** | Dockerized Flask API, pushed to AWS ECR |
| ☁️ **Deployment** | Scalable inference on AWS EKS with LoadBalancer |
| 🔄 **CI/CD** | GitHub Actions workflow — test, build, push, deploy |
| 📊 **Observability** | Prometheus metrics + Grafana dashboards + Istio sidecars |
| ⚡ **Autoscaling** | Reactive (KEDA) + Predictive (PredictKube) scaling |

---

## 🏗️ Architecture Overview

```
 ┌─────────────────────────────────────────────────────────────────────┐
 │                        Developer Workflow                           │
 │   Code → DVC Pipeline → MLflow Experiment → Git Push               │
 └──────────────────────────────┬──────────────────────────────────────┘
                                │
                    ┌───────────▼───────────┐
                    │   GitHub Actions CI/CD │
                    │  Test → Build → Push   │
                    └───────────┬───────────┘
                                │
              ┌─────────────────▼──────────────────┐
              │           AWS ECR                   │
              │     Docker Image Registry           │
              └─────────────────┬──────────────────┘
                                │
              ┌─────────────────▼──────────────────┐
              │           AWS EKS Cluster           │
              │  ┌──────────┐  ┌──────────────────┐│
              │  │Flask Pods│  │  LoadBalancer Svc ││
              │  │(Inference│  │  (Port 5000)      ││
              │  │ + Istio) │  └──────────────────┘│
              │  └────┬─────┘                       │
              │       │  Metrics                    │
              │  ┌────▼──────────────────────────┐  │
              │  │ Prometheus → Grafana Dashboards│  │
              │  │ KEDA + PredictKube Autoscaler  │  │
              │  └───────────────────────────────┘  │
              └────────────────────────────────────┘
                                │
              ┌─────────────────▼──────────────────┐
              │         AWS S3 (DVC Remote)         │
              │   Data & Model Artifact Storage     │
              └────────────────────────────────────┘
```

---

## 📁 Repository Structure

```
sentiment-mlops/
├── .github/
│   └── workflows/
│       └── ci.yaml                 # 🔄 GitHub Actions CI/CD pipeline
├── flask_app/
│   ├── app.py                      # 🌐 Flask REST API for inference
│   ├── Dockerfile                  # 🐳 Container definition
│   └── requirements.txt
├── logger/                         # 📝 Logging utility
├── data_ingestion.py               # 📥 Load & validate datasets
├── data_preprocessing.py           # 🧹 Clean & preprocess text
├── feature_engineering.py          # ⚙️  Feature creation
├── model_building.py               # 🏋️ Train ML models
├── model_evaluation.py             # 📊 Evaluate & log metrics to MLflow
├── register_model.py               # 📦 Register models in MLflow registry
├── tests/                          # ✅ CI test scripts
├── scripts/                        # 🔧 Helper automation scripts
├── dvc.yaml                        # 🔁 DVC pipeline definition
├── params.yaml                     # ⚙️  Pipeline hyperparameters
└── README.md
```

---

## ⚡ Quick Setup

### 1️⃣ Environment

```bash
# Python 3.11 setup on Ubuntu 24.04
sudo apt update && sudo apt install python3.11 python3.11-venv python3.11-dev -y
python3.11 -m venv venv && source venv/bin/activate

# Project structure via cookiecutter
pip install cookiecutter
cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
```

### 2️⃣ DVC Pipeline

```bash
dvc init
dvc remote add -d myremote s3://<your-bucket>
pip install -r requirements.txt
dvc repro        # runs full pipeline end-to-end
dvc status       # check what's changed
```

### 3️⃣ MLflow Experiment Tracking

```bash
pip install mlflow dagshub
# Run experiment notebooks → view runs on DagsHub
# Register best model via register_model.py
```

### 4️⃣ Docker Build & Push to ECR

```bash
cd flask_app
docker build -t capstone-app:latest .
docker run -p 8888:5000 -e CAPSTONE_TEST=<token> capstone-app:latest

# Tag & push to AWS ECR
aws ecr get-login-password | docker login --username AWS --password-stdin <ecr-uri>
docker tag capstone-app:latest <ecr-uri>/capstone-app:latest
docker push <ecr-uri>/capstone-app:latest
```

### 5️⃣ AWS EKS Deployment

```bash
eksctl create cluster \
  --name flask-app-cluster \
  --region us-east-1 \
  --nodegroup-name flask-app-nodes \
  --node-type t3.small \
  --nodes 1 --nodes-min 2 --nodes-max 8 \
  --managed

aws eks --region us-east-1 update-kubeconfig --name flask-app-cluster
kubectl get nodes

# Deploy and verify
kubectl get pods && kubectl get svc
curl http://<external-ip>:5000
```

### 6️⃣ Observability & Autoscaling

```bash
# Prometheus + Grafana via Helm
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/kube-prometheus-stack

# KEDA for reactive autoscaling
helm repo add kedacore https://kedacore.github.io/charts
helm install keda kedacore/keda
```

**Metrics collected:**

| Metric | Type |
|---|---|
| `app_request_count_total` | App-level — request volume |
| `app_request_latency_seconds` | App-level — response latency |
| `model_prediction_count_total` | App-level — inference throughput |
| Istio sidecar metrics | Infra-level — service mesh telemetry |

---

## 🔄 CI/CD Pipeline

Every `git push` to `main` triggers the GitHub Actions workflow:

```
Push → Run Tests → Build Docker Image → Push to ECR → Deploy to EKS
```

Defined in `.github/workflows/ci.yaml` — no manual intervention required after merge.

---

## ⚡ Autoscaling Strategy

This project implements **two layers of autoscaling**:

**Reactive (KEDA)** — scales pods immediately when live metrics cross thresholds (e.g., request queue depth, CPU).

**Predictive (PredictKube)** — analyses historical traffic patterns and pre-scales before demand spikes hit — reducing cold-start latency for predictable workloads.

---

## 🧰 Tech Stack

| Category | Tools |
|---|---|
| 🐍 **Language & Framework** | Python 3.11, Flask |
| 🤖 **ML & Tracking** | Scikit-Learn, MLflow, DagsHub |
| 🔁 **Pipelines & Versioning** | DVC, GitHub Actions |
| 🐳 **Containerization** | Docker, AWS ECR |
| ☁️ **Cloud & Orchestration** | AWS EKS, S3, IAM, eksctl, kubectl |
| ⚡ **Autoscaling** | KEDA, PredictKube |
| 📊 **Observability** | Prometheus, Grafana, Istio |

---

## 📐 Design Decisions

**Why DVC over raw scripts?**
DVC makes the pipeline reproducible and data/model versioning auditable — critical for ML compliance and debugging production regressions.

**Why KEDA + PredictKube together?**
KEDA reacts to what's happening now. PredictKube anticipates what's about to happen. Together they eliminate both over-provisioning waste and cold-start latency.

**Why Istio alongside Prometheus?**
App-level metrics alone miss infrastructure-level failures. Istio sidecar metrics give full service mesh visibility without changing application code.

---

## 💬 Connect

<div align="center">

📧 **Email:** sandeepdashmlops@gmail.com
&nbsp;&nbsp;|&nbsp;&nbsp;
💻 **GitHub:** [github.com/sandeepdash-mlops](https://github.com/sandeepdash-mlops)

</div>

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7c3aed,50:1a1a3a,100:0d1117&height=120&section=footer" alt="footer"/>

*Train it. Ship it. Scale it. Watch it.*

</div>
