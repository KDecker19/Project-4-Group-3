# Import Depancies for Data preprocessing and database storage to MongoDB

import pandas as pd 
import numpy as np
import pymongo 
from pymongo import MongoClient
import json
import os
import pandas as pd

# Function to read the data from the resource folder

file_path = "/Users/kalebdecker/Documents/GitHub/Project-4-Group-3/Data/data.csv"

# Function to read the data from the resource folder

def read_data(file_path):
    data = pd.read_csv(file_path)
    return data
