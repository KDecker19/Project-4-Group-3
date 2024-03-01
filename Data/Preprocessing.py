# Import Depancies for Data preprocessing and database storage to MongoDB

import pandas as pd 
import numpy as np
import pymongo 
from pymongo import MongoClient
import json
import os

# Function to read the data from the csv file

def read_data(file_path):

    # Read the data from the csv file
    data = pd.read_csv(file_path)

    # Return the data
    return data

# Function to clean the data

def clean_data(data):
    
        # Drop the rows with missing values
        data = data.dropna()
    
        # Return the cleaned data
        return data

# Function to store the data in the MongoDB database

def store_data(data, collection_name):
    
    # Connect to the MongoDB database
    client = MongoClient('localhost', 27017)
    
    # Create a new database
    db = client['data']
    
    # Create a new collection
    collection = db[collection_name]
    
    # Convert the data to a dictionary
    data = data.to_dict(orient='records')
    
    # Insert the data into the collection
    collection.insert_many(data)

# Function to read the data from the MongoDB database
    
def read_mongo(collection_name):
     
    # Connect to the MongoDB database
    client = MongoClient('localhost', 27017)
    
    # Create a new database
    db = client['data']
    
    # Create a new collection
    collection = db[collection_name]
    
    # Read the data from the collection
    data = collection.find()
    
    # Convert the data to a dataframe
    data = pd.DataFrame(list(data))
    
    # Drop the '_id' column
    data = data.drop(['_id'], axis=1)
    
    # Return the data
    return data

# Function to preprocess the data

def preprocess_data(file_path, collection_name):
     
    # Read the data from the csv file
    data = read_data(file_path)
    
    # Clean the data
    data = clean_data(data)
    
    # Store the data in the MongoDB database
    store_data(data, collection_name)

    # Return the data
    return data

# Function to read the data from the MongoDB database

def read_mongo(collection_name):
     
    # Connect to the MongoDB database
    client = MongoClient('localhost', 27017)
    
    # Create a new database
    db = client['data']
    
    # Create a new collection
    collection = db[collection_name]
    
    # Read the data from the collection
    data = collection.find()
    
    # Convert the data to a dataframe
    data = pd.DataFrame(list(data))
    
    # Drop the '_id' column
    data = data.drop(['_id'], axis=1)
    
    # Return the data
    return data