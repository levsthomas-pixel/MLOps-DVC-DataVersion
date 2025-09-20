import pandas as pd
import os

# create dictionnary

data = {"Name": ["Alice","Bob","Charlie"],
        "Age" : [25,30,35],
        "City" : ["New York", "Los Angeles","Chicago"]
        }

df = pd.DataFrame(data) 

data_dir="data"
os.makedirs(data_dir, exist_ok=True) #create directory at root level

file_path = os.path.join(data_dir,"sample_data.csv") #extracts file path and names it

df.to_csv(file_path,index=False) #converts data to csv file

print(f"csv word save to {file_path}")