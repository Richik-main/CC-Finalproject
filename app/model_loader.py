# -*- coding: utf-8 -*-
"""model_loader.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18VY8R2fvvy3gEcGgx30biKMQo3aDFqzs
"""

import h2o
import boto3
from config.config import S3_BUCKET, S3_MODEL_KEY, LOCAL_MODEL_PATH

# Initialize H2O
h2o.init()

def download_model_from_s3():
    """Download the H2O model from S3."""
    s3 = boto3.client('s3')
    s3.download_file(S3_BUCKET, S3_MODEL_KEY, LOCAL_MODEL_PATH)
    print("Model downloaded from S3.")

def load_model():
    """Load the H2O model from the local file system."""
    download_model_from_s3()
    model = h2o.load_model(LOCAL_MODEL_PATH)
    print("Model loaded successfully.")
    return model

# Load the model at startup
h2o_model = load_model()