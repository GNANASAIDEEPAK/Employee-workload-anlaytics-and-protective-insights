import pandas as pd

def load_data():
    data = pd.read_csv("data/employee_workload.csv")
    return data

def preprocess(data):
    data = data.dropna()
    data["Workload_Score"] = data["Hours_Worked"] / 40
    return data