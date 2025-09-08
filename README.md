---
title: Gas Price Prediction API
sdk: docker
app_port: 8000
---

# Gas Price Prediction API with Docker ⛽

This project demonstrates a complete ML Ops workflow by taking a trained machine learning model and deploying it as a containerized REST API using FastAPI and Docker.

### Project Overview

The core of this project is a simple linear regression model, trained on historical U.S. gas price data, which predicts the next week's price based on the previous week's price. This model is wrapped in a FastAPI application to expose a `/predict` endpoint.

The entire application is then containerized using Docker, creating a portable and scalable service that can be deployed anywhere.

### Technologies Used

* **ML/Data Science:** Scikit-learn, Pandas, Joblib
* **API Development:** FastAPI, Uvicorn
* **Deployment:** Docker
* **Language:** Python

### How to Run This Project

#### 1. Build the Docker Image
From the root of the project directory, run the `docker build` command:
```bash
docker build -t gas-price-api .
