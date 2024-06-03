# Hate Speech Detection

[PRESENTATION](https://docs.google.com/presentation/d/1blVqvcNYWqYBkql37pqWD1aiWSIp0-zbDb1JLmgNTL0/edit#slide=id.p)

Try it now: [http://188.119.67.145:8000/](http://188.119.67.145:8000/)

## Table of Contents

- [Description](#Description)
- [Setup](#Setup)
- [Dataset](#Dataset)
- [Models](#Models)
- [Metrics](#Metrics)

## Description

Machine learning project for classifying the user's tweets into 3 categories: neutral, negative, and positive.

## Setup

Install python dependencies:

```pip install -r requirements.txt```

Run the server locally:

```uvicorn main:app --host 127.0.0.1 --port 8000```

## Dataset

We trained all our models on [this dataset](https://www.kaggle.com/datasets/saurabhshahane/twitter-sentiment-dataset).

## Models

- CatBoost
- Logistic Regression
- Random Forest

## Metrics

We used the `balanced_accuracy_score` since the target distribution is not uniform.

The value of `balanced_accuracy_score` is in the range from 0.89 to 0.95 depending on the models.
