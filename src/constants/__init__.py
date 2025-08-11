import os,sys
from datetime import datetime

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_time_stamp()

ROOT_DIR_KEY = os.getcwd()
DATA_DIR = "Data"
DATA_DIR_KEY = "finaltrain.csv"

ARTIFACT_DIR_KEY = "Artifact"

# data ingestion
DATA_INGESTION_KEY = "Data_Ingestion"
DATA_INGESTION_RAW_DATA_DIR = "raw_data_dir"
DATA_INGESTION_INGESTED_DIR_KEY = "ingested_dir"
RAW_DATA_DIR_KEY = "raw.csv"
TRAIN_DATA_DIR_KEY = "train.csv"
TEST_DATA_DIR_KEY = "test.csv"

# data transformation
DATA_TRANSFORMATION_ARTIFACT = "Data_Transformation"
DATA_PREPROCESSED_DIR = "processor"
DATA_TRANSFORMATION_PREPROCESSING_OBJ = "processor.pkl"
DATA_TRANSFORMATION_DIR = "transformation"
TRANSFORMED_TRAIN_DIR_KEY = "train.csv"
TRANSFORMED_TEST_DIR_KEY = "test.csv"

#model training

MODEL_TRAINER_KEY = "model_trainer"
MODEL_OBJ = "model.pkl"